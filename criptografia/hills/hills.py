import random
from scipy import linalg
import numpy as np
import scipy
# from mypackage.hill import Hill


class Hill:
    def find_multiplicative_inverse(self, determinant, len_alfabeto):
        print(f"DETERMINANTE: {determinant}")
        for i in range(len_alfabeto):
            inverse = determinant * i
            if int(round(inverse % len_alfabeto, 1)) == 1:
                print(
                    f"multiplicative_inverse:{i}\tlen_alfabeto:{len_alfabeto}")
                return i
        raise Exception("Não encontrado inverse multiplicative")

    def matrix_cofactor(self, matrix):
        try:
            determinant = np.linalg.det(matrix)
            if(determinant != 0):
                cofactor = None
                cofactor = np.linalg.inv(matrix).T * determinant
                # return cofactor matrix of the given matrix
                return cofactor
            else:
                raise Exception("singular matrix")
        except Exception as e:
            print("could not find cofactor matrix due to", e)

    def get_inverse(self, matriz, len_alfabeto):
        return matriz.I

    def mult_matrix(self, matriz1, matriz2, len_alfabeto):
        return matriz1 * matriz2 % len_alfabeto

    def normalize_text(self, text, len_matriz):
        len_text = len(text)
        resto = len_text % len_matriz
        if(resto != 0):
            for _ in range(len_matriz-resto):
                text = text+'o'
            pass
        else:
            pass
        # print(text)
        len_text = len(text)
        return text, len_text

    def one_matriz_convert(self, lenx, leny, alfabeto, text):
        arrays = []
        for _ in range(lenx):
            row = []
            for _ in range(leny):
                # print(text[0],alfabeto.index(text[0]));
                row.append(alfabeto.index(text[0]))
                text = text[1:]
                # print(text);
                pass
            arrays.append(row)
        local_matriz = np.array(arrays, dtype=np.float64)
        return local_matriz, text

    def convert_text_to_matrizes(self, text, shape, alfabeto):
        len_matriz = shape[0]*shape[1]
        text, len_text = self.normalize_text(text, len_matriz)
        num_natrizes = int(len_text/len_matriz)
        # print(num_natrizes)

        matrizes = []
        for _ in range(num_natrizes):
            local_matriz, text = self.one_matriz_convert(
                shape[0], shape[1], alfabeto, text)
            matrizes.append(local_matriz)
            pass
        # print(text)
        # print(matrizes)
        return matrizes

    def convert_matriz_to_text(self, matriz, alfabeto):
        text = ''
        for row in matriz.A:
            for col in row:
                text += alfabeto[int(col % len(alfabeto))]
        return text

    def encript(self, text, matriz, alfabeto):
        len_alfabeto = len(alfabeto)
        matrizes = self.convert_text_to_matrizes(text, matriz.shape, alfabeto)
        matriz_cripto = []
        for matriz_text in matrizes:
            cripto = matriz_text * matriz
            matriz_cripto.append(cripto)
        cripto_text = ''
        for matriz_c in matriz_cripto:
            cripto_text += self.convert_matriz_to_text(matriz_c, alfabeto)
        return cripto_text

    def matrix_cofactor(self, matrix):
        return np.linalg.inv(matrix) * np.linalg.det(matrix)

    def get_adjungate_matrix(self, matriz, determinant):
        x = matriz.A
        c = [[i for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                c[i][j] = (-1)*(i+j)*determinant

    def decript(self, cripto_text, matriz, alfabeto):
        print(cripto_text)
        cripto_text="syi"
        len_alfabeto = len(alfabeto)
        determinant = int(round(np.linalg.det(matriz), 1)) % len_alfabeto
        multiplicative_inverse = self.find_multiplicative_inverse(
            determinant, len_alfabeto)
        matriz_inv = np.conj(matriz).T
        cofactor = self.matrix_cofactor(
            matriz) % len_alfabeto
        invert_key_matrix = cofactor*multiplicative_inverse%len_alfabeto
        print(
            f"det:{determinant}\tinverse:{multiplicative_inverse}\tinv:{invert_key_matrix}\ncofactor:\n{cofactor}")
        matriz_inv = matriz_inv*multiplicative_inverse
        matrizes_cript = self.convert_text_to_matrizes(
            cripto_text, matriz.shape, alfabeto)
        matriz_decripto = []
        for matriz_text in matrizes_cript:
            decripto = self.mult_matrix(matriz_text, invert_key_matrix, len_alfabeto)
            matriz_decripto.append(decripto)
        decripto_text = ''
        for matriz_d in matriz_decripto:
            decripto_text += self.convert_matriz_to_text(matriz_d, alfabeto)
        return decripto_text


def testando_fatores_iniciais(alfabeto):
    hill = Hill()
    len_alfabeto = len(alfabeto)
    matriz2 = np.array([[2,  2], [14, 26]], dtype=np.float64)
    # print(f"Testando fatores Iniciais\n {'_'*100}")
    matriz = np.array([[9, 4], [5, 7]], dtype=np.float64)
    print(f"matriz: \n{matriz}")
    matriz_inv = hill.get_inverse(matriz, len(alfabeto))
    print(f"Inversa:\n{matriz_inv}")
    print(
        f"Matriz e Inversa: \n{hill.mult_matrix(matriz, matriz_inv, len_alfabeto)}")
    print(f"Testando criptografia e decriptografia\n{'&'*100}")
    print(matriz2)
    cripto = hill.mult_matrix(matriz2, matriz, len_alfabeto)
    print(cripto)
    decripto = hill.mult_matrix(cripto, matriz_inv, len_alfabeto)
    print(decripto)
    return matriz_inv


hill = Hill()
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
# matriz_inv = testando_fatores_iniciais(alfabeto)
# exit()

if(__name__ == '__main__'):
    matriz = np.matrix([[1,  0, 2],
                       [10,  20, 15],
                       [0, 1, 2]], dtype=np.float64)
    chave = 'cabababababasdaba'
    # matriz,text = hill.one_matriz_convert(3,3,alfabeto,chave)
    # matriz = np.array([[9, 4], [5, 7]], dtype=np.float64)
    # print(f"Chave:\n{matriz}\tlen_alfabeto:{len(alfabeto)}")
    # text = "totestando nao me enche ze!\\\\\\\'\"".lower()
    text = input()
    text = text.replace(' ', '')
    text="ret"
    print(f"PLAIN_TEXT: {text}")
    cripto_text = hill.encript(text, matriz, alfabeto)
    matriz_inv = hill.get_inverse(matriz, len(alfabeto))
    print(f"CRIPTED_TEXT: {cripto_text}")
    cripto_text ="syi"
    matriz = np.matrix([[0,  11, 15],
                       [7,  0, 1],
                       [4, 19, 0]], dtype=np.float64)
    print(f"Decriptando:")
    decripto_text = hill.decript(cripto_text, matriz, alfabeto)
    print(decripto_text)


pass
