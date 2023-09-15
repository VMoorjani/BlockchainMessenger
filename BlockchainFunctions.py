import hashlib
from datetime import datetime
from datetime import timedelta
genesisData = (datetime.utcnow(), '-----', 0, 'genesisHash', 'genesisMessage')
difficulty = 12

class Block:
    """
    Class that defines what a block on the blockchain looks like
    """
    
    def __init__(self, timestamp, lastHash, nonce, hashValue, message):
        """
        Constructor method for the Block class. takes in a string as the timestamp, a string for the hashValue for the previous
        block on the blockchain, an integer for the nonce value, the hashed data, as well as the message. 
        
        Returns an object of the Block class. 
        """
        self.timestamp = timestamp
        self.lastHash = lastHash
        self.nonce = nonce
        self.difficulty = difficulty
        self.hashValue = hashValue
        self.message = message
        
    def __eq__(self, other):
        """
        Method to check if 2 blocks have the same data. Most often used for checking if a block is the genesis block or not. 
        """
        if (isinstance(other, Block)):
            return (self.message == other.message and self.lastHash == other.lastHash 
                    and self.timestamp == other.timestamp and self.hashValue == other.hashValue)
        return false
    
    def genesis():
        """
        Returns an object of the Block class using the genesis data
        """
        genesisBlock = Block(genesisData[0],genesisData[1],genesisData[2],genesisData[3],genesisData[4])
        
        return(genesisBlock)
    
    def mineBlock(lastBlock, message): 
        """
        Hashes the block using the global difficulty. Sets the timestamp as the current timestamp based on UTC time. Hashes the
        message to ensure all the messages are of the same size. 
        
        Uses SHA-256 for all hashing functions. 
        
        Returns an object of the block class using the above data. 
        """
        nonce = 0
        timestamp = datetime.utcnow()
        message = cryptoHash(message)
        hashInput = str(timestamp)+lastBlock.hashValue+message+str(nonce)
        
        while cryptoHash(hashInput)[0:difficulty] != "0"*difficulty:
            nonce +=1
            hashInput = str(timestamp)+lastBlock.hashValue+message+str(nonce)
        
        hashValue = cryptoHash(hashInput)
        
        return(Block(timestamp, lastBlock.hashValue, nonce, hashValue, message))
    
class Blockchain:
    """
    Class that defines a chain for the blockchain. 
    """
    
    def __init__(self):
        """
        Constructor method for the Blockchain class. The object has only 1 attribute, its chain. The chain is a list with 1 
        item. The first item is the genesis block. 
        """
        self.chain = [Block.genesis()]
        
    def addBlock(self,message):
        """
        Appends a block to the blockchain. Takes in an object of the Blockchain class as well as the message of the block. 
        Calls the mineblock function with the given message and the last element in the chain. 
        
        After the block has been added to the chain, the time difference between the last block and second last block in the 
        chain. If the time difference is more than 4 seconds, then the difficulty is decreased by 1. Else the difficulty is
        increased. 
        
        The difficulty change does not occour of the second last block is the genesis block. 
        """
        
        global difficulty
        newBlock = Block.mineBlock(self.chain[-1], message)
        
        self.chain.append(newBlock)
        
        timeDifference = self.chain[-1].timestamp - self.chain[-2].timestamp
        
        if timeDifference > timedelta(0,4) and self.chain[-2] != Block.genesis():
            difficulty = difficulty - 1
            print(f'Difficulty has been decreased by 1 and is now {difficulty}')
        elif timeDifference < timedelta(0,4):
            difficulty = difficulty + 1
            print(f'Difficulty has been increased by 1 and is now {difficulty}')
        
    def isValidChain(chain):
        """
        Checks if an incoming chain is valid or not. A chain is only valid if it starts with the genesis block, all the 
        values for the last hash match the hashes of the previous block (without including the genesis block) and if
        all the hash values are matching. 
        """
        if Block.genesis() != chain[0]:  ## Is the first block the genesis block
            return (False)
        
        for i in range(1, len(chain)):  ##Are all the last hash values matching
            if (chain[i].lastHash != chain[i-1].hashValue) :
                return (False)
            
        for i in range(1, len(chain)): #Do all the hashes match. I.E has the data been changed
            hashCheck = str(chain[i].timestamp)+chain[i-1].hashValue + chain[i].message +str(chain[i].nonce)
            if cryptoHash(hashCheck) != chain[i].hashValue:
                return(False)
            
        return (True) ##If none of the checks are failed, return true
    
    def replaceChain(self,newChain):
        """
        If an incoming chain is longer than the current chain and it is valid, the current chain is replaced by the new 
        chain. 
        """
        if len(newChain) <= len(self.chain): ##If chain is smaller, automatically rejected
            return(False)
        else:
            if not Blockchain.isValidChain(newChain):  ## If chain is not smaller, but is not valid, is also rejected
                return(False)
            else:  ## If the new chain is longer and is valid, replaces the other chain
                self.chain = newChain
                return(True)        

def cryptoHash(message):
    """
    Uses hashlib to hash an incoming string using SHA-256. If the incoming string is not encoded, then it is encoded using 
    UTF-8 encoding. 
    """
    hasher = hashlib.new('sha256')
    
    if not isinstance(message, bytes):
        message = bytes(message.encode('UTF-8'))
    hasher.update(message)
    
    hashValue = ''
    for digit in hasher.hexdigest():
        hashValue = hashValue+("{0:08b}".format(int(digit, 16)))
    
    return(hashValue)
