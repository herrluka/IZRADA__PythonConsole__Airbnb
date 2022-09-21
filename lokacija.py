from klase import Lokacija, Adresa

FAJL = './podaci/lokacije.txt'

def sve_lokacije():
    lokacije = list()
    with open(FAJL) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            podeljena_linija = line.split('|')
            lokacija = Lokacija()
            lokacija.geografska_sirina = podeljena_linija[0]
            lokacija.geografska_duzina = podeljena_linija[1]

            adresa = Adresa()
            adresa.broj = podeljena_linija[2]
            adresa.ulica = podeljena_linija[3]
            adresa.postanski_broj = podeljena_linija[4]
            adresa.naseljeno_mesto = podeljena_linija[5]

            lokacija.adresa = adresa

            lokacije.append(lokacija)

    return lokacije