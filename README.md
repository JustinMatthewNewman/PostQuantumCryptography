# (LWE) Post Quantum Encryption
A bare bones python implementation of the Learning with Errors (LWE) post quantum encryption algorithm. 
LWE provides resistance against quantum computers by using randomly generated matrices over integers modulo a prime number.

LWE relies on the hardness of distinguishing random linear equations from those with added small errors. 


We begin with the following constant values:

A vector length of $'n'$.

A discrete integer secret $'s'$.

A randomly selected prime integer  $'q'$.

We then generate a public key made up of length $n$ vectors A and B.


# Vector A
Each $A_i$ is randomly generated where $A_i$ is less than $q$.
$$A = (A_1, A_2, \ldots, A_i, \ldots, A_n)$$

# Vector e
Each $e_i$ is a small randomly generated integer where $e_i$ is less than a fixed integer much smaller than $q$.

$$e = (e_1, e_2,  \ldots, e_i, \ldots, e_n)$$

# Vector B
Each $B_i$ is computed as follows:
$$B_i \equiv A_i \cdot (s + e_i) \pmod{q}$$

# Random Samples



Next we choose various random indexes $i$ and sample pairs from A and B.

( $A_i$ , $B_i$ ).

We let $z$ denote the sample size.

To encrypt, the random samples are summed separately. 

$$u=\left( \sum_{i=1}^z A_i Samples \right)  \pmod{q} $$

$$v=\left( \sum_{i=1}^z B_i Samples \right) + \left\lfloor \frac{q}{2} \right\rfloor \cdot M \pmod{q} $$


Where $M$ is a single bit to be encrypted.

The single encryped bit is now stored in $(u,v)$.

To decrypt, the I used: v - su (mod q)

Original algorithm invented by Oded Regev.
This python implementation was created by:
Justin Newman.

Based on a lesson by Bill Buchanan OBE.
Contributions are welcome!


