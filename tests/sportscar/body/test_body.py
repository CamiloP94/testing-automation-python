from pytest import mark

@mark.smoke
@mark.body
@mark.ui
def test_body_functions_as_expected(foo):
    assert True