

class Classe_Posicionamento:

    def __init__(self,distancia_S1_S2 = 0.0, distanciaS2_S3 = 0.0):
        self.distancia_S1_S2 = distancia_S1_S2
        self.distancia_S2_S3 = distanciaS2_S3

    def definir_margem_mapeamento(self, distancia_S1_S2, distancia_S2_S3):
        self.distancia_S1_S2 = distancia_S1_S2
        self.distancia_S2_S3 = distancia_S2_S3

    def calcula_coordenadas(self, dados_brutos):
        pass

    def solicita_ID_objetos(self, coordenadas):
        pass

    def calcular_posicionamento(self,dados_brutos):
        pass