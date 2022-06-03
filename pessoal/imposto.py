class Imposto2022:
    def calcularImposto(self, salario):
        valor = 0
        if(salario > 1903.98):
            if(salario > 2826.65):
                efective = 2826.65-1903.98
            else:
                efective = salario-1903.98
                pass
            v1 = (efective)*0.075
            # print(v1)
            valor = valor+v1
            pass
        if(salario > 2826.65):
            if(salario > 3751.05):
                efective = 3751.05-2826.65
            else:
                efective = salario-2826.65
            v2 = (efective)*0.15
            # print(v2)
            valor = valor+v2
            pass
        if(salario > 3751.05):
            if(salario > 4664.68):
                efective = 4664.68-3751.05
            else:
                efective = salario-3751.05
            v3 = (efective)*0.225
            # print(v3)
            valor = valor+v3
            pass
        if(salario > 4664.68):
            v4 = (salario-4664.68)*0.275
            # print(v4)
            valor = valor+v4
            pass
        return valor

    def calcular_inss(self, salario):
        inss = 0
        if(salario > 1212):
            inss = 1212*0.075
        else:
            inss = salario*0.075
        # print(inss)
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
        # print(salario, (salario-3641.03)*0.14, salario > 3641.03)
        return inss


def calcular_contribuicao(salario):
    calculator = Imposto2022()
    inss = calculator.calcular_inss(salario)
    ir = calculator.calcularImposto(salario-inss)
    salario_liquido = salario-inss-ir
    print(f"INSS:{round(inss,2)}-Imposto de renda:{round(ir,2)}")
    print(f"Salario: {salario}-Salario Liquido:{salario_liquido}")
    return salario_liquido


if(__name__ == "__main__"):
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--salario', type=int,
                        help='Salario para calcular', default=None)
    args = parser.parse_args()
    print(args.salario);
    if(args.salario):
        print(f"\n\n\nSalario: {args.salario}\n")
        salario_liquido = calcular_contribuicao(args.salario)
    else:
        for a in range(15):
            salario = 1000+a*1000
            print(f"\n\n\nSalario: {salario}\n")
            salario_liquido = calcular_contribuicao(salario)
            if(a != 0):
                print(f"Diferença:{salario_liquido-ant_salario}")
            ant_salario = salario_liquido
