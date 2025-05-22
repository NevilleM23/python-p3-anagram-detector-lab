# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word
        self.sorted_lower = sorted(word.lower())
    
    def match(self, candidates):
        original_lower = self.word.lower()
        anagrams = []
        for candidate in candidates:
            candidate_lower = candidate.lower()
            if candidate_lower == original_lower:
                continue
            if sorted(candidate_lower) == self.sorted_lower:
                anagrams.append(candidate)
        return anagrams