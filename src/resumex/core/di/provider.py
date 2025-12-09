from abc import ABC


class Provider(ABC):

    instance = None

    def __new__(cls):
        if cls.instance is not None:
            raise RuntimeError(f"An instance of {cls.__name__} already exists")
        cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        Provider.instance = self

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            raise RuntimeError("Provider is empty")
        return cls.instance
