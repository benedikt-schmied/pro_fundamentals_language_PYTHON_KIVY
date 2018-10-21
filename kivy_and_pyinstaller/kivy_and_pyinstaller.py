'''
Created on 21.10.2018

@author: KNUTH
'''

import os

import kivy
from kivy import kivy_data_dir

os.environ['KIVY_GL_BACKEND'] = 'glew'


from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()