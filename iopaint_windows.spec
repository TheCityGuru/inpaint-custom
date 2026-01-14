# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

block_cipher = None

# Collect all web_app files individually
web_app_datas = []
web_app_path = Path('iopaint/web_app')
for file in web_app_path.rglob('*'):
    if file.is_file():
        # Destination should maintain the iopaint/web_app structure
        relative_path = file.relative_to('iopaint')
        dest_folder = str(Path('iopaint') / relative_path.parent)
        web_app_datas.append((str(file), dest_folder))

# Add batch file and README to root
web_app_datas.append(('run_iopaint.bat', '.'))
web_app_datas.append(('CLIENT_README.txt', '.'))

a = Analysis(
    ['iopaint/__main__.py'],
    pathex=[],
    binaries=[],
    datas=web_app_datas,
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
