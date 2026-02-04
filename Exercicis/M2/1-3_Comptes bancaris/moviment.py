from datetime import date, datetime


class Moviment:
    _descripcio: str
    _valor: float
    _data: date

    def __init__(self, descripcio: str = "", valor: float = 0.0, data: str = '') -> None:
        self._descripcio = descripcio
        self._valor = valor
        if data == '':
            self._data = date.today()
        else:
            self._data = datetime.strptime(data, '%d/%m/%Y')

    def get_descripcio(self) -> str:
        return self._descripcio

    def set_descripcio(self, valor: str) -> None:
        self._descripcio = valor

    def get_valor(self) -> float:
        return self._valor

    def set_valor(self, valor: float) -> None:
        self._valor = valor

    def get_data(self) -> str:
        return datetime.strftime(self._data, '%d/%m/%Y')

    def set_data(self, valor: str) -> None:
        self._data = datetime.strptime(valor, '%d/%m/%Y')


class Rebut(Moviment):
    _entitat: str = ''

    def __init__(self, descripcio: str = "", valor: float = 0.0, data: str = '', entitat=''):
        super().__init__(descripcio, valor, data)
        self._entitat = entitat

    def get_entitat(self) -> str:
        return self._entitat

    def set_entitat(self, valor: str) -> None:
        self._entitat = valor