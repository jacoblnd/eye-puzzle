"""
Simple Deck Cipher:

Consider a 12-character Plaintext (PT) alphabet: ACDEHILMNORS
These characters were chosen since they seem to form words well.

Add some characters which can only appear in the ciphertext (CT): XYZ and call all characters
together a 15-card "deck" where each character (synonymous with symbol) is a card.

Construct the identity deck which is a specific order of the cards/symbols:
ZACDEHILMNORSXY

A CT-symbol-only card (Z) is chosen as the first card to ensure that there exists no way for a
PT symbol to result in a double in the ciphertext.
This is not fully explained now but will be evident later.

The identity deck: index mapping is:
Z: 0
A: 1
C: 2
etc...
X: 13
Y: 14

A permutation or "mapping" function is created for each PT symbol which represents a deterministic
shuffle of the deck where each old position of a card in the deck moves to a new position in the
deck.
If we take the indexes of cards in the identity deck as a "starting" position then the
permutation functions can be represented as a another deck of cards picked in some order from the
full deck.
Aside: It follows that the identity deck is also a mapping/permutation function which is special:
it maps all cards to the location they are already in.

So, a permutation or mapping function is equivalent to a deck which is also equivalent to a list
of symbols in some order and they all are based on the starting position of the identity deck.

These lists of symbols can be made to resemble words for fun and any remaining symbols not used
in the word can be picked in any order to fill the rest of the deck.
For simplicity, we'll set the remaining symbols to their order in the identity deck.

Across all mapping functions, we need to ensure each PT symbol appears on the top of the
deck (index zero) once and only once so we create the deck associated with a given symbol such that
it begins with that symbol.
The reason for needing to appear on the top of the deck once is not explained here but will be
evident later.

Consider the permutation function for the PT symbol "A" represented as the list of symbols in
the order:

ACRESZDHILMNOXY

"ACRES" is just a fun word. The rest of the characters are in identity deck order.
The index mapping for each character is:
A: 0
C: 1
R: 2
...
X: 13
Y: 14

The permutation function derived from the identity deck which is represented by this order of
symbols is:

(permutation deck index -> identity deck index)
0: 1 (permutation deck symbol 0 is A whereas identity deck symbol 1 is A)
1: 2
2: 11
3: 4
...
12: 10
13: 13
14: 14

If we assume permutation deck index order, we can collapse this representation to a simple list
of ints:
[1, 2, 11, 4, ... 10, 13, 14]

Therefore, given:
1. An identity deck containing PT and CT symbols.
2. A map of PT symbols to their corresponding permutation functions represented as a
    specifically-ordered list of symbols.

We can construct this basic deck cipher and encipher / decipher a message.
"""

from ciphers.simple_cipher import SimpleDeckCipher
from ciphers.util import print_cipher_decipher

"""The 15-symbol deck containing 12 PT symbols:"""
identity_deck = "ZACDEHILMNORSXY"
permutation_decks = {
    "A": "ACRESZDHILMNOXY",
    "C": "CHLORINEZADMSXY",
    "D": "DENIALZCHMORSXY",
    "E": "ECHOZADILMNRSXY",
    "H": "HELIOSZACDMNRXY",
    "I": "IDOLSZACEHMNRXY",
    "L": "LORDSZACEHIMNXY",
    "M": "MAZESCDHILNORXY",
    "N": "NORDICZAEHLMSXY",
    "O": "ORCHIDZAELMNSXY",
    "R": "RANCIDZEHLMOSXY",
    "S": "SCAREDZHILMNOXY",
}
simple_cipher = SimpleDeckCipher.from_decks(identity_deck, permutation_decks)

print_cipher_decipher(simple_cipher, "SHARDSACROSSMORDORACROSSMORDORACROSSMORDOR")
"""
Ciphertext:              SDERLIODLOMAOERANDMZNMLHMCEHRZLSRLNALOCAES
Decrypted Ciphertext:    SHARDSACROSSMORDORACROSSMORDORACROSSMORDOR
"""
