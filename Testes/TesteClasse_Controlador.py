import unittest
from Controller.Classe_Posicionamento import Classe_Posicionamento
from should_dsl import should, should_not

from Controller.Classe_Controlador import *


class TesteClasse_Controlador(unittest.TestCase):

    def teste_detectar_objetos(self):
        '''Adimitindo que a saída do serial será "ID:1,angulo:45.0,temperatura:25.0,tempo:233.0|ID:2,angulo:60.0,temperatura:30.0,tempo:233.0|ID:3,angulo:30.0,temperatura:33.0,tempo:233.0"'''
        obj_controlador = Classe_Controlador(distanciaS1_S2=45.0, distanciaS2_S3=30.0)
        resultado = obj_controlador.detectar_objetos()
        resultado | should | equal_to([{'x': 28526.3204, 'y': 28526.3204, 'OBJ': 'a'}, {'x': 35229.1986, 'y': -20294.5873, 'OBJ': 'b'}, {'x': -35373.0852, 'y': -20394.9808, 'OBJ': 'c'}])
    def teste_tipo_retorno_solicita_dados_serial(self):
        obj_Controlador = Classe_Controlador()
        dados_serial = obj_Controlador.solicita_dados_serial()
        dados_serial |should| be_kind_of(list)
        for dado in dados_serial:
            dado |should| be_kind_of(dict)
    def teste_solicita_dados_posicionamento(self):
        obj_controlador = Classe_Controlador(distanciaS1_S2=45.0, distanciaS2_S3=30.0)
        dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0, 'tempo': 0.2},
                        {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0, 'tempo': 0.02},
                        {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0, 'tempo': 0.03}]

        dados_posicionamento = obj_controlador.solicita_dados_posicionamento(dados_brutos=dados_brutos)
        dados_posicionamento  | should | equal_to([{'x': 24.4861, 'y': 24.4861}, {'x': 3.024, 'y': 43.2541}, {'x': 25.4417, 'y': 42.3682}])
    def teste_processa_objs_e_coordenadas(self):
        obj_controlador = Classe_Controlador(distanciaS1_S2=45.0, distanciaS2_S3=30.0)
        coordenadas = [{'x': 24.4861, 'y': 24.4861}, {'x': 3.024, 'y': 43.2541}, {'x': 25.4417, 'y': 42.3682}]
        objetos = obj_controlador.processa_objs_e_coordenadas(coordenadas)
        objetos | should | equal_to([{'x': 24.4861, 'y': 24.4861, 'OBJ': 'a'}, {'x': 3.024, 'y': 43.2541, 'OBJ': 'b'}, {'x': 25.4417, 'y': 42.3682, 'OBJ': 'c'}])