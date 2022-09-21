import blokirani
from klase import Korisnik, KorisnikUloga

FAJL = './podaci/korisnici.txt'


def svi_korisnici():
    korisnici = list()
    with open(FAJL) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            podeljena_linija = line.split('|')
            korisnik = Korisnik()
            korisnik.ime = podeljena_linija[0]
            korisnik.prezime = podeljena_linija[1]
            korisnik.email = podeljena_linija[2]
            korisnik.korisnicko_ime = podeljena_linija[3]
            korisnik.lozinka = podeljena_linija[4]
            korisnik.uloga = podeljena_linija[5]
            korisnik.kontakt_telefon = podeljena_linija[6]
            korisnik.pol = podeljena_linija[7]
            korisnici.append(korisnik)

    return korisnici


def sacuvaj(korisnici):
    with open(FAJL, 'w') as file:
        new_content = ""
        for korisnik in korisnici:
            line = "{}|{}|{}|{}|{}|{}|{}|{}\n".format(
                korisnik.ime,
                korisnik.prezime,
                korisnik.email,
                korisnik.korisnicko_ime,
                korisnik.lozinka,
                korisnik.uloga,
                korisnik.kontakt_telefon,
                korisnik.pol,
            )

            new_content += line

        file.write(new_content)



def login(korisnicko_ime, lozika):
    korisnici = svi_korisnici()

    korisnicka_imena_blokiranih = blokirani.svi_blokirani()

    for k in korisnici:
        if k.korisnicko_ime == korisnicko_ime and k.lozinka == lozika and k.korisnicko_ime not in korisnicka_imena_blokiranih:
            return k

def registracija(ime, prezime, korisnicko_ime, lozinka, kontakt_telefon, email, pol, uloga):
    korisnici = svi_korisnici()
    for k in korisnici:
        if k.korisnicko_ime == korisnicko_ime:
            raise Exception("Korisnicko ime vec postoji")

    korisnik = Korisnik()
    korisnik.ime = ime
    korisnik.prezime = prezime
    korisnik.email = email
    korisnik.korisnicko_ime = korisnicko_ime
    korisnik.lozinka = lozinka
    korisnik.kontakt_telefon = kontakt_telefon
    korisnik.uloga = uloga
    korisnik.pol = pol

    korisnici.append(korisnik)
    sacuvaj(korisnici)


def blokiraj_korisnika(korisnicko_ime):
    blokirani.blokiraj(korisnicko_ime)
