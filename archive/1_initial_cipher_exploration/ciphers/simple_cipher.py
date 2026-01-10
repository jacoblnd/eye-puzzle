"""A smaller, more-basic implementation of the hypothetical 83-card deck cipher.
I'm sure some or much of this will not be fully representative of the
cipher theorized by Lymm and others but it should at least be fun to make.

For background on the 83-card deck cipher, terminology, and a whole lot more, see Lymm's wiki:
https://github.com/Lymm37/eye-messages/wiki
"""

class SimpleDeckCipher:
    identity_deck: str
    permutation_maps: dict[str, list[int]]

    def __init__(self, identity_deck: str, permutation_maps: dict[str, list[int]]):
        self.identity_deck = identity_deck
        self.permutation_maps = permutation_maps

    @staticmethod
    def from_decks(
        identity_deck: str,
        permutation_decks: dict[str, str]
    ) -> SimpleDeckCipher:
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
        return SimpleDeckCipher(identity_deck, permutation_maps)

    def map_state(self, state: str, pt_symbol: str) -> str:
        new_state = ""
        # Find the permutation function associated with this PT symbol.
        permutation_map = self.permutation_maps[pt_symbol]
        for permutation_index in permutation_map:
            # Apply the permutation against each index of the state to get the new
            # state.
            new_state += state[permutation_index]
        return new_state

    def encipher(self, plaintext: str) -> str:
        # Assume starting state is identity_deck.
        deck_state = self.identity_deck
        ciphertext = ""
        for pt_symbol in plaintext:
            # Update state given the pt symbol permutation function and get CT symbol which
            # is the top of the deck.
            deck_state = self.map_state(deck_state, pt_symbol)
            ct_symbol = deck_state[0]
            ciphertext += ct_symbol
        return ciphertext

    def decipher(self, ciphertext: str) -> str:
        # Assume starting state is identity_deck.
        deck_state = self.identity_deck
        plaintext = ""
        for ct_symbol in ciphertext:
            ct_index = deck_state.index(ct_symbol)
            identity_symbol = self.identity_deck[ct_index]
            plaintext += identity_symbol
            deck_state = self.map_state(deck_state, identity_symbol)
        return plaintext

