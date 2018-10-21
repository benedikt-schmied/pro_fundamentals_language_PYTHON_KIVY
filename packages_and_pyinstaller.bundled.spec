# -*- mode: python -*-

import os
from os.path import join

block_cipher = None


datas = []

# list of modules to exclude from analysis
excludes = ['Tkinter', '_tkinter', 'twisted', 'pygments', 'kivy']

# list of hiddenimports
hiddenimports = []

# binary data
bin_tocs = []

# assets
assets_toc = []

tocs = bin_tocs + assets_toc

a = Analysis(['packages_and_pyinstaller\\packages_and_pyinstaller.py'],
             pathex=[],
             binaries=None,
             datas=datas,
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=excludes,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *tocs,
          name='packages_and_pyinstaller',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )


