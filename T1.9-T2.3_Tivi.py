import random
from sre_parse import SPECIAL_CHARS
import string
import unittest
# kun runtest==0 niin silloin testataan play—napilla
# kun runtest==l niin silloin testataan unittest modessa terminaalista
runtest = 0


def generate_password():
    nouns = ['omena', 'dinosaurus', 'pallo', 'paahdin', 'vuohi', 'lohikäärme',
            'vasara', 'sorsa', 'panda', 'puhelin', 'bananas', 'opettaja']

    adjectives = ['unxnen', 'hidas', 'haiseva', 'märkä', 'lihava', 'punaxnen',
                'oranssi', 'keltainen', 'vihreä',
                , 'sunxnen', 'purppura', 'pörroxnen',
                'valkoinen', 'leuhka', 'uljas']

    while True:
        # valitaan satunnaisesti adj ectives listalta
        adjective = random.choice(adjectives)
        # valitaan satunnaisesti nouns listalta
        noun = random.choice(nouns)
        # satunnainen numero väliltä 0 . . . 99
        number = random.randrange(0, 100)
        spacial_char = random.choice(string.punctuation)
        # rakennetaan salasana
        password = adjective + noun + str(number) + SPECIAL_CHARS
        if (runtest == 0):
            print(' Uusi salasanasi on: %s' % password)
        response = input("Haluatko toisen salasanan? Vastaa k tai e ")
        if response == 'e':
            break
        else:
            return password
    if (runtest == 0):
        generate_password()

        # Huom! class nimi pitää olla sama kuin tiedostonnimi
        class test_salasana(unittest.TestCase)
        
        def test_generate_password_success(self):
            actual = len(generate_password())
            expected = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
            print('actual= ', actual)
            self.assertln(actual, expected)

        # asenna python 3 . 11 play—kaupasta niin polut toimii silloin oikein
        # muutoin testaa python oletuskansiossa
        # aseta koodi unittest moodeen jollin runtest =	1
        # testaa komentoriviltä (terminal)
        # avaa View valikosta terminal ikkuna
        # dir (enter)	käskyllä saat katsottua että olet samassa hakemistossa kuin "test salasana.py"
        # python —m unittest test salasana.py
