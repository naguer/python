class Mate():
    def __init__(self):
        self.maxCebadas = 4
        ''' Pregunta1: Los otros atributos cebadasRestantes/estadoMate
        tambien tienen que ir definidos en el constructor, o tienen que
        que estar en la clase, pero afuera del constructor?'''
        self.cebadasRestantes = self.maxCebadas
        ''' Pregunta2: El estado de mate es un boolean(false/true),
        tengo alguna ventaja al definirlo de tal manera? O puedo simplemente definirlo
        como vacio/lleno y comparlos como hice? '''
        self.estadoMate = "Lleno"

    def cebar(self):
        if self.estadoMate == "Lleno":
            print ("Cuidado, te quemaste!\n")
        else:
            self.estadoMate = "Lleno"

    def beber(self):
        if self.estadoMate == "Vacio":
            print ("El mate esta vacio!\n")
        else:
            self.estadoMate = "Vacio"
            if self.cebadasRestantes > 0:
                self.cebadasRestantes = self.cebadasRestantes - 1
            elif self.cebadasRestantes == 0:
                print ("El mate esta lavado")

    def imprimirMate(self):
        print ("Mate: ",self.estadoMate, "\nMax cebadas: ",self.maxCebadas, "\nCebadas rest sin mate lavado: ", self.cebadasRestantes)

    def decisionCebarBeber(self):
        while True:
            rta = input("Que desea hacer cebar, beber o salir? c b s?: ")
            if rta == "c":
                self.cebar()
                self.imprimirMate()
            elif rta == "b":
                self.beber()
                self.imprimirMate()
            elif rta == "s":
                exit()
            else:
                print ("No es un opcion valida, solo son opciones 'c' 'b' o 's'")

# Creo un matelisto del tipo Mate
matelisto = Mate()
matelisto.imprimirMate()
matelisto.decisionCebarBeber()
