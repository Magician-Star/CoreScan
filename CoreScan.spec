# CoreScan.spec

# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Caminho base do projeto
project_path = os.path.abspath('.')

# Coleta todos os arquivos de imagem da pasta assets (recursivamente)
data_files = collect_data_files(
    os.path.join(project_path, 'assets'),
    includes=['*.png', '*.ico', '*.jpg'],
    subdir='assets'
)

a = Analysis(
    [os.path.join(project_path, 'app', 'App.py')],
    pathex=[project_path],
    binaries=[],
    datas=data_files,
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
    icon=os.path.join('assets', 'icons', 'corescan-logo.ico')  # Só afeta builds no Windows
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
