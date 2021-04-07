import requests, json
from PIL import Image
from io import BytesIO

class Bing:

    def __init__(self):
        super().__init__()
        self.__count = 0
        self.__urlBase = "https://www.bing.com"
        self.__urlMeta = "/HPImageArchive.aspx?format=js&n=1&mkt=en-US&idx="
        
    # Private Methods

    def __getMetaUrl(self):
        return self.__urlBase + self.__urlMeta + str(self.__count)

    def __getImageUrl(self, url):
        return self.__urlBase + url

    # Public Methods

    def getImage(self):
        rMeta = requests.get(self.__getMetaUrl())
        if rMeta.status_code == 200:
            meta = rMeta.json()
            print(meta['images'][0]['url'])
            rImage = requests.get(self.__getImageUrl(meta['images'][0]['url']))
            if rImage.status_code == 200:
                image = Image.open(BytesIO(rImage.content))
                return image
        return None

    def getNextImage(self):
        self.__count += 1
        image = self.getImage()
        if image == None: 
            self.__count -= 1
        return image

    def getPreviousImage(self):
        if self.__count != 0:
            self.__count -= 1
        image = self.getImage()
        if image == None: 
            self.__count += 1
        return image