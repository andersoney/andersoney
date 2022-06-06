from criptografia.main import run


def calcular_imposto():
    from imposto.imposto import Imposto2022, Imposto2022Proposta
    calcular = Imposto2022()
    calcular.calcular_contribuicao(salario=6000)
    calcular = Imposto2022Proposta()
    calcular.calcular_contribuicao(salario=6000)


def main():
    imposto = False
    if (imposto):
        salarioAntigo1 = None
        salario_antigo2 = None
        for a in range(10):
            from imposto.imposto import Imposto2022, Imposto2022Proposta
            calcular = Imposto2022()
            salario_novo1 = calcular.calcular_contribuicao(salario=6000+1000*a)
            if(salarioAntigo1):
                print(f"Proposta antiga: {salario_novo1-salarioAntigo1}")
            salarioAntigo1 = salario_novo1

            calcular = Imposto2022Proposta()
            salario_novo2 = calcular.calcular_contribuicao(salario=6000+1000*a)
            if(salario_antigo2):
                print(f"Proposta nova: {salario_novo2-salario_antigo2}")
            salario_antigo2 = salario_novo2

    else:
        run()


if(__name__ == '__main__'):
    main()
