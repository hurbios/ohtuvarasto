import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        

    def test_init_varasto_tilavuudella_alle_0(self):
        uusi_varasto = Varasto(-1.0, -1.0)
        self.assertAlmostEqual(uusi_varasto.tilavuus, 0)
        self.assertAlmostEqual(uusi_varasto.saldo, 0)
 
    def test_init_varasto_saldo_suurempi_kuin_tilavuus(self):
        uusi_varasto = Varasto(1.0, 2.0)
        self.assertAlmostEqual(uusi_varasto.tilavuus, 1)
        self.assertAlmostEqual(uusi_varasto.saldo, 1)
 
    def test_lisaa_varastoon_enemman_kuin_mahtuu(self):
        uusi_varasto = Varasto(2.0, 1.0)

        uusi_varasto.lisaa_varastoon(uusi_varasto.paljonko_mahtuu()+1)
        self.assertAlmostEqual(uusi_varasto.saldo, uusi_varasto.tilavuus)
        
    def test_ota_varastosta_vaarin(self):
        alku_saldo = 1.0
        uusi_varasto = Varasto(2.0, alku_saldo)

        uusi_varasto.ota_varastosta(-1)
        self.assertAlmostEqual(uusi_varasto.saldo, alku_saldo)
        uusi_varasto.ota_varastosta(20)
        self.assertAlmostEqual(uusi_varasto.saldo, 0)

    def test_tostring(self):
        uusi_varasto = Varasto(1.0, 1.0)
        self.assertEqual(str(uusi_varasto), 'saldo = 1.0, vielä tilaa 0.0')
