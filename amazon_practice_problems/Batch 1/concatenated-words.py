class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    #This solution uses memoization to

        words = set(words)
        memo = dict()
        return [w for w in words if self.valid(w, words, memo)]


    def valid(self, word, words, memo):

        if word in memo:
            return memo[word]

        # TRY ALL COMBINATIONS OF NON-EMPTY PREFIX AND SUFFIX FOR THE WORD
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            # PREFIX MUST BE VALID
            if prefix in words :
               # AND SUFFIX IS EITHER VALID OR CAN BE BROKEN INTO VALID SUBSTRINGS
                if (suffix in words or self.valid(suffix, words, memo)):
                    memo[word] = True
                    return True

        memo[word] = False
        return False
