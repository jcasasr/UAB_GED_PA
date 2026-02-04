from typing import List
from moviment import Moviment
from datetime import date, datetime


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


class CompteJove(CompteCorrent):
    _punts: int
    
    def __init__(self, titular:str="", saldo:float=0.0, punts:int=0) -> None:
        super().__init__(titular, saldo)
        self._punts = punts
        
    def get_punts(self) -> int:
        return self._punts


class CompteNomina(CompteCorrent):
    _bonificacio: float
    
    def __init__(self, titular:str="", saldo:float=0.0, bonificacio:float=0.0) -> None:
        super().__init__(titular, saldo)
        self._bonificacio = bonificacio

    def get_bonificacio(self) -> float:
        return self._bonificacio