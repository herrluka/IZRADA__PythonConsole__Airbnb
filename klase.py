import enum


class Korisnik:

    def __init__(self):
        self.korisnicko_ime = ''
        self.lozinka = ''
        self.ime = ''
        self.prezime = ''
        self.pol = ''
        self.kontakt_telefon = ''
        self.email = ''
        self.uloga = None

    @staticmethod
    def heder_tabele(self):
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('Korisnicko ime', 'Lozinka', 'Ime',
                                                                               'Prezime',
                                                                               'Pol', 'Koktakt telefon', 'Email',
                                                                               'Uloga'))


class KorisnikUloga(enum.Enum):
    ADMIN = 'Administrator'
    DOMACIN = 'Domacin'
    GOST = 'Gost'


class Lokacija:
    def __init__(self):
        self.geografska_sirina = None
        self.geografska_duzina = None
        self.adresa = None


class Adresa:
    def __init__(self):
        self.ulica = ''
        self.broj = ''
        self.naseljeno_mesto = ''
        self.postanski_broj = ''


class Apartman:
    def __init__(self):
        self.sifra = None
        self.tip = None
        self.broj_soba = 0
        self.broj_gostiju = 0
        self.lokacija = None
        self.dostupnost = []
        self.domacin = None
        self.cena_po_noci = 0
        self.status = None
        self.sadrzaji = []


class TipApartman(enum.Enum):
    CEO_APARTMAN = 'ceo apartman'
    SOBA = 'soba'

    @staticmethod
    def from_str(label):
        if label == 'ceo apartman':
            return TipApartman.CEO_APARTMAN
        elif label == 'soba':
            return TipApartman.SOBA
        else:
            raise NotImplementedError


class ApartmanStatus(enum.Enum):
    AKTIVAN = 'Aktivno'
    NEAKTIVAN = 'Neaktivno'

    @staticmethod
    def from_str(label):
        if label == 'Aktivno':
            return ApartmanStatus.AKTIVAN
        elif label == 'Neaktivno':
            return ApartmanStatus.NEAKTIVAN
        else:
            raise NotImplementedError


class Sadrzaj:
    def __init__(self):
        self.sifra = None
        self.naziv = ''


class Rezervacija:
    def __init__(self):
        self.apartman = None
        self.pocetni_datum = None
        self.broj_nocenja = 1
        self.ukupna_cena = 0
        self.gost = None
        self.status = None


class RezervacijaStatus(enum.Enum):
    KREIRANA = 'Kreirana'
    ODBIJENA = 'Odbijena'
    ODUSTANAK = 'Odustanak'
    PRIHVACENA = 'Prihvacena'
    ZAVRSENA = 'Zavrsena'

    @staticmethod
    def from_str(label):
        if label == 'Kreirana':
            return RezervacijaStatus.KREIRANA
        else:
            raise NotImplementedError
