from pytest import fixture
import json
import os
from config import Config

data_path = os.getcwd()+'/tests/data-driven/test_data.json'


@fixture(scope='function')
def foo():
    print('pass')
    return True


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run tests against"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

# the parameters are in string beacause i dont wanted to isnstall webdriver


@fixture(params=['webdriver.Chrome', 'webdriver.Firefox', 'webdriver.Edge'])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


@fixture(params=load_test_data(data_path))
def tv_brand_from_fixture(request):
    data = request.param
    return data
