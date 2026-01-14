# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path

block_cipher = None

# Get the iopaint package path
iopaint_path = Path('iopaint')

# Collect web_app files
web_app_datas = []
web_app_path = iopaint_path / 'web_app'
if web_app_path.exists():
    for file in web_app_path.rglob('*'):
        if file.is_file():
            dest_dir = str(file.parent.relative_to(iopaint_path.parent))
            web_app_datas.append((str(file), dest_dir))

# Add batch file and README to distribution
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
        'fastapi',
        'uvicorn',
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
    strip=False,
    upx=True,
    upx_exclude=[],
    name='IOPaint',
)
