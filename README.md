# Ethereum Monitoring Service

A small service to monitor and track confirmations on-chain. This tracks by creating a table of mined blocks, to avoid chain reorganization we wait for 6 transaction confirmations to consider the data is finalized. The data can then added be added to off-chain db for performacne at scale. 

## How to Run

```
cd into/folder/location
pip install web3
python3 monitor.py
```