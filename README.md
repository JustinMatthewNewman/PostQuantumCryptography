# Learning with Errors (LWE) Post Quantum Encryption
This is a python implementation of the Learning with Errors (LWE) post quantum encryption algorithm. 
LWE provides resistance against quantum computers by using randomly generated matrices over integers modulo a prime number.

# Description:

LWE relies on the hardness of distinguishing random linear equations from those with added small errors. 

It generates a public key made up of a matrix A and a vector B.
To encrypt, random samples are taken from A and B, summed separately and a small error is added to B. 
The ciphertext is the pair of summed values from A and B.

To decrypt, the decryptor uses the secret key to remove A's influence from B, 
leaving just the small error values that cryptographically hide the message.

Original algorithm invented by Oded Regev.
This python implementation was created by:
Justin Newman

Based on a lesson by Bill Buchanan OBE
Contributions are welcome!
