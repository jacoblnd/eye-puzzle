"""What happens if we setup a cipher with permutation maps which don't shuffle very
much? These only have 3-letters meaning the rest are left in the same position.
"""
from ciphers.simple_cipher import SimpleDeckCipher
from ciphers.util import deck_from_word

full_identity_deck = "!@#$%^*( ABCDEFGHIJKLMNOPQRSTUVWXYZ"
permutation_words = [
    "APR",
    "BRI",
    "CUR",
    "DEL",
    "EXH",
    "FLU",
    "GEL",
    "HYP",
    "INO",
    "JUX",
    "KIL",
    "LOG",
    "MOD",
    "NOR",
    "OBF",
    "PRE",
    "QUA",
    "REL",
    "SUB",
    "THI",
    "UNV",
    "VEL",
    "WIZ",
    "XYL",
    "YES",
    "ZOI",
    " AP"
]
full_permutation_deck = {
    word[0]: deck_from_word(full_identity_deck, word)
    for word in permutation_words
}

full_cipher = SimpleDeckCipher.from_decks(full_identity_deck, full_permutation_deck)

print(full_cipher.encipher("HOW MUCH WOOD COULD A WOODCHUCK CHUCK IF A WOODCHUCK COULD CHUCK WOOD"))
print(full_cipher.encipher("AHOW MUCH WOOD COULD A WOODCHUCK CHUCK IF A WOODCHUCK COULD CHUCK WOOD"))
print(full_cipher.encipher("BHOW MUCH WOOD COULD A WOODCHUCK CHUCK IF A WOODCHUCK COULD CHUCK WOOD"))
print(full_cipher.encipher("CHOW MUCH WOOD COULD A WOODCHUCK CHUCK IF A WOODCHUCK COULD CHUCK WOOD"))
"""
HMVPFRZCSQYHCIE!AFIGAOL CAUS^XJPNM#GWES*YEORBCETP ^HU(WGVU@N#OC^SMA%^
AFKVNDQZ SOYF GCA*DGE*MJ^ *US#XHNLKREWCS$YCMQ( CTN^#FU%WEVUPLRM #SK*@#
BFLVODQZ SPYF GCB*DGE*NK^ *US#XHOMLIEWCS$YCNQ( CTO^#FU%WEVURMIN #SL*@#
CFKVNDPZ QOYF GBC*DGE*MJ^ *TQ#XHNLKREWBQ$YBMP( BSN^#FT%WEVTULRM #QK*@#
"""

