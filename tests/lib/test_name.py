import name


def test_name_supplied():
    assert(name.display('robert') == 'robert')


def test_name_empty():
    assert(name.display('') == 'there')


def test_name_missing():
    assert (name.display(None) == 'there')
