
from abc import abstractmethod, ABC


class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self._jaratszam = jaratszam
        self._celallomas = celallomas
        self._jegyar = jegyar

    @property
    def jaratszam(self):
        return self._jaratszam

    @property
    def celallomas(self):
        return self._celallomas

    @property
    def jegyar(self):
        return self._jegyar

    @abstractmethod
    def jarat_info(self):
        pass