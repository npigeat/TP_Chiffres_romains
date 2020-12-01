
import Chiffre_romains as m

def test_addition():
    assert m.calc_rom("+", 'I', 'II') == 'III'
    assert m.calc_rom("+", 'II', 'II') == 'IV'
    assert m.calc_rom("+", 'XLII', 'XXVI') == 'LXVIII'
    assert m.calc_rom("+", 'XLII', 'MMMMMMM') =='ERROR'


def test_mul():
    assert m.calc_rom("*", 'II', 'III') == 'VI'
    assert m.calc_rom("*", 'XII', 'III') == 'XXXVI'
    assert m.calc_rom('*', 'XLII', 'XXVI')=='MXCII'
    assert m.calc_rom('*', 'A', 'B')=='ERROR'

def test_sub():
    assert m.calc_rom("-", 'II', 'III') == 'ERROR'
    assert m.calc_rom("-", 'XII', 'III') == 'IX'
    assert m.calc_rom('-', 'XLII', 'XXVI') == 'XVI'
    assert m.calc_rom('-', 'A', 'B') == 'ERROR'

def test_div():
    assert m.calc_rom("/", 'II', 'III') == 'ERROR'
    assert m.calc_rom("/", 'XII', 'III') == 'IV'
    assert m.calc_rom('/', 'XLII', 'XXVI') == 'I'
    assert m.calc_rom('/', 'A', 'B') == 'ERROR'