# Learning with Errors (LWE) Post Quantum Encryption
This is a python implementation of the Learning with Errors (LWE) post quantum encryption algorithm. 
LWE provides resistance against quantum computers by using randomly generated matrices over integers modulo a prime number.

# Description:

LWE relies on the hardness of distinguishing random linear equations from those with added small errors. 

It generates a public key made up of a matrix A and a vector B.

# Vector A
`list of Random ints no greater than prime number 'q' with a fixed length.`
# Vector B
`B_i = A_i x (s + e_i) (mod q)`
# Error Vector e
`e = small random error values with same numner of entries as vector A`



To encrypt, random samples are taken from A and B, summed separately and a e_i is added to each element of B. 

The ciphertext is the pair of summed values from A and B after -q/2 * M is applied to v, where M is a single bit to be encrypted.

To decrypt, the I used: v - su (mod q)

Original algorithm invented by Oded Regev.
This python implementation was created by:
Justin Newman

Based on a lesson by Bill Buchanan OBE
Contributions are welcome!

**The Cauchy-Schwarz Inequality**
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$
