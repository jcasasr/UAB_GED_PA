import os
import re
from typing import List, Tuple, Dict


def llegeix_vocabulari(nom_fitxer: str) -> List[str]:
    """
    Llegeix d'un fiter les paraules que formen part del vocabulari i les guarda
    en una llista

    PARAMETERS:
        nom_fitxer:str
            Nom del fitxer que conté les paraules del vocabulari, una paraula
            a cada línia del fitxer
    RETURN:
        vocabulari: list[str]
            Llista amb totes les paraules que formen el vocabulari que s'ha de
            considerar per obtenir la representació BoW. Cada element de la
            llista és una paraula del vocabulari
    """


def crea_bow(nom_fitxer: str, vocabulari: List[str]) -> Dict[str, int]:
    """
    Obté la representació BoW en forma de diccionari d'un missatge guardat
    en un fitxer de text

    PARAMETERS:
        nom_fitxer:str
            Nom del fitxer que conté el missatge
        vocabulari: list[str]
            Llista amb totes les paraules que formen el vocabulari que s'ha de
            considerar per obtenir la representació BoW. Cada element de la
            llista és una paraula del vocabulari
    RETURN:
        bow: Dict[str, int]
            Diccionari amb la representació BoW del missatge. El diccionari
            conté per cada paraula del vocabulari el nº de vegades que aquesta
            paraula apareix al missatge
    """


def compara_bow(bow1: Dict[str, int], bow2: Dict[str, int]) -> float:
    """
    Compara la representació BoW de dos missatges, retornant una distància que
    mesura el grau de similitud entre els dos missatges

    PARAMETERS:
        bow1, bow2:dict[str, int]
            Diccionaris amb la representació BoW dels dos missatges a comparar
    RETURN:
        distancia: float
            Valor de la distància entre les dues representacions BoW
    """


def crea_conjunt_entrenament(train: str, vocabulari: List[str]) -> List:
    """
    Llegeix tots els missatges del conjunt d'entrenament i obté la seva
    representació BoW. Per cada missatge d'entrenament guarda la seva
    representació i una etiqueta que ens diu si és un missatge d'spam o no

    PARAMETERS:
        train: str
            Nom del directori on estan tots els missatges d'entrenament
        vocabulari: list[str]
            Llista amb totes les paraules que formen el vocabulari que s'ha de
            considerar per obtenir la representació BoW. Cada element de la
            llista és una paraula del vocabulari

    RETURN:
        training_set: list[tuple[str, dict[str, int], bool]]
            Retorna una llista que conté tota la informació del conjunt
            d'entrenament. La llista conté un element per cada missatge
            d'entrenament. Cada element de la llista és una tupla amb tres
            elements: el nom del fitxer que conté el missatge, el diccionari
            amb la representació BoW del missatge i un booleà que ens indica
            si el missatge és spam (True) o no (False)
    """


def classifica_document(nom_fitxer: str, training_set: List,
                        vocabulari: List[str], k: int) -> Tuple:
    """
    Classifica un missatge com a spam o no spam

    PARAMETERS:
        nom_fitxer: str
            Nom del fitxer que conté el missatge que volem classificar
        training_set: list[tuple[str, dict[str, int], bool]]
            Conjunt d'entrenament tal com s'obté per la funció
            'crea_conjunt_entrenament'
        vocabulari: list[str]
            Llista amb totes les paraules que formen el vocabulari que s'ha de
            considerar per obtenir la representació BoW. Cada element de la
            llista és una paraula del vocabulari
        k: int
            Nombre d'elements del conjunt d'entrenament que s'han de considerar
            per fer la classificació K-NN del missatge.

    RETURN:
        resultat: tuple[bool, list[float]]
            Retorna una tupla amb el resultat de la classificació del missatge:
            el primer valor és un booleà que indica si el missatge és
            spam (True) o no (False). El segon és una llista amb les k
            distàncies que s'han tingunt en compte per determinar el resultat
            de la classificació
    """


def deteccio_spam(train: str, test: str, fitxer_vocabulari: str, k) -> List:
    """
    Fa la detecció de spam per tots els missatges que estan en el directori de
    test

    PARAMETERS:
        train: str
            Nom del directori on estan tots els missatges d'entrenament
        test: str
            Nom del directori on estan tots els missatges que volem classificar
            com a spam o no
        nom_fitxer:str
            Nom del fitxer que conté les paraules del vocabulari
        k: int
            Nombre d'elements que s'han de considerar per fer la classificació
            K-NN del missatge

    RETURN:
        resultat: list[tuple[str, bool, list[float]]]
            Retorna una llista amb el resultat de la classificació per tots els
            missatges del directori de test. Cada element de la llista és una
            tupla amb el resultat de la classificació del missatge:
            el primer valor de la tupla és el nom del fitxer que conté el
            missatge. El segon valor és un booleà que indica si el missatge és
            spam (True) o no (False). El tercer és una llista amb les k
            distàncies que s'han tingunt en compte per determinar el resultat
            de la classificació
    """
