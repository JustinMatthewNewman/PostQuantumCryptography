# (LWE) Post Quantum Encryption
This is a python implementation of the Learning with Errors (LWE) post quantum encryption algorithm. 
LWE provides resistance against quantum computers by using randomly generated matrices over integers modulo a prime number.

# Description:

LWE relies on the hardness of distinguishing random linear equations from those with added small errors. 
It generates a public key made up of a vector A and a vector B.

We begin with a prime integer $q$.
integer size $n$.
integer secret $s$.

# Vector A
$$A = (A_1, A_2, \ldots, A_i, \ldots, A_n)$$
Each $A_i$ is randomly generated where $A_i$ is less than $q$.
# Vector B
$$B_i \equiv A_i \cdot (s + e_i) \pmod{q}$$

# Vector e
$$e = (e_1, e_2,  \ldots, e_i, \ldots, e_n)$$

let $c$ denote the sample size.

To encrypt, random samples are taken from A and B, summed separately and a e_i is added to each element of B. 

$$u=\left( \sum_{i=1}^c sample_(A_i) \right), v=\left( \sum_{i=1}^c sample_(B_i) \right)$$

The ciphertext is the pair of summed values from A and B after -q/2 * M is applied to v, where M is a single bit to be encrypted.

To decrypt, the I used: v - su (mod q)

Original algorithm invented by Oded Regev.
This python implementation was created by:
Justin Newman.

Based on a lesson by Bill Buchanan OBE.
Contributions are welcome!


