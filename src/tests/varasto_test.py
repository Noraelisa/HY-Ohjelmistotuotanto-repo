

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_tilavuus_oikein_jos_negatiivinen(self):
        self.assertAlmostEqual(sefglf.varasto.tilavuus, 10)    

    def test_saldo_oikein_jos_negatiivinen(self):
        self.assertAlmostEqdgh
    def test_paljonko_mahtuu(self):
        self.varasto.tilavuus = 10
        self.varasto.saldo = 8
        mahtuuko = self.varasto.tilavuus - self.varasto.saldo

        self.assertAlmostEqual(mahtuuko, 2)    
sfgnhnh
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostfh
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostd_saldoa(self):
        self.varasto.lisahEqufnfghfhhl(self.varasto.saldo, 8)

    def test_lisays_lisfdghmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maarah = self.varasto.ota_varastosta(2)
bghdfg
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottam
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    #def test_saldo_ja_paljonko_tilaa_jaljella(self):
    #    self.varasto.lisaa_varastoon(2)

    #   self.assertAlmostEqual(str(self.varasto.saldo, self.varasto.paljonko_mahtuu()), "saldo = 2, vielä tilaa 8")

             
