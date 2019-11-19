import math
from Controller.Classe_OBJ_Detec import Classe_OBJ_Detec

class Classe_Posicionamento:

    def __init__(self,distancia_S1_S2 = 0.0, distanciaS2_S3 = 0.0):
        self.distancia_S1_S2 = distancia_S1_S2
        self.distancia_S2_S3 = distanciaS2_S3

    def definir_margem_mapeamento(self, distancia_S1_S2, distancia_S2_S3):
        self.distancia_S1_S2 = distancia_S1_S2
        self.distancia_S2_S3 = distancia_S2_S3

    def calcular_posicionamento(self, dados_brutos):

        coordenadas = []

        for dado in dados_brutos:
            velocidade_som = self.calcula_velocidade_do_som(dado["temperatura"])
            distancia_obj = self.calcula_distancia(velocidade_som,dado["tempo"])

            if dado["ID"] == 1:
                coordenada_x = float("{0:.4f}".format(distancia_obj * math.cos(math.radians(dado["angulo"]))))
                coordenada_y = float("{0:.4f}".format(distancia_obj * math.sin(math.radians(dado["angulo"]))))
            elif dado["ID"] == 2:
                coordenada_x = float("{0:.4f}".format(distancia_obj * math.sin(math.radians(dado["angulo"]))))
                coordenada_y = float("{0:.4f}".format(self.distancia_S1_S2 - (distancia_obj * math.cos(math.radians(dado["angulo"])))))
            elif dado["ID"] == 3:
                coordenada_x = float("{0:.4f}".format(self.distancia_S2_S3 - (distancia_obj * math.cos(math.radians(dado["angulo"])))))
                coordenada_y = float("{0:.4f}".format(self.distancia_S1_S2 - (distancia_obj * math.sin(math.radians(dado["angulo"])))))

            coordenadas.append({"x": coordenada_x,"y":coordenada_y})
        return coordenadas

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
        detector_objetos = Classe_OBJ_Detec()

        return detector_objetos.identificar_objetos(coordenadas)




# posicionamento = Classe_Posicionamento(distancia_S1_S2=45.0, distanciaS2_S3=30.0)
# dados_brutos = [{'temperatura': 25.0, 'angulo': 45.0, 'ID': 1.0,'tempo':0.3},
#                 {'temperatura': 30.0, 'angulo': 60.0, 'ID': 2.0,'tempo':0.3},
#                 {'temperatura': 33.0, 'angulo': 30.0, 'ID': 3.0,'tempo':0.3}]
# coordenadas = posicionamento.calcula_coordenadas(dados_brutos)