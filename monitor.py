from web3 import Web3
import time 
import json

f = open ('settings.json')
settings = json.load(f)

print(f"Booting up with api key: {settings['INFURA_API_KEY']}")
print(f"Listening tx processed on: {settings['ACCOUNT_ADDRESS']}")
infura_url = settings['INFURA_API_KEY']
account = settings['ACCOUNT_ADDRESS']

web3 = Web3(Web3.HTTPProvider(infura_url))

def confirmations(tx_hash):
    tx = web3.eth.get_transaction(tx_hash)
    return web3.eth.block_number - tx.blockNumber

def debugTable(table):
    print( "" )
    print( " ---- Confirmations Table ----" )
    for entry in table:
        print(f"     :: { entry } ")
    print( "" )

def watch():
    block = ""
    prevBlock = ""
    txConfirmTable = []
    print(f"length is: {len(txConfirmTable)}") 
    
    while True:
        
        # Note: To optimize double calls with get_block then get_transaction() we can set 
        # SHOW TRANSACTION DETAILS FLAG to true to include all detail in one call
        block = web3.eth.get_block('latest', True)
        if block != prevBlock:
            print("Searching in block " + str(block.number))
            if block and block.transactions: 
                print("total transactions found: " + str(len(block.transactions)))
                for tx in block.transactions: 
                    print(tx)
                    if tx.to != None:
                        if tx.to == account:
                            print("     Transaction found in block {} :".format(block.number))
                            print({
                                "     - hash": tx.hash,
                                "from": tx["from"],
                                "value": web3.fromWei(tx["value"], 'ether')
                                })
                            
                            # create tuple set
                            entry = [ -1, tx ]
                            txConfirmTable.append(entry)
                            print(f"     + Added: { entry }" )  

            # check if first element has data to calculate 
            if len(txConfirmTable) > 1:
                # increment all entries by 1 confirmation
                for entry in txConfirmTable:
                    confirmations  = entry[0]
                    transaction = entry[1]
                    entry[0] += 1
                    print("++++++++++++++++++")
                    print(entry[0])     # confirmations
                    print(entry[1])     # transactions
                    
                # check confirmations and consider finalized when 6 occur
                print("----------------- CHECKING---------------")
                for entry in txConfirmTable:   
                    if entry[0] > 5:
                        txConfirmTable.remove(entry)
                        print(f"     - Removed: { entry }" ) 
                        # upon removal add to the database 
                        
            debugTable(txConfirmTable)

            prevBlock = block 
            
        time.sleep(5)
        # instead of sleep we try do some work here like checking confirmations

watch()
# print(confirmations("0x0d40d60e118e9e1f61c2baa2252cc5f8b8ed491c885ec35db6fd6cfc8589c1a7"))
# If confirmations is 6 then we can finalize it