class Imposto2022:
    def __init__(self):
        print(f"{self.__class__.__name__}")

    def calcularImposto(self, salario):
        valor = 0
        if(salario > 1903.98):
            if(salario > 2826.65):
                efective = 2826.65-1903.98
            else:
                efective = salario-1903.98
            valor = valor+(efective)*0.075
        if(salario > 2826.65):
            if(salario > 3751.05):
                efective = 3751.05-2826.65
            else:
                efective = salario-2826.65
            valor = valor+(efective)*0.15
        if(salario > 3751.05):
            if(salario > 4664.68):
                efective = 4664.68-3751.05
            else:
                efective = salario-3751.05
            valor = valor+(efective)*0.225
        if(salario > 4664.68):
            valor = valor+(salario-4664.68)*0.275
        return valor

    def calcular_inss(self, salario):
        inss = 0
        if(salario > 1212):
            inss = 1212*0.075
        else:
            inss = salario*0.075
        if(salario > 1212):
            if(salario > 2427.35):
                inss = inss+(2427.35-1212)*0.09
            else:
                efective = salario-1212
                inss = inss+efective*0.09
        if(salario > 2427.35):
            if(salario > 3641.03):
                inss = inss+(3641.03-2427.35)*0.12
            else:
                efective = salario-2427.35
                inss = inss+efective*0.12
        if(salario > 3641.03):
            if(salario < 7087.22):
                efective = salario-3641.03
                inss = inss+efective*0.14
            else:
                inss = inss+(7087.22-3641.03)*0.14
        return inss

    def calcular_contribuicao(self, salario, proposta=False):
        inss = self.calcular_inss(salario)
        ir = self.calcularImposto(salario-inss)
        salario_liquido = salario-inss-ir
        print(f"INSS:{round(inss,2)}-Imposto de renda:{round(ir,2)}")
        print(f"Salario: {salario}-Salario Liquido:{salario_liquido}")
        return salario_liquido


class Imposto2022Proposta(Imposto2022):
    def calcularImposto(self, salario):
        valor = 0
        if(salario > 2500):
            if(salario > 3200):
                efective = 3200-2500
            else:
                efective = salario-2500
            valor = valor+(efective)*0.075
        if(salario > 3200):
            if(salario > 4250):
                efective = 4250-3200
            else:
                efective = salario-3200
            valor = valor+(efective)*0.15
        if(salario > 4250):
            if(salario > 5300):
                efective = 5300-4250
            else:
                efective = salario-4250
            valor = valor+(efective)*0.225
        if(salario > 5300):
            valor = valor+(salario-4664.68)*0.275
        return valor


if(__name__ == "__main__"):
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--salario', type=int,
                        help='Salario para calcular', default=None)
    parser.add_argument('--proposta', type=bool,
                        help='Calcular com proposta 2022', default=False)
    args = parser.parse_args()
    print(args.proposta)
    calculator = Imposto2022Proposta()
    if(args.salario):
        print(f"\n\n\nSalario: {args.salario}\n")
        salario_liquido = calculator.calcular_contribuicao(
            args.salario, args.proposta)
    else:
        for a in range(9):
            salario = 1000+a*1000
            print(f"\n\n\nSalario: {salario}\n")
            salario_liquido = calculator.calcular_contribuicao(
                salario, args.proposta)
            if(a != 0):
                print(f"Diferença:{salario_liquido-ant_salario}")
            ant_salario = salario_liquido
