import time
from pytest import mark


@mark.parallel
def test_result_1_completes_as_expected():
    time.sleep(5)
    print("Result 1 has completed")


@mark.parallel
def test_result_2_completes_as_expected():
    time.sleep(5)
    print("Result 2 has completed")


@mark.parallel
def test_result_3_completes_as_expected():
    time.sleep(5)
    print("Result 3 has completed")


@mark.parallel
def test_result_4_completes_as_expected():
    time.sleep(5)
    print("Result 4 has completed")


@mark.parallel
def test_result_5_completes_as_expected():
    time.sleep(5)
    print("Result 5 has completed")


@mark.parallel
def test_result_6_completes_as_expected():
    time.sleep(5)
    print("Result 6 has completed")


@mark.parallel
def test_result_7_completes_as_expected():
    time.sleep(5)
    print("Result 7 has completed")


@mark.parallel
def test_result_8_completes_as_expected():
    time.sleep(5)
    print("Result 8 has completed")
