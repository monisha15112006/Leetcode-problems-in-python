class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count, close_count, current_string):
            # Base case: if the string length is 2*n, a valid combination is formed
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
            
            # Rule 1: We can add an opening bracket if we have used fewer than n
            if open_count < n:
                backtrack(open_count + 1, close_count, current_string + "(")
            
            # Rule 2: We can only add a closing bracket if it won't exceed the number of open brackets
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_string + ")")
        
        backtrack(0, 0, "")
        return res
