class Solution(object):
    def mapWordWeights(self, words, weights):
        result = []
        for word in words:
            total = 0

            for char in word:
                total += weights[ord(char) - ord('a')]

            remainder = total % 26
            result.append(chr(ord('z') - remainder))

        return ''.join(result)
        