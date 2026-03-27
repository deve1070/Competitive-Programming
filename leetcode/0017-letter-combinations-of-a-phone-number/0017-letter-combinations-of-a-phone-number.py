class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
       
        if not digits:
            return []
        
        # Mapping from digits to letters
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Result list to store the combinations
        result = []
        
        # Backtracking helper function
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get the letters for the current digit
            current_digit = digits[index]
            for letter in digit_to_letters[current_digit]:
                # Recursively build combinations
                backtrack(index + 1, current_combination + letter)
        
        # Start backtracking from the first digit
        backtrack(0, "")
        
        return result
