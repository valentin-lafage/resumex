from abc import ABC


class Provider(ABC):

    _instance = None

    def __new__(cls):
        if cls._instance is not None:
            raise RuntimeError(f"An instance of {cls.__name__} already exists")
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        Provider._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise RuntimeError("Provider is empty")
        return cls._instance
