'''
Created on 23.10.2018

@author: schmied
'''

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.treeview import TreeViewLabel, TreeView
from kivy.properties import (ObjectProperty, StringProperty, OptionProperty,
                             ListProperty, BooleanProperty)
from kivy.lang import Builder
from kivy.utils import platform
from kivy.clock import Clock
from kivy.compat import PY2
import string
from os.path import sep, dirname, expanduser, isdir, join
from os import walk
from sys import getfilesystemencoding
from functools import partial

if platform == 'win':
    from ctypes import windll, create_unicode_buffer

Builder.load_file('ui/fs_browser.kv')

def get_drives():
    drives = []
    
    if platform == 'win':
        bitmask = windll.kernel32.GetLogicalDrives()
        GetVolumeInformationW = windll.kernel32.GetVolumeInformationW
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                name = create_unicode_buffer(64)
                # get name of the drive
                drive = letter + u':'
                res = GetVolumeInformationW(drive + sep, name, 64, None,
                                            None, None, None, 0)
                drives.append((drive, name.value))
            bitmask >>= 1
    return drives


class TreeLabel(TreeViewLabel):
    path = StringProperty('')
    '''Full path to the location this node points to.

    :class:`~kivy.properties.StringProperty`, defaults to ''
    '''


class LinkTree(TreeView):
    
    # link to the favorites section of link bar
    _computer_node = None

    def fill_tree(self):

        self._computer_node = self.add_node(TreeLabel(text='Computer',\
        is_open=True, no_selection=True))
        self._computer_node.bind(on_touch_down=self._drives_touch)
        self.reload_drives()

    def _drives_touch(self, obj, touch):
        if obj.collide_point(*touch.pos):
            self.reload_drives()

    def reload_drives(self):
        nodes = [(node, node.text + node.path) for node in\
                 self._computer_node.nodes if isinstance(node, TreeLabel)]
        sigs = [s[1] for s in nodes]
        nodes_new = []
        sig_new = []
        for path, name in get_drives():
            if platform == 'win':
                text = u'{}({})'.format((name + ' ') if name else '', path)
            else:
                text = name
            nodes_new.append((text, path))
            sig_new.append(text + path + sep)
        for node, sig in nodes:
            if sig not in sig_new:
                self.remove_node(node)
        for text, path in nodes_new:
            if text + path + sep not in sigs:
                self.add_node(TreeLabel(text=text, path=path + sep),
                              self._computer_node)

    def trigger_populate(self, node):
        if not node.path or node.nodes:
            return
        parent = node.path
        _next = next(walk(parent))
        if _next:
            for path in _next[1]:
                self.add_node(TreeLabel(text=path, path=parent + sep + path),
                              node)


class FS_Browser(BoxLayout):
    '''FileBrowser class, see module documentation for more information.
    '''
    __events__ = ('on_canceled', 'on_success')
    
    success_string  = StringProperty('Ok')
    cancel_string   = StringProperty('Cancel')
    filename        = StringProperty('')
    selection       = ListProperty([])
    path            = StringProperty(u'/')
    filters         = ListProperty([])
    filter_dirs     = BooleanProperty(False)
    show_hidden     = BooleanProperty(False)
    multiselect     = BooleanProperty(False)
    dirselect       = BooleanProperty(False)

    def on_success(self):
        pass

    def on_canceled(self):
        pass

    def __init__(self, **kwargs):
        super(FS_Browser, self).__init__(**kwargs)
        Clock.schedule_once(self._post_init)
        
        self.button_success.text    = self.success_string
        self.button_cancel.text     = self.cancel_string
        
        
    def _post_init(self, *largs):
        self.ids.list_view.bind(
            selection   = partial(self._attr_callback, 'selection'),
            path        = partial(self._attr_callback, 'path'),
            filters     = partial(self._attr_callback, 'filters'),
            filter_dirs = partial(self._attr_callback, 'filter_dirs'),
            show_hidden = partial(self._attr_callback, 'show_hidden'),
            multiselect = partial(self._attr_callback, 'multiselect'),
            rootpath    = partial(self._attr_callback, 'rootpath')
            )

    def _shorten_filenames(self, filenames):
        if not len(filenames):
            return ''
        elif len(filenames) == 1:
            return filenames[0]
        elif len(filenames) == 2:
            return filenames[0] + ', ' + filenames[1]
        else:
            return filenames[0] + ', _..._, ' + filenames[-1]

    def _attr_callback(self, attr, obj, value):
        setattr(self, attr, getattr(obj, attr))
        
        
if __name__ == '__main__':
    
    from kivy.app import App

    class TestApp(App):

        def build(self):
            fs_browser = FS_Browser(success_string = "enter", cancel_string = "exit")
            
            fs_browser.bind(
                on_success  = self._success, 
                on_canceled = self._canceled
                )
            return fs_browser
        
        def _canceled(self, instance):
            import sys
            sys.exit()
        
        def _success(self, instance):
            print("test")
        
    TestApp().run()