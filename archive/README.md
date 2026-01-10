# Archive

This directory contains previous partial states of this repo.

This is my current solution in trying to:

1. Minimize the time I spend re-hashing the organizational structure of this repo.
2. Maintain some representation of the logical progression of the project.

The significant amount of duplication which will result from this seems reasonable to me.
Storage is free on Github and I can consolidate if needed in the future.

## Previous States

### 1 Initial Cipher Exploration

The goal of this phase of the repo was to attempt a naive construction of the deck cipher.

#### Expected Utility

This seemed like a good approach to understand more about the problem space or, at the very least, have some fun with a toy cipher.
If a deck analogy was used when constructing the original cipher (a large logical leap but maybe reasonable considering other deck analogies in Noita), trying to emulate that development process might yield intuition about the true implementation.

Taking another large logical leap: if the resultant cipher was somewhat representative of the actual implementation, then a simplified implementation of that (such as with fewer characters and/or permutations) might provide a more-approachable way to develop understandings of generalizable attacks against the full implementation.

#### Findings / Results

**Permutation Representation**

I wanted to construct a convenient way to represent permutations with alphabets like I had seen in the discord.
What I ended up with was an identity deck represented just as the ordered alphabet, a set of different permutation decks represented as other jumbled alphabets, and the concept of a permutation as the required swaps to go from the identity deck to any given permutation deck.
I realized that such an identity deck must not begin with a PT symbol due to the no-doubles rule.

I incorrectly assumed that this meant it must begin with a CT character
and that a CT character must, therefore, map to the identity deck.
Tomster provided a correct refutation that this needn't be the case.
And, in fact, no character needs to map to any identity deck.

The representation still seems useful for convenience in the ciphers but a careful distinction must be made between an "identity deck" used to derive a permutation associated with a given PT symbol and any true identity deck which may actually not map to any symbol in the CT.

I'll need to try to create some common names for these.

