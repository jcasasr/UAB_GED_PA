import os
import re
from typing import List, Tuple, Dict


def llegeix_vocabulari(nom_fitxer: str) -> List[str]:
    vocabulari = []
    with open(nom_fitxer, 'r') as file:
        for line in file:
            vocabulari.append(line[:-1])
    return vocabulari


def crea_bow(nom_fitxer: str, vocabulari: List[str]) -> Dict[str, int]:
    bow = {}
    with open(nom_fitxer, "r") as fitxer:
        for linia in fitxer:
            paraules = re.sub("[^a-zA-Z0-9]", " ", linia).split()
            for paraula in paraules:
                paraula = paraula.lower()
                if paraula in vocabulari:
                    if paraula in bow:
                        bow[paraula] = bow[paraula] + 1
                    else:
                        bow[paraula] = 1
    return bow


def compara_bow(bow1: Dict[str, int], bow2: Dict[str, int]) -> float:
    distancia = 0.0
    for paraula in bow1:
        if paraula in bow2:
            distancia = distancia + min(bow1[paraula], bow2[paraula])
    distancia /= min(sum(bow1.values()), sum(bow2.values()))
    return 1 - distancia


