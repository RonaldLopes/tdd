
class Classe_OBJ_Detec:

    def identificar_objetos(self, coordenadas):
        coordenadas_aproximadas = self.aproximar_coordenadas(coordenadas)
        coordenadas_rotuladas = self.rotular_coordenadas(coordenadas_aproximadas)

        return coordenadas_rotuladas

    def aproximar_coordenadas(self, coordenadas, distancia_maxima = 3.0):
        '''
        Exemplo de coordenada = [{'x': 24.4861, 'y': 24.4861,proximo: Treu}, {'x': 3.024, 'y': 43.2541}, {'x': 25.4417, 'y': 42.3682}]
        Distancia minima permitida = 2 cm
        '''
        for ponto in coordenadas:
            ponto['proximo'] = False
        coordenadas_unificadas = []
        for i in range(len(coordenadas)):
            temp = coordenadas[i]
            for j in range(i+1,len(coordenadas)):
                if (abs(temp['x']-coordenadas[j]['x']) <= distancia_maxima) and (abs(temp['y']-coordenadas[j]['y']) <= distancia_maxima):
                    x_medio = float("{0:.4f}".format((temp['x']+coordenadas[j]['x'])/2.0))
                    y_medio = float("{0:.4f}".format((temp['y']+coordenadas[j]['y'])/2.0))
                    coordenadas[j]['proximo'] = True
                    temp['x'] = x_medio
                    temp['y'] = y_medio
            if temp['proximo'] == False:
                temp.pop("proximo")
                coordenadas_unificadas.append(temp)
        return coordenadas_unificadas

    def rotular_coordenadas(self, coordenadas):
        for i in range(len(coordenadas)):
            coordenadas[i]["OBJ"] = chr(97+i)

        return coordenadas