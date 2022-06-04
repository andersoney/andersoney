from criptografia.main import run


def calcular_imposto():
    from imposto.imposto import Imposto2022, Imposto2022Proposta
    calcular = Imposto2022()
    calcular.calcular_contribuicao(salario=6000)
    calcular = Imposto2022Proposta()
    calcular.calcular_contribuicao(salario=6000)

run()