# Ethereum Monitoring Service

A small service to monitor and track confirmations on-chain. This tracks by creating a table of mined blocks, to avoid chain reorganization we wait for 6 transaction confirmations to consider the data is finalized. The data can then added be added to off-chain db for performacne at scale. This example monitors transactions to the WETH address `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2`.

## How to Run
Note: After copying settings.json, replace `INFURA_API_KEY` with your own key
```
taro@pc: cd into/folder/location
taro@pc: pip install web3
taro@pc: cp settings.json.example settings.json 
taro@pc: python3 monitor.py
```

## Sources: 

- This project began from this script with optimizations in mind: https://docs.infura.io/infura/tutorials/ethereum/monitor-transfers-using-python 
- Optimized query of block to include transactions and avoid double call and hex lookups: https://community.infura.io/t/reading-all-transactions-in-detail-from-a-block/966
