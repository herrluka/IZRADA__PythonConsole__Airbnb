from klase import Sadrzaj

FAJL = './podaci/sadrzaji.txt'

def svi_sadrzaji():
    sadrzaji = list()
    with open(FAJL) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            podeljena_linija = line.split('|')
            sadrzaj = Sadrzaj()
            sadrzaj.sifra = int(podeljena_linija[0])
            sadrzaj.naziv = podeljena_linija[1]
            sadrzaji.append(sadrzaj)

    return sadrzaji


def sacuvaj(lista_sarzaja):
    with open(FAJL, 'w') as file:
        novi_sadrzaj = ""
        for s in lista_sarzaja:
            novi_sadrzaj += "{}|{}\n".format(s.sifra, s.naziv)

        novi_sadrzaj = novi_sadrzaj.strip()

        file.write(novi_sadrzaj)


def dodaj_sadrzaj(s):
    svi = svi_sadrzaji()

    for sad in svi:
        if sad.sifra == s.sifra:
            raise Exception("Sifra vec postoji")
        elif sad.naziv == s.naziv:
            raise Exception("Sadrzaj vec postoji")

    svi.append(s)
    sacuvaj(svi)


def brisanje(sifra):
    nova_lista = list()
    for sad in svi_sadrzaji():
        if sad.sifra != sifra:
            nova_lista.append(sad)

    sacuvaj(nova_lista)
