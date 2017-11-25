from lib import name


def test_name_supplied():
    assert(name.display_name('robert') == 'robert')


def test_name_empty():
    assert(name.display_name('') == 'there')


def test_name_missing():
    assert (name.display_name(None) == 'there')
