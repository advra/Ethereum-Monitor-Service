# Ethereum Monitoring Service

A small service to monitor and track confirmations on-chain. This tracks by creating a table of mined blocks, to avoid chain reorganization we wait for 6 transaction confirmations to consider the data is finalized. The data can then added be added to off-chain db for performacne at scale. 

## How to Run

```
cd into/folder/location
pip install web3
cp settings.json.example settings.json # add your own infura key to this file inplace of demo
python3 monitor.py
```

## Sources: 

- This project began from this script with optimizations in mind: https://docs.infura.io/infura/tutorials/ethereum/monitor-transfers-using-python 
- Optimized query of block to include transactions and avoid double call and hex lookups: https://community.infura.io/t/reading-all-transactions-in-detail-from-a-block/966
