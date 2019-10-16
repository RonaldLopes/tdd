
class Classe_OBJ_Detec:

    def identificar_objetos(self, coordenadas):
        valor = 0
        for ponto in coordenadas:
            ponto["OBJ"] = valor + 1
            valor = valor + 1

        return coordenadas