import os, ctypes
from PIL import Image

class AppData:

    def __init__(self):
        super().__init__()
        self.__appName = 'pybing'
        basePath = os.getenv('APPDATA')
        self.__dataFolder  = os.path.join(basePath,self.__appName)
        
    
    def getAppDataFolderPath(self):
        self.iniateFolder()
        return self.__dataFolder

    def checkAppFolderExists(self):
        return os.path.isdir(self.__dataFolder)
    
    def iniateFolder(self):
        if not self.checkAppFolderExists():
            os.mkdir(self.__dataFolder)
    
    def saveImage(self, image):
        print(os.path.join(self.getAppDataFolderPath(),'wallpaper.jpeg'))
        image.save(os.path.join(self.getAppDataFolderPath(),'wallpaper.jpeg'),'JPEG')
    
    def getImagePath(self):
        return os.path.join(self.getAppDataFolderPath(),'wallpaper.jpeg')

class WindowsWallpaper:

    def __init__(self):
        super().__init__()

    def setWallpaper(self, path):
        SPI_SETDESKWALLPAPER    = 0x0014
        SPIF_UPDATEINIFILE      = 0x01
        SPIF_SENDWININICHANGE   = 0x02
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, SPIF_SENDWININICHANGE | SPIF_UPDATEINIFILE)