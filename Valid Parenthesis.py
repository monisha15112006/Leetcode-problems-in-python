class Solution:
    def isValid(self, text: str) -> bool:
        stack = []

        for char in text:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False

                last_open = stack.pop()

                diff = ord(char) - ord(last_open)
                if diff != 1 and diff != 2:
                    return False

        return len(stack) == 0
        
