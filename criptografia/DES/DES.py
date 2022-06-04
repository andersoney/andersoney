from .util import Util


class DESProcess:
    def __init__(self, chave):
        self.chave = Util.convert_text_string_to_bitarray(chave)
        self.rotor = 0
        self.i = 0
        pass

    def criptografia(self, text: str, num_round=16) -> str:
        bitArray = Util.convert_text_string_to_bitarray(text)
        for a in range(num_round):
            bitArray = self.round(bitArray)
            # print(f"Round1:{bitArray}")
        text = Util.convert_bitarray_to_text_string(bitArray)
        return text

    def round(self, bitArray):
        meio = int(len(bitArray)/2)
        for a, _ in enumerate(range(meio)):
            aux = bitArray[a]
            fValue = self.f()
            bitArray[a] = Util.xor(fValue, bitArray[meio+a])
            bitArray[meio+a] = aux
        return bitArray

    def f(self):
        response = self.chave[(self.i+self.rotor) % len(self.chave)]
        self.i = self.i+1
        self.rotor = self.rotor+1
        return response
