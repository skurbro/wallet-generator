from networks.solana_network import SolanaNetwork
from networks.evm_network import EVMNetwork

TELEGRAM_CHANNEL = "https://t.me/agnostic_dao"
TELEGRAM_ACCOUNT = "https://t.me/skurbro"

def main():
    print(r"""



 █████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗████████╗██╗ ██████╗
██╔══██╗██╔════╝ ████╗  ██║██╔═══██╗██╔════╝╚══██╔══╝██║██╔════╝
███████║██║  ███╗██╔██╗ ██║██║   ██║███████╗   ██║   ██║██║     
██╔══██║██║   ██║██║╚██╗██║██║   ██║╚════██║   ██║   ██║██║     
██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████║   ██║   ██║╚██████╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝ ╚═════╝
                                                                
          
                                                 

""")
    
    print(f"Telegram Channel: {TELEGRAM_CHANNEL}")
    print(f"Telegram Account: {TELEGRAM_ACCOUNT}")
    print("\nCrypto Wallet Generator")
    print("1. Solana Network")
    print("2. EVM Network")
    
    try:
        network_choice = input("Select network (1/2): ")
        num_wallets = int(input("Enter number of wallets to generate: "))

        if network_choice == '1':
            network = SolanaNetwork()
            filename = 'solana_wallets.txt'
        elif network_choice == '2':
            network = EVMNetwork()
            filename = 'evm_wallets.txt'
        else:
            print("Invalid network selection!")
            return

        wallets = network.generate_wallet(num_wallets)
        network.save_wallets(wallets, filename)
        
        print(f"\n{num_wallets} wallets generated and saved to {filename}")
        print(f"\nJoin our Telegram community:")
        print(f"Channel: {TELEGRAM_CHANNEL}")
        print(f"Creator: {TELEGRAM_ACCOUNT}")
    
    except ValueError:
        print("Please enter a valid number of wallets.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()