"""Utility functions for dealing with deck ciphers."""

def deck_from_word(identity_deck: str, word: str) -> str:
    """Helper function for generating the full permutation deck for a PT symbol for a cipher
    given the identity deck and a starting word.
    Always writes the rest of the deck in identity-deck order.
    """
    permutation_deck = word
    for symbol in identity_deck:
        if symbol not in permutation_deck:
            permutation_deck += symbol
    return permutation_deck

def print_cipher_decipher(cipher, plaintext: str):
    ciphertext = cipher.encipher(plaintext)
    print("Ciphertext: \t\t", ciphertext)
    print("Decrypted Ciphertext: \t", cipher.decipher(ciphertext))

