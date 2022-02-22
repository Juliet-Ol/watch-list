from distutils.debug import DEBUG
from msilib.schema import Class


class Config:
    '''
    General configuration parent class
    '''

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True