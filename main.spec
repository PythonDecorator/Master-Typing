# -*- mode: python -*-
a = Analysis(['main.py'],
         pathex=['C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App'],
         datas=[('C:\\Users\\XPS\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\customtkinter', 'customtkinter/'), ('C:\\Users\\XPS\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\wonderwords', 'wonderwords/')],
         hiddenimports=["wonderwords"],
         hookspath=None,
         runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('files\\logo\\logo\\1.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\1.png', 'DATA'), ('files\\logo\\logo\\2.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\2.png', 'DATA'), ('files\\logo\\logo\\3.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\3.png', 'DATA'), ('files\\logo\\logo\\4.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\4.png', 'DATA'), ('files\\logo\\logo\\5.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\5.png', 'DATA'), ('files\\logo\\logo\\6.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\6.png', 'DATA'), ('files\\logo\\logo\\7.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\7.png', 'DATA'), ('files\\logo\\logo\\8.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\8.png', 'DATA'), ('files\\logo\\logo\\9.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\9.png', 'DATA'), ('files\\logo\\logo\\10.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\10.png', 'DATA'), ('files\\logo\\logo\\11.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\11.png', 'DATA'), ('files\\logo\\logo\\12.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\12.png', 'DATA'), ('files\\logo\\logo\\13.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\13.png', 'DATA'), ('files\\logo\\logo\\14.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\14.png', 'DATA'), ('files\\logo\\logo\\15.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\15.png', 'DATA'), ('files\\logo\\logo\\16.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\16.png', 'DATA'), ('files\\logo\\logo\\17.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\17.png', 'DATA'), ('files\\logo\\logo\\18.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\18.png', 'DATA'), ('files\\logo\\logo\\19.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\19.png', 'DATA'), ('files\\logo\\logo\\20.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\20.png', 'DATA'), ('files\\logo\\logo\\21.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\21.png', 'DATA'), ('files\\logo\\logo\\22.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\22.png', 'DATA'), ('files\\logo\\logo\\23.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\23.png', 'DATA'), ('files\\logo\\logo\\24.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\24.png', 'DATA'), ('files\\logo\\logo\\25.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\25.png', 'DATA'), ('files\\logo\\logo\\26.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\26.png', 'DATA'), ('files\\logo\\logo\\27.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\27.png', 'DATA'), ('files\\logo\\logo\\28.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\28.png', 'DATA'), ('files\\logo\\logo\\29.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\29.png', 'DATA'), ('files\\logo\\logo\\30.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\30.png', 'DATA'), ('files\\logo\\logo\\31.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\31.png', 'DATA'), ('files\\logo\\logo\\32.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\32.png', 'DATA'), ('files\\logo\\logo\\33.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\33.png', 'DATA'), ('files\\logo\\logo\\34.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\34.png', 'DATA'), ('files\\logo\\logo\\35.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\35.png', 'DATA'), ('files\\logo\\logo\\36.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\36.png', 'DATA'), ('files\\logo\\logo\\37.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\37.png', 'DATA'), ('files\\logo\\logo\\38.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\38.png', 'DATA'), ('files\\logo\\logo\\39.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\39.png', 'DATA'), ('files\\logo\\logo\\40.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\40.png', 'DATA'), ('files\\logo\\logo\\41.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\41.png', 'DATA'), ('files\\logo\\logo\\42.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\42.png', 'DATA'), ('files\\logo\\logo\\43.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\43.png', 'DATA'), ('files\\logo\\logo\\44.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\44.png', 'DATA'), ('files\\logo\\logo\\45.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\45.png', 'DATA'), ('files\\logo\\logo\\46.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\46.png', 'DATA'), ('files\\logo\\logo\\47.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\47.png', 'DATA'), ('files\\logo\\logo\\48.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\48.png', 'DATA'), ('files\\logo\\logo\\49.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\49.png', 'DATA'), ('files\\logo\\logo\\50.png', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\logo\\logo\\50.png', 'DATA'), ('files\\sound\\not_started.mp3', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\sound\\not_started.mp3', 'DATA'), ('files\\sound\\sound effect.mp3', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\sound\\sound effect.mp3', 'DATA'), ('files\\sound\\typing.mp3', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\sound\\typing.mp3', 'DATA'), ('files\\images\\logo.ico', 'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Typing Speed App\\files\\images\\logo.ico', 'DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='Master-Typing.exe',
      debug=False,
      strip=None,
      upx=True,
      console=False,
      icon='C:\\Users\\XPS\Desktop\\Pro Portfolio\\Typing Speed App\\files\\images\\logo.ico')