# Learning with Errors (LWE) Post Quantum Encryption.
# Python implemented by Justin Newman,
# original lesson from Bill Buchanan OBE.

# We will define a public and private key.
# Define a secret value s:

s = 5

# Generate public key. Made up of two vectors A and B
# First we will look at vector A:
# random numbers up to a given prime. We will use 97.

import random, math

# start with a prime number. In live apps, we use a larger q.
q = 97  
list_length = 20 # using 20 in this case.  

# Generate a random vector of numbers
# A = [random.randint(1, q) for _ in range(list_length)]

A = [80,86,19,62,2,83,25,47,20,58,45,15,30,68,4,13,8,6,42,92]
print('A = ', A)

# n integers int mod q

# next we define a number of error values.
# max_e = 4
# e = [random.randint(1, max_e) for _ in range(list_length)]

e = [3,3,4,1,3,3,4,4,1,4,3,3,2,2,3,2,4,4,1,3]


# now define B such that 
# B_i = A_i x (s + e) (mod q)

def compute_b(A, e):
    B = []
    for i in range(list_length):
        B.append((A[i] * s + e[i]) % q)
    return B

B = compute_b(A, e)

print("B = ",B)
print("e = ", e)

# The public key is now (A,B)
# Anyone who wants to send encrypted values will send with A and B

# A =  [80, 86, 19, 62, 2, 83, 25, 47, 20, 58, 45, 15, 30, 68, 4, 13, 8, 6, 42, 92]
# B =  [15, 45, 2, 20, 13, 30, 32, 45, 4, 3, 34, 78, 55, 51, 23, 67, 44, 34, 17, 75]

# Next we have a single bit message (M), we sample A and B to produce:
M = 0

n_samples=4

sample_indexes = set()
while len(sample_indexes) < n_samples:
    sample_indexes.add(random.randint(0, list_length-1))
sample_indexes = list(sample_indexes)

print("Sample indexes: ", sample_indexes)

samples = []
# display the sampled pairs
for x in range(n_samples):
    samples.append((A[sample_indexes[x]], B[sample_indexes[x]]))
print("Samples: ", samples)

# compute u and v

# u = sum of samples from A
# v = sum of samples from B (-q/2 * M)

u = 0
v= 0
for x in range(n_samples):
    u=u+samples[x][0]
    v=v+samples[x][1]

v=v+math.floor(q//2)*M
v = v%q
u = u%q

# encrypted value is then (u,v)
print("Encrypted value: ", u,v)

# to decrypt we take (u,v) and calculate:


# Dec = v - su (mod q)
dec=(v-s*u) % q
if (dec>q/2): # if Dec is greater than q/2, the message is 1
    print("Decrypted Bit: 1")
else: # if Dec is less than q/2, the message is 0
    print("Decrypted Bit: 0")