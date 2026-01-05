"""A smaller, more-basic implementation of the hypothetical 83-card deck cipher.
I'm sure some or much of this will not be fully representative of the
cipher theorized by Lymm and others but it should at least be fun to make.

For background on the 83-card deck cipher, terminology, and a whole lot more, see Lymm's wiki:
https://github.com/Lymm37/eye-messages/wiki

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

class DeckCipher:
    identity_deck: str
    permutation_maps: dict[str, list[int]]

    def __init__(self, identity_deck: str, permutation_maps: dict[str, list[int]]):
        self.identity_deck = identity_deck
        self.permutation_maps = permutation_maps

    @staticmethod
    def from_decks(
        identity_deck: str,
        permutation_decks: dict[str, str]
    ) -> DeckCipher:
        # Derive permutation index lists for each permutation deck.
        permutation_maps = {}
        for pt_symbol, perm_deck in permutation_decks.items():
            permutation_list = []
            # Find the corresponding identity index for each symbol
            # and add it to the permutation list.
            for permutation_symbol in perm_deck:
                identity_deck_index = identity_deck.index(permutation_symbol)
                permutation_list.append(identity_deck_index)
            permutation_maps[pt_symbol] = permutation_list
        return DeckCipher(identity_deck, permutation_maps)

    def map_state(self, state: str, pt_symbol: str) -> str:
        new_state = ""
        # Find the permutation function associated with this pt symbol.
        permutation_map = self.permutation_maps[pt_symbol]
        for permutation_index in permutation_map:
            new_state += state[permutation_index]
        return new_state


    def encipher(self, plaintext: str) -> str:
        # Assume starting state is identity_deck
        deck_state = self.identity_deck
        ciphertext = ""
        for pt_symbol in plaintext:
            # Update state given the pt symbol permutation function and get ct symbol which
            # is the top of the deck.
            deck_state = self.map_state(deck_state, pt_symbol)
            ct_symbol = deck_state[0]
            ciphertext += ct_symbol
        return ciphertext

    def decipher(self, ciphertext: str) -> str:
        # Assume starting state is identity_deck
        deck_state = self.identity_deck
        plaintext = ""
        for ct_symbol in ciphertext:
            ct_index = deck_state.index(ct_symbol)
            identity_symbol = self.identity_deck[ct_index]
            plaintext += identity_symbol
            deck_state = self.map_state(deck_state, identity_symbol)
        return plaintext

identity_deck = "ZACDEHILMNORSXY"
permutation_decks = {
    "A": "ACRESZDHILMNOXY",
    "C": "CHLORINEZADMSXY",
    "D": "DENIALZCHMORSXY",
    "E": "ECHOZADILMNRSXY",
    "H": "HELIOSZACDMNRXY"
}
simple_cipher = DeckCipher.from_decks(identity_deck, permutation_decks)

def cipher_decipher(cipher, plaintext: str):
    ciphertext = cipher.encipher(plaintext)
    print("Ciphertext: ", ciphertext)
    print("Decrypted Ciphertext: ", cipher.decipher(ciphertext))

cipher_decipher(simple_cipher, "ACEDHEEDHEEDHEEDHEEDHEED")
