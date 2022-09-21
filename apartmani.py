import datetime

from klase import Apartman, TipApartman, Lokacija, ApartmanStatus, Korisnik, Adresa, Sadrzaj

FAJL = './podaci/apartmani.txt'

def svi_apartmani():
    apartmani = list()
    with open(FAJL) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            podeljena_linija = line.split('|')
            apartman = Apartman()
            apartman.sifra = int(podeljena_linija[0])
            apartman.tip = TipApartman.from_str(podeljena_linija[1])
            apartman.broj_soba = int(podeljena_linija[2])
            apartman.broj_gostiju = int(podeljena_linija[3])
            apartman.status = ApartmanStatus.from_str(podeljena_linija[4])
            apartman.cena_po_noci = int(podeljena_linija[5])

            domacin_linija = podeljena_linija[6].split(';')
            domacin = Korisnik()
            domacin.ime = domacin_linija[0]
            domacin.prezime = domacin_linija[1]
            domacin.email = domacin_linija[2]
            domacin.korisnicko_ime = domacin_linija[3]
            domacin.lozinka = domacin_linija[4]
            domacin.uloga = domacin_linija[5]
            domacin.kontakt_telefon = domacin_linija[6]
            domacin.pol = domacin_linija[7]
            apartman.domacin = domacin

            lokacija_line = podeljena_linija[7].split(';')
            lokacija = Lokacija()
            lokacija.geografska_sirina= lokacija_line[0]
            lokacija.geografska_duzina = lokacija_line[1]

            adresa_linija = lokacija_line[2].split('~')
            adresa = Adresa()
            adresa.broj = adresa_linija[0]
            adresa.ulica = adresa_linija[1]
            adresa.postanski_broj = adresa_linija[2]
            adresa.naseljeno_mesto = adresa_linija[3]

            lokacija.adresa = adresa

            apartman.lokacija = lokacija

            if podeljena_linija[8]:
                dostupnost_linija= podeljena_linija[8].split(';')
                dostupnosti = list()
                for datumi_linija in dostupnost_linija:
                    dostupnosti.append((datumi_linija.split('~')[0], datumi_linija.split('~')[1]))

                apartman.dostupnost = dostupnosti

            sadrzaji = list()
            if podeljena_linija[9]:
                sadrzaji_linija = podeljena_linija[9]
                for sadrzaj_linija_podeljeno in sadrzaji_linija.split(';'):
                    sadrzaj_linija_obelezja = sadrzaj_linija_podeljeno.split('~')
                    sadrzaj = Sadrzaj()
                    sadrzaj.sifra = sadrzaj_linija_obelezja[0]
                    sadrzaj.naziv = sadrzaj_linija_obelezja[1]
                    sadrzaji.append(sadrzaj)

                apartman.sadrzaji = sadrzaji

            apartmani.append(apartman)

    return apartmani


def sacuvaj(lista_apartmana):
    with open(FAJL, 'w') as file:
        novi_sadrzaj = ""
        for ap in lista_apartmana:
            dostupnost = ""
            for d in ap.dostupnost:
                dostupnost += d[0] + "~" + d[1] + ";"

            sadrzaj = ""
            for s in ap.sadrzaji:
                sadrzaj += str(s.sifra) + "~" + s.naziv + ";"

            if sadrzaj != "":
                sadrzaj = sadrzaj[:-1]

            if dostupnost != "":
                dostupnost = dostupnost[:-1]

            line = "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(
                ap.sifra,
                ap.tip.value,
                ap.broj_soba,
                ap.broj_gostiju,
                ap.status.value,
                ap.cena_po_noci,
                "{};{};{};{};{};{};{};{}".format(
                    ap.domacin.ime,
                    ap.domacin.prezime,
                    ap.domacin.email,
                    ap.domacin.korisnicko_ime,
                    ap.domacin.lozinka,
                    ap.domacin.uloga,
                    ap.domacin.kontakt_telefon,
                    ap.domacin.pol,
                ),
                "{};{};{}~{}~{}~{}".format(
                    ap.lokacija.geografska_sirina,
                    ap.lokacija.geografska_duzina,
                    ap.lokacija.adresa.broj,
                    ap.lokacija.adresa.ulica,
                    ap.lokacija.adresa.postanski_broj,
                    ap.lokacija.adresa.naseljeno_mesto
                ),
                dostupnost,
                sadrzaj
            )

            novi_sadrzaj += line + '\n'

        novi_sadrzaj = novi_sadrzaj.strip()
        file.write(novi_sadrzaj)


def aktivni_apartmani():
    aktivni = list()
    for apartman in svi_apartmani():
        if apartman.status == ApartmanStatus.AKTIVAN:
            aktivni.append(apartman)

    return aktivni


