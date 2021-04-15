# IaS-Crypto

## Task 2

The ab_encrypt.py and ab_decrypt.py are not information theoretically secure! To be so, the key must have the same length as the plaintext. So every
letter in the plaintextalphabet is mapped to every letter of the cipher alphabetand vive versa.

Nevertheless they are secure in a weaker sense, since the key needs to be brute forced when uing the CBC Method, when choosing the key in a random manner and
long enough, one could be pretty safe.

**Authenticity**:

Is Not Neccessarily given, to ensure this one have to sign the image/header, which is encrypting a predefined sequence with the own private key.

**Confidentiality**:

Yes, it is encrypted, so no one, exept the ones who have the key, can read the plain message

**Integrity**:  

Not given! You need to create a checksum of content and header that is appended to the header or file and also encrypted, if the receiver then decrypts
the message, he can check the plain text and header against the checksum to see if anything was changed or modified.

**Reliable Delivery**:

There is nothing to say about that, since this is content to another topic! Do Alice and Bob have a reliable connection via TCP? Or do they use post-pigeons
which are shot by Evil Erna?
