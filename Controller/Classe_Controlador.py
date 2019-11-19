from Controller.Classe_Comunicacao import *
from Controller.Classe_OBJ_Detec import *
from Controller.Classe_Posicionamento import *

class Classe_Controlador:

    def __init__(self,porta_serial='/dev/ttyACM0',baud_rate = 9600,distanciaS1_S2 = 45.0, distanciaS2_S3 = 30.0):
        self.porta_serial = porta_serial
        self.baud_rate = baud_rate
        self.distanciaS1_S2 = distanciaS1_S2
        self.distanciaS2_S3 = distanciaS2_S3

    def detectar_objetos(self):
        dados_brutos = self.solicita_dados_serial()

    def solicita_dados_serial(self):
        obj_comunicacao = Classe_Comunicacao(porta = self.porta_serial,baudrate = self.baud_rate)
        dados_brutos = obj_comunicacao.obter_dados_brutos()

        return dados_brutos

    def solicita_dados_posicionamento(self, dados_brutos):
        obj_posicionamento = Classe_Posicionamento(distancia_S1_S2 = self.distanciaS1_S2, distanciaS2_S3 = self.distanciaS2_S3)
        return obj_posicionamento.calcular_posicionamento(dados_brutos = dados_brutos)

    def processa_objs_e_coordenadas(self): #parte grafica
        pass