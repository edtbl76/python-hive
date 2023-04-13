from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()

local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()

#
#
# Block 0 <block.Block object at 0x7f41bfb53048>
# timestamp: 2022-01-19 00:00:57.238821
# transactions: []
# current hash: 2e78b3d40ba65c216feab8b60fcdb134bba508bd299edb42301d4ed51e91cedf
# previous hash: 0
# Block 0 <block.Block object at 0x7f41bfb53048>
# timestamp: 2022-01-19 00:00:57.238821
# transactions: []
# current hash: 2e78b3d40ba65c216feab8b60fcdb134bba508bd299edb42301d4ed51e91cedf
# previous hash: 0
# Block 1 <block.Block object at 0x7f41bfb4a048>
# timestamp: 2022-01-19 00:00:57.238860
# transactions: {'sender': 'Alice', 'receiver': 'Bob', 'amount': '50'}
# current hash: ce76a4889707cfc5e8bf454453ec4c5968ed7963d0073d4cbdfdc2e8d783b39d
# previous hash: 2e78b3d40ba65c216feab8b60fcdb134bba508bd299edb42301d4ed51e91cedf
# Block 2 <block.Block object at 0x7f41bfb4a080>
# timestamp: 2022-01-19 00:00:57.238871
# transactions: {'sender': 'Bob', 'receiver': 'Cole', 'amount': '25'}
# current hash: ed8cbeea50899698ed3e79cb2eb52feb9af2b313f685d8e09b6670962d9947ce
# previous hash: ce76a4889707cfc5e8bf454453ec4c5968ed7963d0073d4cbdfdc2e8d783b39d
# Block 3 <block.Block object at 0x7f41bfb4a0b8>
# timestamp: 2022-01-19 00:00:57.238880
# transactions: {'sender': 'Alice', 'receiver': 'Cole', 'amount': '35'}
# current hash: ce3dc420b3b9eddb5881a99b71e256b91917078f026d620224f6fcb2cc9d75a4
# previous hash: ed8cbeea50899698ed3e79cb2eb52feb9af2b313f685d8e09b6670962d9947ce
# Current hash does not equal generated hash
