# Blockchain Messenger
A Python3 approach to build a secure messaging application using blockchain

<h2>Brief Overview</h2>
<p>
  This project was created in 2021 when the government of India updated their Internet Technology Rules. Essentially, the new rules compromised user privacy by requiring companies to disclose information on the sender and contents of private messages. I found that for a messaging appliation to be free from government influence. it had to be decentralised. Blockchains are decentralized networks and their security is governed by the miners. All the data is stored on the blockchain and is protected by asymeteric cryptography. The blockchain messenger allows the
sender of a message to encrypt data using the recievers public key. A reciever can verify the authenticity of a message using its digital certificate, and decrypt the message using their private key. This program is only intented to be a proof of concept for blockchain based messaging, and there are many features to be implemented before this is a usable real-world application.
</p>

<h2>High Level Program Flow</h2>
<p>
  The program flows as follows: <br>
    <ol>
      <li>The sender and reciever generate their public and private keys.</li>
      <li>The sender writes their message and a one time key is generated.</li>
      <li>The message is encrypted using the one time key, and the encrypted message is added to the blockchain (mined).</li>
      <li>The sender digitally signs the message to verify its authenticity.</li>
      <li>Upon verification of the digital signature, the reciever recreates the one time key using their own private key and decrypts the message data.</li>
    </ol>
</p>

<h2>Key Notes + Changes</h2>
<p>
  To create this project, I studied the Bitcoin whitepaper, the Ethereum whitepaper, the Matic whitepaper and CryptoNote 2.0 (outlines the basis for Monero). Using my learnings from these papers, some of which I have implemented in this project, I have the following notes about the current iteration of this project as well as future changes. <br>
  This iteration of a blockchain messenger was designed to run on one machine such that the sender, reciever and mining network all exist on the same machine. For this to be a real-world application the mining network would be distributed across many computers and the sender and reciver would also be independant of one another. <br>
  Further, the aim of this project was to explore the viability of a blockchain based messaging system. To implement a network that is completely anonomous, based on my current understanding of CryptoNote 2.0 it would need to implement one-time ring signatures. <br>
  User privacy and protection are guaranteed by asymetric encryption using Elliptic Curve keys as well as hashing using SHA-256, which are currently thought to be secure as given the current computing power of the world, decrypting the messages or breaking the hashing algorithm would take too much time. However, significant improvements to computing power or changes to how computers work with large numbers might compromise the security of the network. Since all the data is stored on a publically distributed ledger, anyone who has a copy of the blockchain can decrypt the messages in the future if such changes occur. <br>
  While a network with 51% or more of the computing power belonging to honest miners is considered secure as fake transactions cannot be added, the current iteration is secure as there is no monetary benefit. To incentivise people to mine the blocks in a real-world application this could be implemented with a token such that users would pay a small fee for each message that would be given to the miner who mines the block first. However, then the aforementioned concerns about the security of blockchains must be accounted for. 
</p>
