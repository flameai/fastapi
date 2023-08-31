from abc import ABC, abstractmethod


class BaseFastAPIApp(ABC):
    @abstractmethod
    def startup(self):
        pass
