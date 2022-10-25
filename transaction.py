import os
import constants
import time

def buy_eth(w3, account):
    chain_name = os.environ.get("CHAIN_NAME", "GOERLI")
    chain = constants.CHAINS[chain_name]

    abi = open('IUniswapV2Router.json', 'r')


    uniswap_contract = w3.eth.contract(address=chain["UNISWAP_ADDRESS"], abi=abi)

    # Grab the unixtime in seconds
    timestamp = int(time.time())
    deadline = timestamp + constants.DEADLINE_MINUTES * constants.MINUTE_IN_SECONDS

    # function swapExactTokensForTokens(
    #   uint amountIn,
    #   uint amountOutMin,
    #   address[] calldata path,
    #   address to,
    #   uint deadline
    # ) external returns (uint[] memory amounts);

    uniswap_contract.functions.swapExactTokensForTokens(
        constants.AMOUNT_IN,
        constants.AMOUNT_OUT_MIN,
        [chain["USDC_ADDRESS"], chain["WETH_ADDRESS"]],
        account.address,
        deadline
    )