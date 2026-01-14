# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Explicitly add web_app files
added_files = [
    ('iopaint/web_app/index.html', 'iopaint/web_app'),
    ('iopaint/web_app/favicon.ico', 'iopaint/web_app'),
    ('iopaint/web_app/assets', 'iopaint/web_app/assets'),
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
        'iopaint.runtime',
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
        'torchvision',
        'safetensors',
        'diffusers',
        'transformers',
        'accelerate',
        'omegaconf',
        'starlette.staticfiles',
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
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='IOPaint',
)
