import base58
import hashlib
from mnemonic import Mnemonic
from .base_network import BaseNetwork

class SolanaNetwork(BaseNetwork):
    def __init__(self):
        self.mnemo = Mnemonic("english")

    def generate_wallet(self, num_wallets=1):
        wallets = []
        for _ in range(num_wallets):
            seed_phrase = self.mnemo.generate(strength=128)
            
            seed = self.mnemo.to_seed(seed_phrase)
            
            private_key = seed[:32]
            
            public_key = self._derive_public_key(private_key)
            
            wallet_info = {
                'address': public_key,
                'private_key': base58.b58encode(private_key).decode('utf-8'),
                'seed_phrase': seed_phrase
            }
            wallets.append(wallet_info)
        
        return wallets

    def _derive_public_key(self, private_key):
        public_key_bytes = hashlib.sha256(private_key).digest()[:32]
        return base58.b58encode(public_key_bytes).decode('utf-8')

    def save_wallets(self, wallets, filename='solana_wallets.txt'):
        with open(filename, 'w') as f:
            for wallet in wallets:
                f.write(f"{wallet['address']} | {wallet['private_key']} | {wallet['seed_phrase']}\n")