from ui.text import Text
from utils.observer import Observer, Publisher


class Score(Publisher):
    def __init__(self, score=0):
        super().__init__()
        self.score = score

    def up(self, change):
        self.score += change
        self.scoreChange()

    def down(self, change):
        self.score -= change
        self.scoreChange()

    def getScore(self):
        return self.score

    def scoreChange(self):
        self.notify()


class ScoreDisplayHandler(Observer):
    def __init__(self, scoreC):
        self.scoreC = scoreC
        self.scoreC.attach(self)

    def draw(self):
        self.scoreSprite = Text(text=self.getText(self.scoreC.score))
        return self.scoreSprite

    def getText(self, score):
        return "score : %s" % score

    def observeUpdate(self):
        self.scoreSprite.setText(self.getText(self.scoreC.score))


class ScoreDisplayHandler2(Observer):
    def __init__(self, scores):
        self.scores = scores
        for score in scores:
            score.attach(self)

    def draw(self):
        self.scoreSprite = Text(text=self.getText(self.scores[0].score, self.scores[1].score))
        return self.scoreSprite

    def getText(self, score1, score2):
        return "score : %s - %s " % (score1, score2)

    def observeUpdate(self):
        self.scoreSprite.setText(self.getText(self.scores[0].score, self.scores[1].score))
