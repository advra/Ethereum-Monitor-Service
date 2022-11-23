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

def debugTable(table, allEntries=False):
    print( "" )
    print( " ---- Confirmations Table ----" )
    for entry in table:
        if allEntries:
            print(f"     :: { entry } ")
        else:
            print(f"     :: { entry[0] }, {entry[1].hash} ")
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
                    entry[0] += 1
                    print("++++++++++++++++++")
                    print(entry[0])     # confirmations
                    print(entry[1])     # transactions
                    
                    if entry[0] > 5:
                        txConfirmTable.remove(entry)
                        print(f"     - Removed: { entry }" ) 
                        # upon removal add to the database 
                        
            debugTable(txConfirmTable)

            prevBlock = block 
            
        time.sleep(5)

watch()