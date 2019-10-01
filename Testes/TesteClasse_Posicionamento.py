import unittest
from Controller.Classe_Posicionamento import Classe_Posicionamento
from should_dsl import should

from Controller.Classe_Comunicacao import *


class TesteClasse_Posicionamento(unittest.TestCase):

    def teste_calcular_posicionamento(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2 = 0.0, distanciaS2_S3 = 0.0)
        dados_brutos = [{'temp': 25.0, 'angulo': 45.0, 'ID': 1.0},
                        {'temp': 30.0, 'angulo': 60.0, 'ID': 2.0},
                        {'temp': 33.0, 'angulo': 30.0, 'ID': 3.0}]
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

    def teste_calcular_coordenadas(self):
        posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
        dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0,'tempo':0.3},
                        {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0,'tempo':0.3},
                        {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0,'tempo':0.3}]
        coordenadas = posicionamento.calcula_coordenadas(dados_brutos)

    def teste_solicita_id_objetos(self):
        pass