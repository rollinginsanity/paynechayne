from  paynechain.block import BlockChain
from pathlib import Path
import pickle

bc_file = Path('blockchain')
if bc_file.is_file():
    with open('blockchain', 'rb') as bc_handle:
        bc = pickle.load(bc_handle)
else:
    bc = BlockChain()
    bc.make_genesis_block()

data = input("Add some data to le blockchain: ")

bc.make_next_block(data)

with open('blockchain', 'wb') as bc_write_handle:
    pickle.dump(bc, bc_write_handle)