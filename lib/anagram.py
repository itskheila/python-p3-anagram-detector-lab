class Anagram:
    """A simple anagram detector.

    Create an instance with a reference word then call ``match`` with a list of
    candidate words to obtain those that are anagrams of the reference word.
    """

    def __init__(self, word: str):
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        # Store the original word and a canonical (sorted) representation for
        # fast comparisons later. We keep everything in lowercase to make the
        # comparison case-insensitive while preserving the original word for
        # any future use.
        self._word = word
        self._canonical = self._canonical_form(word)

    @staticmethod
    def _canonical_form(word: str) -> str:
        """Return the canonical representation of *word* used for comparison.

        The canonical form is simply the word's letters lower-cased and
        arranged in sorted order. Two words are anagrams if and only if their
        canonical forms are identical.
        """
        return "".join(sorted(word.lower()))

    def match(self, candidates: list[str]) -> list[str]:
        """Return the sub-list of *candidates* that are anagrams of the base word.

        The order of *candidates* is preserved in the output. Words that are
        identical to the base word (ignoring case) are **not** considered
        anagrams and are therefore excluded from the result.
        """
        if not isinstance(candidates, (list, tuple, set)):
            raise TypeError("match() expects a list (or iterable) of candidate words")

        matches: list[str] = []
        for candidate in candidates:
            # Ensure candidate is a string; if not, skip it.
            if not isinstance(candidate, str):
                continue

            # Exclude the word itself (case-insensitive comparison).
            if candidate.lower() == self._word.lower():
                continue

            if self._canonical_form(candidate) == self._canonical:
                matches.append(candidate)
        return matches
