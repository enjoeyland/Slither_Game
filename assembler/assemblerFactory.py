from assembler.P1H_assembler import P1H_assembler
from assembler.P2C_assembler import P2C_assembler
from utils.setting import PLAYER1_HIGH_SCORE, PLAYER2_COMPETE

class AssemblerFactory:
    def __init__(self):
        pass
    def getAssembler(self, gameState, *args):
        if gameState == PLAYER1_HIGH_SCORE:
            return P1H_assembler(*args)
        elif gameState == PLAYER2_COMPETE:
            return P2C_assembler(*args)
