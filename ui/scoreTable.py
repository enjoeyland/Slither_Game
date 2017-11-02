from ui.button import Button
from ui.popUp import PopUp
from ui.text import Text
from utils.setting import TOP_MIDDLE, SCREEN_WIDTH, POS_X, POS_Y, RED, BLUE, BOTTOM_LEFT, PARENT_SIZE_WIDTH, \
    PARENT_SIZE_HEIGHT


class DrawTable():
    def draw(self, data, key, basePoint=(0, 0), width=SCREEN_WIDTH, highLight=None):
        textSpriteList = []
        fontSize = 20
        margin = fontSize + 10
        one = True
        for index, datum in enumerate(data):
            if datum[key] == highLight and one == True:
                textSpriteList.append(Text(color=RED, text="%s. %s" % (index + 1, datum[key]), fontSize=20,
                                           location=(basePoint[POS_X] + width / 2, basePoint[POS_Y] + margin * index),
                                           alignment=TOP_MIDDLE))
                one = False
            else:
                textSpriteList.append(Text(text="%s. %s" % (index + 1, datum[key]), fontSize=20,
                                           location=(basePoint[POS_X] + width / 2, basePoint[POS_Y] + margin * index),
                                           alignment=TOP_MIDDLE))
        return textSpriteList


class ScoreTable(PopUp):
    def __init__(self, pageSize=(500, 300)):
        self.pageSize = pageSize
        super().__init__(pageSize=self.pageSize, buildImageAutomatic=False)
        self.key = "score"
        self.buttonSprites = []

    def drawAdditionalContent(self, data, thisSessionScore, appendButtons=[]):
        self.allSprites = []
        scoreSprites = DrawTable().draw(data, self.key, width=self.pageSize[POS_X], highLight=thisSessionScore)
        self.allSprites.extend(scoreSprites)

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
            self.buttonSprites.append(buttonSprite)

    def getButtonSprite(self):
        return self.buttonSprites

    def update(self):
        for sprite in self.allSprites:
            sprite.update()
            self.popUpPage.blit(sprite.image, sprite.rect)
        for buttonSprite in self.buttonSprites:
            buttonSprite.update()
            self.popUpPage.blit(buttonSprite.image, buttonSprite.rect)
