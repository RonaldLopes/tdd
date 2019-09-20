from Testes.serial import Serial


class Classe_Comunicacao:
    def __init__(self, porta = '', baudrate = 9600):
        self.porta = porta
        self.baudrate = baudrate

    def obter_dados_brutos(self):
        dados_brutos = self.ler_serial()
        dados_pre_processados = self.formatar_pacote(dados_brutos)
        return dados_pre_processados

    def ler_serial(self):
        s = Serial(self.porta, self.baudrate)
        return s.read()

    def formatar_pacote(self, dados_brutos):
        dicionario =[]
        for elemento in dados_brutos.split("|"):
            dicionario_temporario= {}
            for dado in elemento.split(","):
                temporario = dado.split(":")
                dicionario_temporario[str(temporario[0])] = float(temporario[1])
            dicionario.append(dicionario_temporario)
        return dicionario

# temp = Classe_Comunicacao()
# print(temp.obter_dados_brutos())