def pretrazi(tip_pretrage, tekst):
    if tip_pretrage == 'a':
        filtrirani = list()
        for apart in aktivni_apartmani():
            if tekst in apart.lokacija.adresa.naseljeno_mesto:
                filtrirani.append(apart)

        return filtrirani
    elif tip_pretrage == 'b':
        datum_pretrage = datetime.datetime.strptime(tekst, '%d.%m.%Y.')
        filtrirani = list()
        for apart in aktivni_apartmani():
            postoji_dostupan = False
            for dostupnost in apart.dostupnost:
                datum_do = datetime.datetime.strptime(dostupnost[1], '%d.%m.%Y.')
                if datum_pretrage >= datum_do:
                    postoji_dostupan = True

            if postoji_dostupan:
                filtrirani.append(apart)

        return filtrirani

    elif tip_pretrage == 'c':
        datum_pretrage = datetime.datetime.strptime(tekst, '%d.%m.%Y.')

        filtrirani = list()
        for apart in aktivni_apartmani():
            postoji_dostupan = False
            for dostupnost in apart.dostupnost:
                datum_od = datetime.datetime.strptime(dostupnost[0], '%d.%m.%Y.')
                if datum_pretrage <= datum_od:
                    postoji_dostupan = True

            if postoji_dostupan:
                filtrirani.append(apart)

        return filtrirani
    elif tip_pretrage == 'd':
        filtrirani = list()
        for apart in aktivni_apartmani():
            if apart.broj_soba < int(tekst):
                filtrirani.append(apart)

        return filtrirani
    elif tip_pretrage == 'e':
        filtrirani = list()
        for apart in aktivni_apartmani():
            if apart.broj_soba > int(tekst):
                filtrirani.append(apart)

        return filtrirani
    elif tip_pretrage == 'f':
        filtrirani = list()
        for apart in aktivni_apartmani():
            if apart.cena_po_noci < int(tekst):
                filtrirani.append(apart)

        return filtrirani
    elif tip_pretrage == 'g':
        filtrirani = list()
        for apart in aktivni_apartmani():
            if apart.cena_po_noci > int(tekst):
                filtrirani.append(apart)

        return filtrirani


def visekriterijumska_pretraga(pretraga_mesto, pretraga_vreme_pre, pretraga_vreme_posle,
                                                     pretraga_broj_soba_manje, pretraga_broj_soba_vece,
                                                     pretraga_cena_manje, pretraga_cena_vece):
    filtrirani = aktivni_apartmani()
    if pretraga_mesto:
        pomocna = list()
        for apart in filtrirani:
            if pretraga_mesto in apart.lokacija.adresa.naseljeno_mesto:
                pomocna.append(apart)

        filtrirani = pomocna

    if pretraga_vreme_pre:
        datum_pretrage = datetime.datetime.strptime(pretraga_vreme_pre, '%d.%m.%Y.')
        pomocna = list()
        for apart in filtrirani:
            postoji_dostupan = False
            for dostupnost in apart.dostupnost:
                datum_do = datetime.datetime.strptime(dostupnost[1], '%d.%m.%Y.')
                if datum_pretrage >= datum_do:
                    postoji_dostupan = True

            if postoji_dostupan:
                pomocna.append(apart)

        filtrirani = pomocna

    if pretraga_vreme_posle:
        datum_pretrage = datetime.datetime.strptime(pretraga_vreme_posle, '%d.%m.%Y.')
        pomocna = list()
        for apart in filtrirani:
            postoji_dostupan = False
            for dostupnost in apart.dostupnost:
                datum_od = datetime.datetime.strptime(dostupnost[0], '%d.%m.%Y.')
                if datum_pretrage <= datum_od:
                    postoji_dostupan = True

            if postoji_dostupan:
                pomocna.append(apart)

        filtrirani = pomocna

    if pretraga_broj_soba_manje:
        pomocna = list()
        for apart in filtrirani:
            if apart.broj_soba < int(pretraga_broj_soba_manje):
                pomocna.append(apart)

        filtrirani = pomocna

    if pretraga_broj_soba_vece:
        pomocna = list()

        for apart in filtrirani:
            if apart.broj_soba > int(pretraga_broj_soba_vece):
                pomocna.append(apart)

        filtrirani = pomocna

    if pretraga_cena_manje:
        pomocna = list()
        for apart in filtrirani:
            if apart.cena_po_noci < int(pretraga_cena_manje):
                pomocna.append(apart)

        filtrirani = pomocna

    if pretraga_cena_vece:
        pomocna = list()
        for apart in filtrirani:
            if apart.cena_po_noci > int(pretraga_cena_vece):
                pomocna.append(apart)

        filtrirani = pomocna

    return filtrirani


def dodaj_apartman(apartman):
    ap = svi_apartmani()
    ap.append(apartman)
    sacuvaj(ap)


def apartman_po_sifri(sifra):
    for ap in svi_apartmani():
        if ap.sifra == sifra:
            return ap


def azuriraj(apartman):
    svi = svi_apartmani()
    print(apartman.status)
    for a in svi:
        if a.sifra == apartman.sifra:
            a.tip = apartman.tip
            a.broj_soba = apartman.broj_soba
            a.broj_gostiju = apartman.broj_gostiju
            a.lokacija = apartman.lokacija
            a.dostupnost = apartman.dostupnost
            a.cena_po_noci = apartman.cena_po_noci
            a.status = apartman.status
            a.sadrzaji = apartman.sadrzaji

    sacuvaj(svi)


def obrisi(apartman):
    filtrirani = list()
    for a in svi_apartmani():
        if a.sifra != apartman.sifra:
            filtrirani.append(a)

    sacuvaj(filtrirani)


def apartmani_domacin(domacin):
    lista = []
    for ap in svi_apartmani():
        if ap.domacin.korisnicko_ime == domacin.korisnicko_ime:
            lista.append(ap)

    return lista