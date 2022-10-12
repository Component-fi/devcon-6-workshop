import os
import constants
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.middleware import construct_sign_and_send_raw_middleware

# Open file
def web3_init():
    chain_name = os.environ.get("CHAIN_NAME", "GOERLI")
    chain = constants.CHAINS[chain_name]

    # Connect to an RPC provider
    w3 = Web3(Web3.HTTPProvider(chain['PROVIDER']))

    # Adds compatibility with goerli
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)


    private_key = os.environ.get("PRIVATE_KEY")
    assert private_key is not None, "You must set PRIVATE_KEY environment variable"
    assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"

    account: LocalAccount = Account.from_key(private_key)
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))

    return w3, account