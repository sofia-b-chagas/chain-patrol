# patrol.py
from web3 import Web3

# You can get a free endpoint URL from a service like Infura or Alchemy
INFURA_URL = "https://mainnet.infura.io/v3/7aa73b755e5b4a4491b531ee39d3bb18g" 
# This is a public address for the Ethereum Foundation's wallet
ADDRESS_TO_WATCH = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe"

# Connect to an Ethereum node
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def get_balance():
    if web3.is_connected():
        print("Connection to Ethereum successful!")
        balance_wei = web3.eth.get_balance(ADDRESS_TO_WATCH)
        # Convert the balance from Wei (the smallest unit) to Ether
        balance_ether = web3.from_wei(balance_wei, 'ether')
        print(f"Watching Address: {ADDRESS_TO_WATCH}")
        print(f"Current Balance: {balance_ether:.4f} ETH")
    else:
        print("Failed to connect to Ethereum node.")

if __name__ == "__main__":
    get_balance()