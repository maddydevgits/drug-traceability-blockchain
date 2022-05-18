from web3 import Web3,HTTPProvider
import json

def connect_Blockchain_register(acc):
    blockchain_address="http://127.0.0.1:8545"
    web3=Web3(HTTPProvider(blockchain_address))
    if(acc==0):
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='../build/contracts/register.json'
    contract_address="0x02E5556090ba5e6ab9Ee89b5150183E960eed4Eb"
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
    print('connected with blockchain')
    return (contract,web3)

def testUser(name,role,walletaddr,password):
    contract,web3=connect_Blockchain_register(walletaddr)
    tx_hash=contract.functions.registerUser(walletaddr,password,name,role).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    
    state=contract.functions.loginUser(walletaddr,password).call()
    print(state)

# # Lab
# testUser('Madhu Lab',1,'0xCf43ae58dCd8893e4C9671f51fa898ecC57b6362',1234)

# # Manufacturer
# testUser('Madhu Manufacturer',2,'0x0F07fd4ca590F510121A3a01D1354dD7659CCdcd',1234)

# # WareHouse M
# testUser('Madhu WareHouse M',3,'0x14a941428cFEfD644587d70348dfE79c49Da3cF4',1234)

# # Transportation
# testUser('Madhu Transportation',4,'0x921eC0a3c3c8008Fe2E254E6e798e63C286c1d36',1234)

# # WareHouse T
# testUser('Madhu WareHouse T',5,'0xc42A1b2f6886E27af013BfFC85098BC398552D95',1234)

# # Hospitals
# testUser('Madhu Hospitals',6,'0x1eEC74A4fF31D7FbaAC277B298Ba548888747341',1234)

# # Retailers
# testUser('Madhu Retailers',7,'0xaD395A15Bfd1492f005bF9B8C6d25304e292C498',1234)

# final test

contract,web3=connect_Blockchain_register('0x957DA269f07bef529168E1be133C7e47dE154372')
_users,_passwords,_roles,_names=contract.functions.viewUsers().call()
print(_users,_passwords,_roles,_names)