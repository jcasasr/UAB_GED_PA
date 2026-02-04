from typing import List
from moviment import Moviment


class CompteCorrent:
    _titular: str
    _saldo: float
    _moviments: List[Moviment]
    
    def __init__(self, titular:str="", saldo:float=0.0) -> None:
        self._titular = titular
        self._saldo = saldo
        self._moviments = []
    
    def get_titular(self) -> str:
        return self._titular
    
    def get_saldo(self) -> float:
        return self._saldo

    def afegeix_moviment(self, moviment: Moviment) -> None:
        self._moviments.append(moviment)
        self._saldo += moviment.get_valor()
