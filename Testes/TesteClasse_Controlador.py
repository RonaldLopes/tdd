import unittest
from Controller.Classe_Posicionamento import Classe_Posicionamento
from should_dsl import should, should_not

from Controller.Classe_Controlador import *


class TesteClasse_Controlador(unittest.TestCase):

    def teste_detectar_objetos(self):
        pass
    def teste_tipo_retorno_solicita_dados_serial(self):
        obj_Controlador = Classe_Controlador()
        dados_serial = obj_Controlador.solicita_dados_serial()
        dados_serial |should| be_kind_of(list)
        for dado in dados_serial:
            dado |should| be_kind_of(dict)
    def teste_solicita_dados_posicionamento(self):
        obj_posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0, 'tempo': 0.2},
                        {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0, 'tempo': 0.02},
                        {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0, 'tempo': 0.03}]

        dados_posicionamento = obj_posicionamento.calcular_posicionamento(dados_brutos=dados_brutos)
        print(dados_posicionamento)
        # for dado in dados_posicionamento:
        #     dado |should| include_keys('OBJ', '')
    def teste_processa_objs_e_coordenadas(self):
        pass