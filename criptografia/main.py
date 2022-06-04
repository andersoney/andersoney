from .DES.DES import DESProcess
from .DES.util import Util
import random
seed = 10
random.seed(10)

global i
i = 0


def aa(num_round):
    print(f"Number of rounds :{num_round}")
    chave = "ChaveDeTesteasdasadasd1asdlkajs99293182312asdasds"
    texto = "Bom dia, testando com textos grandes para garantir que o processo funciona"
    # print(chave)
    random.seed(10)
    process = DESProcess(chave)
    cript = process.criptografia(texto, num_round=num_round)
    print(f"cripto:{cript}")
    random.seed(10)
    process = DESProcess(chave)
    decript = process.criptografia(cript, num_round=num_round)
    print(f"decript:{decript}")
    pass


def run():
    for a in range(40):
        aa(a*2+2)
        pass
