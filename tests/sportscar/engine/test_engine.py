from pytest import mark

@mark.smoke
@mark.engine # find it running pytest -m engine
def test_engine_functions_as_expected():
    assert True