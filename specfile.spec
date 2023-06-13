# specfile.spec

# Importiere tracker.py
import tracker

# Füge die styles.py-Datei zur Analyse hinzu
a = Analysis(['tracker.py', 'styles.py'],
             pathex=['path_to_folder'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

# Definiere die ausführbare Datei und die Optionen
exe = EXE(a,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='tracker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='path_to_icon.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='tracker')
