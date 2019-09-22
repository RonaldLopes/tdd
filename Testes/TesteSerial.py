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
        leitura |should| be_like(r'^ID:[123]+,angulo:[0-9]+.[0-9]+,temp:[0-9]+.[0-9]+[|]ID:[123]+,angulo:[0-9]+.[0-9]+,temp:[0-9]+.[0-9]+[|]ID:[123]+,angulo:[0-9]+.[0-9]+,temp:[0-9]+.[0-9]+$')

    def teste_formatar_pacote(self):
        pass

    def teste_obter_brutos(self):
        pass