import coolcalc as nc


def test_add():
    assert nc.calculate('5+5') == '10'


def test_sub():
    assert nc.calculate('12-3') == '9'


def test_mult():
    assert nc.calculate('2*3') == '6'


def test_div():
    assert nc.calculate('4/5') == '0.8'


def test_bracket():
    assert nc.calculate('2*(2+2)') == '8'


def test_fackt():
    assert nc.calculate('1+((3-2)+(5-3))!!') == '721'


def test_num_sys():
    assert nc.calculate('bin587') == '1001001011'


def test_log():
    assert nc.calculate('log10') == '1'
