# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path
from PyInstaller.building.datastruct import Tree

block_cipher = None

# Collect web_app files using Tree for entire directory
web_app_tree = Tree('iopaint/web_app', prefix='iopaint/web_app', excludes=[])

# Additional data files
added_files = [
    ('run_iopaint.bat', '.'),
    ('CLIENT_README.txt', '.'),
]

a = Analysis(
    ['iopaint/__main__.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        'iopaint',
        'iopaint.cli',
        'iopaint.api',
        'iopaint.model',
        'iopaint.model.lama',
        'iopaint.model_manager',
        'iopaint.schema',
        'iopaint.const',
        'iopaint.download',
        'iopaint.file_manager',
        'iopaint.helper',
        'fastapi',
        'uvicorn',
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        'pydantic',
        'PIL',
        'cv2',
        'torch',
        'numpy',
        'typer',
        'loguru',
        'yacs',
        'torch',
        'torchvision',
        'safetensors',
        'diffusers',
        'transformers',
        'accelerate',
        'omegaconf',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'tkinter',
        'PyQt5',
        'PyQt6',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='IOPaint',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Set to False to hide console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add .ico file path here if you have one
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    web_app_tree,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='IOPaint',
)
