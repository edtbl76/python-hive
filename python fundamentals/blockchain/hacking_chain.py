from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

my_blockchain = Blockchain()
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()
my_blockchain.chain[1].transactions = "fake_transactions"

my_blockchain.validate_chain()


# OUTPUT
#
# Block 0 <block.Block object at 0x7fcaa1c1ce80>
# timestamp: 2022-01-18 23:41:01.655990
# transactions: {}
# current hash: 61ba96a7015eda198051371e000454561aefe12707ad8413c9e83bc216e51555
# previous hash: 0
# Block 1 <block.Block object at 0x7fcaa1c1ceb8>
# timestamp: 2022-01-18 23:41:01.656016
# transactions: [{'amount': '30', 'sender': 'alice', 'receiver': 'bob'}, {'amount': '55', 'sender': 'bob', 'receiver': 'alice'}]
# current hash: 757c9c3ca209c2858bc22337097958c0300a68f3c64a49c6bb7551bd1fa7bed1
# previous hash: 61ba96a7015eda198051371e000454561aefe12707ad8413c9e83bc216e51555
# The current hash of the block does not equal the generated hash of the block.