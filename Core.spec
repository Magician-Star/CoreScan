# CoreScan.spec

# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

project_path = '/home/gabriel/Área de trabalho/Ambiente SPYDER/CoreScan/'

a = Analysis(
    [os.path.join(project_path, 'App.py')],
    pathex=[project_path],
    binaries=[],
    datas=[
        (os.path.join(project_path, 'assets'), 'assets')
    ],
    hiddenimports=['flet'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CoreScan',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon="corescan-logo.ico"  # Você pode colocar aqui um .ico se quiser, como 'assets/icons/corescan.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CoreScan'
)
