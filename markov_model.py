"""
markov_model.py

A data type that represents a Markov model of order k from a given text string.
"""
import sys
import random

class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Creates a Markov model of order k from given text. Assumes that text
        has length at least k.
        """

        self._k = k
        self._st = {}
        circ_text = text + text[:k]
        for i in range(len(circ_text) - k):
            word = circ_text[i:i+k]
            self._st.setdefault(word, {})
            next_word = circ_text[i + k]            
            check = self._st.get(word).setdefault(next_word, 0)
            self._st.get(word).update({next_word: check + 1})
    def order(self):
        """
        Returns order k of Markov model.
        """

        return self._k

    def kgram_freq(self, kgram):
        """
        Returns number of occurrences of kgram in text. Raises an error if
        kgram is not of length k.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        return sum(self._st.get(kgram).values())

    def char_freq(self, kgram, c):
        """
        Returns number of times character c follows kgram. Raises an error if
        kgram is not of length k.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        return self._st.get(kgram).get(c)

    def rand(self, kgram):
        """
        Returns a random character following kgram. Raises an error if kgram
        is not of length k or if kgram is unknown.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        if kgram not in self._st:
            raise ValueError('Unknown kgram ' + kgram)
        return random.choice(list(self._st.get(kgram).keys()))

    def gen(self, kgram, T):
        """
        Generates and returns a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k characters of the
        generated string is the argument kgram. Assumes that T is at least k.
        """
        text = kgram
        l = len(kgram)
        for i in range(T - self._k):
            text += self.rand(text[-l:])
        return text
        

    def replace_unknown(self, corrupted):
        """
        Replaces unknown characters (~) in corrupted with most probable
        characters, and returns that string.
        """

        # Given a list a, argmax returns the index of the maximum element in a.
        def argmax(a):
            return a.index(max(a))

        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                kgram = original[i - self._k: i]
                dictKeys = self._st.get(kgram)
                if(dictKeys != None):
                    index = argmax(list(dictKeys.values()))
                    toAdd = list(self._st.get(kgram).keys())[index]
                    original += toAdd
            else:
                original += corrupted[i]
        return original


def _main():
    """
    Test client [DO NOT EDIT].
    """

    text, k = sys.argv[1], int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    for line in sys.stdin:
        line.rstrip()
        words = line.split()
        for i in range(len(words) - 1):
            kgram = words[i]
            char = words[i+1]
            a.append((kgram.replace("-", " "), char.replace("-", " ")))
            i+=1
    for kgram, char in a:
        if char == ' ':
           sys.stdout.write("freq({0}) = {1}\n".format(kgram, model.kgram_freq(kgram))) 
        else:
            sys.stdout.write('freq({0}, {1}) = {2}\n'.format(kgram, char,
                         model.char_freq(kgram, char)))

if __name__ == '__main__':
    _main()
