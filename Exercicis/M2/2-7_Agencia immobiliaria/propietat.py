from contracte import Contracte, Lloguer, Venda


def llegeixBool(missatge):
    valor = input(missatge)
    assert valor == 's' or valor == 'n', "Valor incorrecte"
    return (valor == 's')


class Propietat:
    _codi: str
    _superficie: float
    _n_habitacions: int 
    _n_banys: int 
    _contracte: Contracte

    def __init__(self, codi="", superficie=0.0, n_habitacions=0, n_banys=0):
        self._codi = codi
        self._superficie = superficie
        self._n_habitacions = n_habitacions
        self._n_banys = n_banys
        self._contracte = None

    def llegeix(self):
        self._codi = input("Codi de la propietat: ")
        self._superficie = float(input("Superficie (em m2): "))
        self._n_habitacions = int(input("N. habitacions: "))
        self._n_banys = int(input("N. banys: "))
        tipus_contracte = input("Tipus Contracte (L: lloguer, V: Venda): ")
        if tipus_contracte == 'L':
            self._contracte = Lloguer()
        else:
            self._contracte = Venda()
        self._contracte.llegeix()

    def mostra(self):
        print("Codi: ", self._codi)
        print("Superficie (en m2): ", self._superficie)
        print("N. habitacions: ", self._n_habitacions)
        print("N. banys: ", self._n_banys)

    def preu(self) -> float:
        return self._contracte.preu()


class Casa(Propietat):
    _superficie_jardi: float 
    _te_garatge: bool 

    def __init__(self, codi="", superficie=0.0, n_habitacions=0, n_banys=0, superficie_jardi=0.0, te_garatge=False):
        super().__init__(codi, superficie, n_habitacions, n_banys)
        self._superficie_jardi = superficie_jardi
        self._te_garatge = te_garatge

    def llegeix(self):
        super().llegeix()
        self._superficie_jardi = float(input("Superficie del jardi: "))
        self._te_garatge = llegeixBool("Te garatge? (s/n)")

    def mostra(self):
        super().mostra()
        print("Superficie del jardi: ", self._superficie_jardi)
        print("Garatge: ", self._te_garatge)
        self._contracte.mostra()


class Pis(Propietat):
    _te_terrassa: bool
    _te_ascensor: bool

    def __init__(self, codi="", superficie=0.0, n_habitacions=0, n_banys=0, te_terrassa=False, te_ascensor=False):
        super().__init__(codi, superficie, n_habitacions, n_banys)
        self._te_terrassa = te_terrassa
        self._te_ascensor = te_ascensor

    def llegeix(self):
        super().llegeix()
        self._te_terrassa = llegeixBool("Te terrassa? (s/n)")
        self._te_ascensor = llegeixBool("Te ascensor? (s/n)")

    def mostra(self):
        super().mostra()
        print("Terrassa: ", self._te_terrassa)
        print("Ascensor: ", self._te_ascensor)
        self._contracte.mostra()
