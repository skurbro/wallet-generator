from eth_account import Account
from mnemonic import Mnemonic
from .base_network import BaseNetwork

class EVMNetwork(BaseNetwork):
    def __init__(self):
        self.mnemo = Mnemonic("english")

    def generate_wallet(self, num_wallets=1):
        wallets = []
        for _ in range(num_wallets):
            seed_phrase = self.mnemo.generate(strength=128)
            
            account = Account.create(seed_phrase)
            
            wallet_info = {
                'address': account.address,
                'private_key': account.key.hex(),
                'seed_phrase': seed_phrase
            }
            wallets.append(wallet_info)
        
        return wallets

    def save_wallets(self, wallets, filename='evm_wallets.txt'):
        with open(filename, 'w') as f:
            for wallet in wallets:
                f.write(f"{wallet['address']} | {wallet['private_key']} | {wallet['seed_phrase']}\n")