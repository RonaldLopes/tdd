
class Classe_OBJ_Detec:

    def identificar_objetos(self, coordenadas):
        valor = 0
        for ponto in coordenadas:
            ponto["OBJ"] = valor + 1
            valor = valor + 1

        return coordenadas

    def identificar_pontos_proximos(self, coordenadas):
        pass

    def aproximar_coordenadas(self):
        pass

    def rotular_coordenadas(self):
        pass