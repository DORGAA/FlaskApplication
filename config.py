

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
    TESTING = True


appConfig = {

    'development': DevConfig,
    'production': ProdConfig,
    'Testing': TestConfig,
    'default': DevConfig

}

