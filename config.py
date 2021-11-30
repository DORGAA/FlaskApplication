

class DevConfig():
    """
    Developement configs
    """
    DEBUG = True


class ProdConfig():
    """
    Production configs
    """
    DEBUG = False


class TestConfig():
    """
    Testing configs
    """


appConfig = {

    'development': DevConfig,
    'production': ProdConfig,
    'Testing': TestConfig

}

