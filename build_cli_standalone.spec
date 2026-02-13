# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec file for L-ZIP CLI-only executable (no GUI)

a = Analysis(
    ['cli_noui.py'],
    pathex=['D:\\Dev\\L-ZIP'],
    binaries=[],
    datas=[('D:\\Dev\\L-ZIP\\lzip.py', '.'),
            ('D:\\Dev\\L-ZIP\\mcp_server.py', '.'),
            ('D:\\Dev\\L-ZIP\\lzip_extended_operators.py', '.')],
    hiddenimports=['lzip', 'mcp_server'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=['gui', 'customtkinter', 'darkdetect', 'tkinter', '_tkinter', 'PIL', 'pillow', 'Pillow', 'ctk_debug', 'customtkinter._core', 'customtkinter._gui_core'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='lzip-cli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=['vcruntime140.dll'],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='D:\\Dev\\L-ZIP\\images\\L-ZIP-logo.ico',
)
