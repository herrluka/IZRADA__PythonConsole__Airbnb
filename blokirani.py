FAJL = './podaci/blokirani.txt'


def svi_blokirani():
    with open(FAJL) as file:
        line = file.readline()
        return line.split('|')


def sacuvaj(lista):
    with open(FAJL, 'w') as file:
        novi_sadrzaj = ""
        for b in lista:
            novi_sadrzaj += "{}|".format(b)

        if novi_sadrzaj:
            novi_sadrzaj = novi_sadrzaj[:-1]

        file.write(novi_sadrzaj)


def blokiraj(korisnicko_ime):
    svi = svi_blokirani()
    if korisnicko_ime in svi:
        return

    svi.append(korisnicko_ime)

    sacuvaj(svi)