from web3 import Web3,HTTPProvider
import json

def connect_Blockchain_drug(acc):
    blockchain_address="http://127.0.0.1:8545"
    web3=Web3(HTTPProvider(blockchain_address))
    if(acc==0):
        acc=web3.eth.accounts[0]
    web3.eth.defaultAccount=acc
    artifact_path='../build/contracts/drug.json'
    contract_address="0x50f1728806f5cB3212d18f6b059925E6f552F967"
    with open(artifact_path) as f:
        contract_json=json.load(f)
        contract_abi=contract_json['abi']

    contract=web3.eth.contract(address=contract_address,abi=contract_abi)
    print('connected with blockchain')
    return (contract,web3)

def addLabManufacturer(walletaddr,formula):
    contract,web3=connect_Blockchain_drug(walletaddr)
    tx_hash=contract.functions.addLabManufacturer(walletaddr,formula).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    
    _labmanu,_labform=contract.functions.viewLabManufacturers().call()
    print(_labmanu,_labform)

def addLabFeedback(formula,feed):
    contract,web3=connect_Blockchain_drug(0)

    _lab,_labmanu,_labform=contract.functions.viewLabManufacturers().call()
    formindex=_labform.index(formula)
    print(_labmanu,_labform,formindex)

    tx_hash=contract.functions.addLabFeedback(formindex,feed).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)

    _labfeeds=contract.functions.viewLabFeedback().call()
    print(_labfeeds)


addLabManufacturer('0x64966cfdFdac598B8e8342C23b1AF74E6FD21a31','H2SHS')
addLabFeedback('H2SHS','Working Good')
addLabFeedback('H2SHS','Working Partially')