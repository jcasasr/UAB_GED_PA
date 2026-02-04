from compte import CompteCorrent, CompteJove, CompteNomina
from moviment import Moviment, Rebut
from typing import Dict, List


def inicialitza_comptes(comptes: Dict[str, CompteCorrent], nom_fitxer: str) -> None:


def filtra_moviments(comptes: Dict[str, CompteCorrent], titular: str) -> List[Moviment]:


def recupera_moviments(comptes: Dict[str, CompteCorrent], titular: str, data_inicial: str, data_final: str) -> List[Moviment]:


def aplica_bonificacio(comptes: Dict[str, CompteCorrent], titular: str) -> None: