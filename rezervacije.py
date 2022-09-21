from klase import Rezervacija, RezervacijaStatus, Korisnik

FAJL = './podaci/rezervacije.txt'


def sve_rezervacije():
    rezervacije = list()
    with open(FAJL) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            podeljena_linija = line.split('|')
            
            rezervacija = Rezervacija()
            rezervacija.apartman = int(podeljena_linija[0])
            rezervacija.pocetni_datum = podeljena_linija[1]
            rezervacija.broj_nocenja = int(podeljena_linija[2])
            rezervacija.ukupna_cena = int(podeljena_linija[3])

            gost_linija = podeljena_linija[4].split(';')
            gost = Korisnik()
            gost.ime = gost_linija[0]
            gost.prezime = gost_linija[1]
            gost.email = gost_linija[2]
            gost.korisnicko_ime = gost_linija[3]
            gost.lozinka = gost_linija[4]
            gost.uloga = gost_linija[5]
            gost.kontakt_telefon = gost_linija[6]
            gost.pol = gost_linija[7]
            rezervacija.gost = gost
            
            rezervacija.status = RezervacijaStatus.from_str(podeljena_linija[5])

            rezervacije.append(rezervacija)

        return rezervacije


def sacuvaj(lista_rezervacija):
    with open(FAJL, 'w') as file:
        novi_sadrzaj = ""
        for r in lista_rezervacija:
            novi_sadrzaj += "{}|{}|{}|{}|{}|{}\n".format(
                r.apartman, 
                r.pocetni_datum, 
                r.broj_nocenja,
                r.ukupna_cena,
                "{};{};{};{};{};{};{};{}".format(
                    r.gost.ime,
                    r.gost.prezime,
                    r.gost.email,
                    r.gost.korisnicko_ime,
                    r.gost.lozinka,
                    r.gost.uloga,
                    r.gost.kontakt_telefon,
                    r.gost.pol
                ),
                r.status.value)
                
        novi_sadrzaj = novi_sadrzaj.strip()

        file.write(novi_sadrzaj)


def dodaj(rezervacija):
    svi = sve_rezervacije()
    svi.append(rezervacija)
    sacuvaj(svi)


def revervacije_domacin(domacin_apartmani):
    lista = []
    for r in sve_rezervacije():
        for apartman in domacin_apartmani:
            if r.apartman == apartman.sifra:
               lista.append(r)

    return lista