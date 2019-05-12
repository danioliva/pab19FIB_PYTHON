

class Fibonacci():

    def init_(self):
        pass

    def compute(self, numero_meses, parejas_producidas):
        conejos_maduros = 0
        conejos_jovenes = 1
        result = 0
        if numero_meses == 1 or numero_meses == 2:
            result = 1
        else:
            for generacion in range(1, numero_meses):
                temporal = conejos_maduros
                conejos_maduros = conejos_jovenes + conejos_maduros
                conejos_jovenes = temporal * parejas_producidas
                result = conejos_jovenes + conejos_maduros
                generacion += 1


        return result

