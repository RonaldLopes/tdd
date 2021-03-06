import unittest

from should_dsl import should

from Controller.Classe_Comunicacao import *



class Teste_Comunicacao(unittest.TestCase):


    def teste_ler_serial_tipo_saida(self):
        s = Classe_Comunicacao()
        leitura =  s.ler_serial()
        leitura |should| be_kind_of(str)

    def teste_ler_serial_verifica_integridade(self):
        s = Classe_Comunicacao()
        leitura =  s.ler_serial()
        leitura |should| be_like(r'^ID:[123]+,angulo:[0-9]+.[0-9]+,temperatura:[0-9]+.[0-9]+,tempo:[0-9]+.[0-9]+[|]ID:[123]+,angulo:[0-9]+.[0-9]+,temperatura:[0-9]+.[0-9]+,tempo:[0-9]+.[0-9]+[|]ID:[123]+,angulo:[0-9]+.[0-9]+,temperatura:[0-9]+.[0-9]+,tempo:[0-9]+.[0-9]+$')

    def teste_formatar_pacote(self):
        s = Classe_Comunicacao()
        pacote = s.formatar_pacote(s.ler_serial())
        pacote |should| be_kind_of(list)

        for dicionario in pacote:
            dicionario |should| be_kind_of(dict)

    def teste_obter_brutos(self):
        s = Classe_Comunicacao()
        retorno = s.obter_dados_brutos()
        retorno |should| be_kind_of(list)