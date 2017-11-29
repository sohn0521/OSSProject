# -*- mode: python -*-

block_cipher = None

a = Analysis(['__main__.py'],
             pathex=['/Users/KimSungsoo/PycharmProjects/OSSProject'],
             binaries=[],
             datas=[ ('images/*.png', 'images') ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ytdl.exe',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='ytdl.app',
             icon=None,
             bundle_identifier=None,
             info_plist={
                'NSHighResolutionCapable': 'True'
             },)
