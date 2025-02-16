from abc import ABC, abstractmethod

class BaseNetwork(ABC):
    @abstractmethod
    def generate_wallet(self):
        pass

    @abstractmethod
    def save_wallets(self, wallets, filename):
        pass