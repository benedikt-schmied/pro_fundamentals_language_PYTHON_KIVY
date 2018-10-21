#!/bin/bash

pyinstaller.exe -y packages_and_pyinstaller.none_bundled.spec
pyinstaller.exe -y packages_and_pyinstaller.bundled.spec

pyinstaller.exe -y kivy_and_pyinstaller.none_bundled.spec
pyinstaller.exe -y kivy_and_pyinstaller.bundled.spec
