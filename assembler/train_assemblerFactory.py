from utils.setting import PLAYER1_HIGH_SCORE, INTRO, EXIT
from assembler import train_P1H_assembler

class TrainAssemblerFactory:
    def __init__(self):
        pass
    def getAssembler(self, gameState, *args):
        if gameState == PLAYER1_HIGH_SCORE:
            return train_P1H_assembler.TrainP1H_assembler(*args)
