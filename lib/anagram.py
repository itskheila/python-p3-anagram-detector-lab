class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, candidates):
        matches = []
        for candidate in candidates:
            if sorted(candidate.lower()) == sorted(self.word.lower()):
                matches.append(candidate)
        return matches
