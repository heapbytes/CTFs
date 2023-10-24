import web3 
from web3.middleware import geth_poa_middleware


'''SOL FILE
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
/**
 * @title SolveMe
 * @author BlueAlder duc.tf
 */
contract SolveMe {
    bool public isSolved = false;
    function solveChallenge() external {
        isSolved = true;
    }
   
}
'''

account_from = {
                "address":"0x9bbB1824338862cF04EE8Aa6E576c99b9C7E2964",
                "private_key":"0x8bda9bf67b767d6a75a77eb109d3ec0813d465b6ae743a330282ef009c7a8479",
                "balance":"2.0 ETH"
    }#The instance for this challenge was destroyed, the private keys won't work anymore

challenge_url = 'https://blockchain-solveme-d0dfb4b964acf39d-eth.2022.ductf.dev/'
contract_address = address = '0x6E4198C61C75D1B4D1cbcd00707aAC7d76867cF8'

abi = [
	{
		"inputs": [],
		"name": "isSolved",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "solveChallenge",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
		
	}
]

w3 = web3.Web3(web3.HTTPProvider(challenge_url))
inc = w3.eth.contract(address=address, abi=abi)

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

#inc.functions.solveChallenge().call() #RETURNS [], true
#print(w3.eth.generate_gas_price())


increment_tx = inc.functions.solveChallenge().buildTransaction(
    {
        'from': account_from['address'],
        'nonce': w3.eth.get_transaction_count(account_from['address']),
           'gasPrice': w3.toWei('20', 'gwei'),
    }
)

tx_create = w3.eth.account.sign_transaction(increment_tx, account_from['private_key'])


tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')


#flag	"DUCTF{muM_1_did_a_blonkchain!}"
