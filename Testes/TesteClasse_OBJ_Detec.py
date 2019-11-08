import unittest
from Controller.Classe_Posicionamento import Classe_Posicionamento
from should_dsl import should, should_not

from Controller.Classe_OBJ_Detec import *


class TesteClasse_OBJ_Detec(unittest.TestCase):



    def teste_aproximar_coordenadas(self):
        obj_detec = Classe_OBJ_Detec()
        coordenadas = [{'x': 24.4861, 'y': 24.4861}, {'x': 3.024, 'y': 43.2541}, {'x': 25.4417, 'y': 25.3682}]
        coordenadas_aproximadas = obj_detec.aproximar_coordenadas(coordenadas)
        coordenadas_esperadas = [{'x': 24.9639, 'y': 24.9272}, {'x': 3.024, 'y': 43.2541}]
        for ponto in coordenadas_aproximadas:
            coordenadas_esperadas |should| contain(ponto)

    def teste_tipo_retorno_aproximar_coordenadas(self):
        obj_detec = Classe_OBJ_Detec()
        coordenadas = [{'x': 24.4861, 'y': 24.4861}, {'x': 3.024, 'y': 43.2541}, {'x': 25.4417, 'y': 25.3682}]

        coordenadas_aproximadas = obj_detec.aproximar_coordenadas(coordenadas)

        coordenadas | should | be_kind_of(list)

        for ponto in coordenadas_aproximadas:
            ponto | should | be_kind_of(dict)

    def teste_rotular_coordenadas(self):
        obj_detec = Classe_OBJ_Detec()
        coordenadas = [{'x': 24.4861, 'y': 24.4861}, {'x': 3.024, 'y': 43.2541}, {'x': 25.4417, 'y': 25.3682}]

        coordenadas_aproximadas = obj_detec.aproximar_coordenadas(coordenadas)

        coordenadas_rotuladas = obj_detec.rotular_coordenadas(coordenadas_aproximadas)

        for ponto in coordenadas_rotuladas:
            ponto |should| include_keys('OBJ')

    def teste_tipo_retorno_rotular_coordenadas(self):

        obj_detec = Classe_OBJ_Detec()
        coordenadas = [{'x': 24.4861, 'y': 24.4861}, {'x': 3.024, 'y': 43.2541}, {'x': 25.4417, 'y': 25.3682}]

        coordenadas_aproximadas = obj_detec.aproximar_coordenadas(coordenadas)

        coordenadas_rotuladas = obj_detec.rotular_coordenadas(coordenadas_aproximadas)

        coordenadas_rotuladas | should | be_kind_of(list)
        for ponto in coordenadas_aproximadas:
            ponto | should | be_kind_of(dict)


    def teste_identificar_objetos(self):

        obj_detec = Classe_OBJ_Detec()
        coordenadas = [{'x': 24.4861, 'y': 24.4861}, {'x': 3.024, 'y': 43.2541}, {'x': 25.4417, 'y': 25.3682}]
        coordenadas_processadas = obj_detec.identificar_objetos(coordenadas)

        coordenadas_esperadas = [{'x': 24.9639, 'OBJ': 'a', 'y': 24.9272}, {'x': 3.024, 'OBJ': 'b', 'y': 43.2541}]

        for ponto in coordenadas_processadas:
            coordenadas_esperadas | should | contain(ponto)

    def teste_tipo_retorno_identificar_objetos(self):

        obj_detec = Classe_OBJ_Detec()
        coordenadas = [{'x': 24.4861, 'y': 24.4861}, {'x': 3.024, 'y': 43.2541}, {'x': 25.4417, 'y': 25.3682}]
        coordenadas_processadas = obj_detec.identificar_objetos(coordenadas)