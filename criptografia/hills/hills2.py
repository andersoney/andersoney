import numpy as np
import scipy



class Hill:
    def __init__(self, matriz: np.matrix, alfabeto:str):
        self.matriz = matriz
        self.len_alfabeto = len(alfabeto)
        print(self.len_alfabeto)
        self.alfabeto = alfabeto
        self.check_key();

    def encript(self, text:str)->str:
        matrizes = []
        while(len(text) > 0):
            matriz = []
            for _ in range(self.matriz.shape[0]):
                if text == "":
                    matriz.append(self.alfabeto.index('a'))
                    continue
                matriz.append(self.alfabeto.index(text[0]))
                text = text[1:]
            matriz = np.matrix(matriz)
            matrizes.append(matriz)
        matriz_cripted = []
        for matriz in matrizes:
            matriz_cripted.append(self.matriz*matriz.T % self.len_alfabeto)
        cripted_text = ''
        for matriz in matriz_cripted:
            for chaaa in matriz.getA():
                cripted_text += self.alfabeto[int(chaaa)]
        return cripted_text

    def find_multiplicative_inverse(self, determinant:float, len_alfabeto:int)->int:
        for i in range(len_alfabeto):
            inverse = determinant * i
            if int(round(inverse % len_alfabeto, 1)) == 1:
                return i
        raise Exception("Não encontrado inverse multiplicative")

    def matrix_cofactor(self, matrix: np.matrix) -> np.matrix:
        try:
            determinant = np.linalg.det(matrix)
            if(determinant != 0):
                cofactor = None
                cofactor = np.linalg.inv(matrix).T * determinant
                return cofactor
            else:
                raise Exception("singular matrix")
        except Exception as e:
            print("could not find cofactor matrix due to", e)
    def check_key(self):
        determinant = int(round(np.linalg.det(self.matriz), 1)
                          ) % self.len_alfabeto
        multiplicative_inverse = self.find_multiplicative_inverse(
            determinant, self.len_alfabeto)
        cofactor = self.matrix_cofactor(
            self.matriz).T % self.len_alfabeto
    def dencript(self, text: str)->str:
        determinant = int(round(np.linalg.det(self.matriz), 1)
                          ) % self.len_alfabeto
        multiplicative_inverse = self.find_multiplicative_inverse(
            determinant, self.len_alfabeto)
        cofactor = self.matrix_cofactor(
            self.matriz).T % self.len_alfabeto
        invert_key_matrix = cofactor*multiplicative_inverse % self.len_alfabeto

        matrizes = []
        while(len(text) > 0):
            matriz = []
            for _ in range(self.matriz.shape[0]):
                if text == None:
                    matriz.append(self.alfabeto.index('a'))
                    continue
                matriz.append(self.alfabeto.index(text[0]))
                text = text[1:]
                pass
            matriz = np.matrix(matriz)
            matrizes.append(matriz)
        matriz_cripted = []
        for matriz in matrizes:
            matriz_cripted.append(
                invert_key_matrix*matriz.T)
        cripted_text = ''
        for matriz in matriz_cripted:
            for chaaa in matriz.getA():
                index = round(chaaa[0], 1) % self.len_alfabeto
                index = int(index)
                cripted_text += self.alfabeto[index]
        return cripted_text

    @staticmethod
    def make_key(alfabeto: str, key: str) -> np.matrix:
        key_matrix = []
        len_matriz = int(len(key)**(1/2))
        for _ in range(len_matriz):
            row_key_matriz = []
            for _ in range(len_matriz):
                row_key_matriz.append(alfabeto.index(key[0]))
                key = key[1:]
            key_matrix.append(row_key_matriz)
        return np.matrix(key_matrix)


def test1(alfabeto):
    matriz = np.matrix([[1,  0, 2],
                       [10,  20, 15],
                       [0, 1, 2]], dtype=np.float64)
    print(Hill(matriz, alfabeto).encript('ret'))

    matriz = np.matrix([[0,  11, 15],
                       [7,  0, 1],
                       [4, 19, 0]], dtype=np.float64)
    print(Hill(matriz, alfabeto).dencript('syi'))

def main():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz! '
    key=input();
    matriz = Hill.make_key(alfabeto, 'aadqrs qkls')
    # matriz = Hill.make_key(alfabeto, key)
    print(matriz)
    cripted_text = Hill(matriz, alfabeto).encript('testandocapacidadedocodigo')
    print(cripted_text)
    decripted_text = Hill(matriz, alfabeto).dencript(cripted_text)
    print(decripted_text)
    pass


if __name__ == '__main__':
    main()
