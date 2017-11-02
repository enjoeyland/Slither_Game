from ui.button import Button
from ui.popUp import PopUp
from ui.text import Text
from utils.setting import POS_X, POS_Y, PARENT_SIZE_WIDTH, PARENT_SIZE_HEIGHT, CENTER_MIDDLE


class WhoWinPopUp(PopUp):
    def __init__(self, pageSize=(500, 300)):
        self.pageSize = pageSize
        super().__init__(pageSize=self.pageSize, buildImageAutomatic=False)
        self.key = "score"
        self.buttonSprites = []

    def drawAdditionalContent(self, data, appendButtons=[]):
        self.allSprites = []
        text = Text(text="Player %s Win!" % (data + 1),
                    fontSize=50,
                    alignment=CENTER_MIDDLE,
                    location=(self.pageSize[POS_X]/2, self.pageSize[POS_Y]/4),
                    basePoint=self.popUpPageBasePoint)
        self.allSprites.append(text)
        for appendButton in appendButtons:
            buttonSprite = Button(appendButton["func"],
                                  buttonSize=(150, 40),
                                  text=appendButton["name"],
                                  fontSize=30,
                                  location=(self.pageSize[POS_X] if appendButton["location"][POS_X] == PARENT_SIZE_WIDTH  else appendButton["location"][POS_X],
                                            self.pageSize[POS_Y] if appendButton["location"][POS_Y] == PARENT_SIZE_HEIGHT  else appendButton["location"][POS_Y]),
                                  alignment=appendButton["alignment"],
                                  basePoint=self.popUpPageBasePoint)
            buttonSprite.listen(appendButton["listener"])
            self.allSprites.append(buttonSprite)

    def getButtonSprite(self):
        return self.buttonSprites

    def update(self):
        for sprite in self.allSprites:
            sprite.update()
            self.popUpPage.blit(sprite.image, sprite.rect)