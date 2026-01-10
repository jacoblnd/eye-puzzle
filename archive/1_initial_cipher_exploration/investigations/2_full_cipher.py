"""Building off of the simple cipher, we can just construct a full
27-character alphabet (including space) with 10 ciphertext-only symbols:
"""

from ciphers.simple_cipher import SimpleDeckCipher
from ciphers.util import deck_from_word, print_cipher_decipher

full_identity_deck = "!@#$%^*( ABCDEFGHIJKLMNOPQRSTUVWXYZ"
permutation_words = [
    "APRICOT",
    "BRICKED",
    "CURVED",
    "DELIGHT",
    "EXHAUSTING",
    "FLUORIDE",
    "GELATIN",
    "HYPERBOLIC",
    "INOCULATE",
    "JUXTAPOSED",
    "KILT",
    "LOGARITHM",
    "MODULE",
    "NORMAL",
    "OBFUSCATED",
    "PREAMBLE",
    "QUADRICEP",
    "RELOCATE",
    "SUBLIMATE",
    "THICK",
    "UNVEIL",
    "VELOCITY",
    "WIZARD",
    "XYLO",
    "YES",
    "ZOID",
    " APHORISM"
]
full_permutation_deck = {
    word[0]: deck_from_word(full_identity_deck, word)
    for word in permutation_words
}

full_cipher = SimpleDeckCipher.from_decks(full_identity_deck, full_permutation_deck)

print_cipher_decipher(full_cipher, "HOW MUCH WOOD COULD A WOODCHUCK CHUCK IF A WOODCHUCK COULD CHUCK WOOD")
print_cipher_decipher(full_cipher, "AHOW MUCH WOOD COULD A WOODCHUCK CHUCK IF A WOODCHUCK COULD CHUCK WOOD")
print_cipher_decipher(full_cipher, "BHOW MUCH WOOD COULD A WOODCHUCK CHUCK IF A WOODCHUCK COULD CHUCK WOOD")
print_cipher_decipher(full_cipher, "CHOW MUCH WOOD COULD A WOODCHUCK CHUCK IF A WOODCHUCK COULD CHUCK WOOD")
