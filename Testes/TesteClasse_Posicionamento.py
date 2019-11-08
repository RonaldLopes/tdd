import unittest
from Controller.Classe_Posicionamento import Classe_Posicionamento
from should_dsl import should, should_not

from Controller.Classe_Comunicacao import *


class TesteClasse_Posicionamento(unittest.TestCase):

    def teste_calcular_posicionamento(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2 = 0.0, distanciaS2_S3 = 0.0)
        dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0,'tempo':0.2},
                        {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0,'tempo':0.02},
                        {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0,'tempo':0.03}]
        objetos = posicionamento.calcular_posicionamento(dados_brutos)



    def teste_definir_margem_mapeamento(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=0.0, distanciaS2_S3=0.0)
        dist1 = 33.9
        dist2 = 45.6
        posicionamento.definir_margem_mapeamento(dist1,dist2)
        posicionamento.distancia_S2_S3 |should| equal_to(dist2)
        posicionamento.distancia_S1_S2 | should | equal_to(dist1)

    def teste_tipo_retorno_calcula_velocidade_do_som(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        velocidade = posicionamento.calcula_velocidade_do_som(temperatura_celsius=0.0)
        velocidade |should| be_kind_of(float)

    def teste_calcula_velocidade_do_som(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        velocidade = posicionamento.calcula_velocidade_do_som(temperatura_celsius=0.0)
        velocidade |should| close_to(332, delta=0.7)

    def teste_tipo_retorno_calcula_distancia(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        distancia = posicionamento.calcula_distancia(velocidade_som = 343.0, tempo_de_resposta = 1)
        distancia |should| be_kind_of(float)

    def teste_calcula_distancia(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        distancia = posicionamento.calcula_distancia(velocidade_som = 343.0, tempo_de_resposta = 1)
        distancia |should| close_to(171.0, delta=3)

    def teste_calcula_distancia_negativo(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        distancia = posicionamento.calcula_distancia(velocidade_som = 343.0, tempo_de_resposta = 1)
        distancia |should_not| be_less_than(0)

    def teste_calcular_coordenadas_negativo(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0,'tempo': 0.2},
                        {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0,'tempo': 0.02},
                        {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0,'tempo': 0.03}]
        coordenadas = posicionamento.calcula_coordenadas(dados_brutos)

        for ponto in coordenadas:
            ponto['x'] |should_not| be_less_than(0)
            ponto['y'] | should_not | be_less_than(0)

    def teste_tipo_retorno_calcular_coordenadas(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0,'tempo': 0.2},
                        {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0,'tempo': 0.02},
                        {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0,'tempo': 0.03}]
        coordenadas = posicionamento.calcula_coordenadas(dados_brutos)

        for ponto in coordenadas:
            ponto['x'] |should| be_kind_of(float)
            ponto['y'] |should| be_kind_of(float)

    def teste_limite_coordenada_calcular_coordenadas(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0,'tempo': 0.2},
                        {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0,'tempo': 0.02},
                        {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0,'tempo': 0.03}]
        coordenadas = posicionamento.calcula_coordenadas(dados_brutos)

        for ponto in coordenadas:
            ponto['x'] |should| be_greater_than(0.0)
            ponto['y'] | should | be_greater_than(0.0)

        for ponto in coordenadas:
            ponto['x'] |should| be_less_than(posicionamento.distancia_S2_S3)
            ponto['y'] | should | be_less_than(posicionamento.distancia_S1_S2)

    def teste_tipo_retorno_solicita_id_objetos(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0, 'tempo': 0.2},
                        {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0, 'tempo': 0.02},
                        {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0, 'tempo': 0.03}]
        coordenadas = posicionamento.calcula_coordenadas(dados_brutos)

        objetos = posicionamento.solicita_ID_objetos(coordenadas)

        objetos | should | be_kind_of(list)

        for obj in objetos:
            obj | should | be_kind_of(dict)

    def teste_solicita_id_objetos(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0, 'tempo': 0.2},
                        {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0, 'tempo': 0.02},
                        {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0, 'tempo': 0.03}]
        coordenadas = posicionamento.calcula_coordenadas(dados_brutos)

        objetos = posicionamento.solicita_ID_objetos(coordenadas)

        for obj in objetos:
            obj |should| include_keys('OBJ')




