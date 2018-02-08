from  paynechain.block import BlockChain
from pathlib import Path
import pickle

bc_file = Path('blockchain')
if bc_file.is_file():
    with open('blockchain', 'rb') as bc_handle:
        bc = pickle.load(bc_handle)

        for block in bc.blockchain:
            print(block.index)
            print(block.timestamp)
            print(block.data)
            print(block.previous_hash)

else:
    print("No blockchain found")
