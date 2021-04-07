import pystray, sys
from pystray import MenuItem, Menu
from PIL import Image
from bing import Bing
from windows import AppData, WindowsWallpaper

class Main:

    def __init__(self):
        super().__init__()
        self.b = Bing()
        self.appData = AppData()
        self.icon = None
    
    def run(self):
        self.createIcon()
        self.icon.run()

    def createIcon(self):
        image = self.b.getNextImage()
        self.appData.saveImage(image)
        wall = WindowsWallpaper()
        wall.setWallpaper(self.appData.getImagePath())
        image = Image.open("icon.png")
        menu = Menu(MenuItem('Next Image', self.nextI),
                    MenuItem('Prev Image', self.prevI),
                    MenuItem('Quit', self.quitI))
        self.icon = pystray.Icon("pyBing v0.1", image, "pyBing v0.1", menu)

    def nextI(self):    
        image = self.b.getNextImage()
        self.appData.saveImage(image)
        wall = WindowsWallpaper()
        wall.setWallpaper(self.appData.getImagePath())

    def prevI(self):
        image = self.b.getPreviousImage()
        self.appData.saveImage(image)
        wall = WindowsWallpaper()
        wall.setWallpaper(self.appData.getImagePath())

    def quitI(self):
        print('Exit')
        self.icon.stop()
        pass

if __name__ == "__main__":
    main = Main()
    main.run()
