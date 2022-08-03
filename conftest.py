def pytest_addoption(parser):
    parser.addoption("--url", action="store", default=False)


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.url
    if 'base_url' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("base_url", [option_value])