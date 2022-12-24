import password_1


def test_password_len():
    assert password_1.check('fff') == False
    assert password_1.check('ffffff') == False
    assert password_1.check('ffffffff5') == True

def test_password_only_digit():
    assert password_1.check('555555555') == False
    assert password_1.check('555555555f') == True

def test_password_only_alpha():
    assert password_1.check('fffffffff') == False
    assert password_1.check('fffffffff5') == True

def test_password_easy():
    assert password_1.check('password2002') == False
    assert password_1.check('PasSwOrd2002') == False
    assert password_1.check('PASSWORD2002') == False
