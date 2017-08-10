from utils.setting import PLAYER1_HIGH_SCORE, INTRO, EXIT
from assembler import P1H_assembler

class AssemblerFactory:
    def __init__(self):
        pass
    def getAssembler(self, gameState, *args):
        if gameState == PLAYER1_HIGH_SCORE:
            return P1H_assembler.P1H_assembler(*args)