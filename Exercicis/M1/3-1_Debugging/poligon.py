import os
import punt


def llegeix_poligon(nom_fitxer):
    with open(nom_fitxer, "r") as fitxer:
        poligon = []
        for linia in fitxer:
            valors = linia.split()
            poligon.append(punt.Point(int(valors[0]), int(valors[1])))
    return poligon


def bounding_box(poligon):
    x = [p.get_x() for p in poligon]
    y = [p.get_y() for p in poligon]
    top_left = punt.Point(min(x), min(y))
    bottom_right = punt.Point(max(x), max(y))
    return top_left, bottom_right


def area_bounding_box(bb):
    dx = bb[1].get_x() - bb[0].get_x()
    dy = bb[0].get_y() - bb[1].get_y()
    return dx * dy


if __name__ == '__main__':
    directori_prova = 'prova/'
    fitxers_prova = os.listdir(directori_prova)
    for fitxer in fitxers_prova:
        poligon = llegeix_poligon(directori_prova + fitxer)
        bb = bounding_box(poligon)
        area = area_bounding_box(bb)
        print("Bounding box:", bb[0], bb[1])
        print("Area bounding box", area)
