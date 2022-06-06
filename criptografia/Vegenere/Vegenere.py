class Vegenere:
    def __init__(self, alfabeto):
        self.alfabeto = alfabeto
        pass

    def convert_text_int(self, character):
        try:
            return self.alfabeto.index(character)
        except Exception:
            return -1

    def convert_int_text(self, inteiro):
        return self.alfabeto[inteiro % len(self.alfabeto)]

    def decript(self, decrit_text, chave):
        new_text = ''
        for index, character in enumerate(decrit_text):
            char_int = self.convert_text_int(character)
            char_int_vegenere = self.convert_text_int(
                chave[index % len(chave)])
            cripto_char = self.convert_int_text(
                (char_int - char_int_vegenere) % len(self.alfabeto))
            new_text += cripto_char
        return new_text

    def cript(self, text, chave):
        new_text = ''
        for index, character in enumerate(text):
            char_int = self.convert_text_int(character)
            char_int_vegenere = self.convert_text_int(
                chave[index % len(chave)])
            cripto_char = self.convert_int_text(
                (char_int + char_int_vegenere) % len(self.alfabeto))
            new_text += cripto_char
        return new_text


alfabeto = input();
chave = input();
texto = input();

vegener = Vegenere(alfabeto)
cript_text = vegener.cript(texto, chave)
print(cript_text)
decript_text = vegener.decript(cript_text, chave)
print(decript_text)
