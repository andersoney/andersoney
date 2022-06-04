import bitarray


class Util:
    encode = 'cp1252'

    def __init__(self):
        self.i = 0

    @staticmethod
    def convert_text_string_to_bitarray(text):
        ba = bitarray.bitarray()
        ba.frombytes(text.encode(Util.encode))
        return ba

    @staticmethod
    def convert_bitarray_to_text_string(array_bit):
        return bitarray.bitarray(array_bit).tobytes().decode(Util.encode)

    @staticmethod
    def xor(a, b):
        return a ^ b and a != b

    def f(self, key):
        ba = bitarray.bitarray()
        ba.frombytes(key.encode(Util.encode))
        self.i = self.i+1
        return ba[self.i]
