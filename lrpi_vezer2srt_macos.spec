# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['lrpi_vezer2srt.py'],
             pathex=[],
             binaries=[],
             datas=[('/Users/francesco.anselmo/Documents/Code/Python/venv/py39/lib/python3.9/site-packages/pyfiglet/fonts', './pyfiglet/fonts')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='lrpi_vezer2srt_macos',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
