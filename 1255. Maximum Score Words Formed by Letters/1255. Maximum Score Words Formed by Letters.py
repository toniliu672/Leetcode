class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def calculate_word_score(word):
            return sum(score[ord(char) - ord('a')] for char in word)
        
        def can_form_word(word, available):
            word_count = Counter(word)
            for char, count in word_count.items():
                if available[char] < count:
                    return False
            return True
        
        def backtrack(index, available, current_score):
            if index == len(words):
                return current_score
            
            max_score = backtrack(index + 1, available, current_score)
            
            word = words[index]
            if can_form_word(word, available):
                word_score = calculate_word_score(word)
                for char in word:
                    available[char] -= 1
                max_score = max(max_score, backtrack(index + 1, available, current_score + word_score))
                for char in word:
                    available[char] += 1
            
            return max_score
        
        available = Counter(letters)
        
        return backtrack(0, available, 0)