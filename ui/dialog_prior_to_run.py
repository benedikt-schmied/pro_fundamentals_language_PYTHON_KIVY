'''
Created on 23.10.2018

@author: schmied
'''

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (ObjectProperty, StringProperty, OptionProperty,
                             ListProperty, BooleanProperty)
from kivy.lang import Builder
Builder.load_file('ui/dialog_prior_to_run.kv')

class Dialog_Prior_to_Run(BoxLayout):
    __events__ = ('on_canceled', 'on_success')
    
    success_string  = StringProperty('Ok')
    cancel_string   = StringProperty('Cancel')
    dialog_string   = StringProperty('Dialog String')
    arg             = ObjectProperty('None')
    
    def __init__(self, **kwargs):

        super(Dialog_Prior_to_Run, self).__init__(**kwargs)
        self.label_hints.text       = self.dialog_string
        self.button_success.text    = self.success_string
        self.button_cancel.text     = self.cancel_string
        
    def on_success(self):
        pass

    def on_canceled(self):
        pass

if __name__ == '__main__':
    
    from kivy.app import App

    class TestApp(App):

        def build(self):
            dialog = Dialog_Prior_to_Run(hints = "Dialog Text")
            
            dialog.bind(
                on_success  = self._success, 
                on_canceled = self._canceled
                )
            return dialog
        
        def _canceled(self, instance):
            import sys
            sys.exit()
        
        def _success(self, instance):
            print("test")
        
    TestApp().run()