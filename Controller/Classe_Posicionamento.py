
import math

class Classe_Posicionamento:

    def __init__(self,distancia_S1_S2 = 0.0, distanciaS2_S3 = 0.0):
        self.distancia_S1_S2 = distancia_S1_S2
        self.distancia_S2_S3 = distanciaS2_S3

    def definir_margem_mapeamento(self, distancia_S1_S2, distancia_S2_S3):
        self.distancia_S1_S2 = distancia_S1_S2
        self.distancia_S2_S3 = distancia_S2_S3

    def calcula_coordenadas(self, dados_brutos):
        pass

    def calcula_velocidade_do_som(self, temperatura_celsius):
        '''velocidade do som para o AR = c = co * (√(T/T0))'''
        temperatura_kelvin = temperatura_celsius + 273.15
        velocidade_som = 331.45 * (math.sqrt(temperatura_kelvin/273.15))
        return velocidade_som

    def calcula_distancia(self, velocidade_som, tempo_de_resposta):
        ''' distancia = (Tempo de duração do sinal de saída × velocidade do som) / 2'''
        distancia = (velocidade_som * tempo_de_resposta)/2.0
        return distancia


    def solicita_ID_objetos(self, coordenadas):
        pass

    def calcular_posicionamento(self,dados_brutos):
        pass