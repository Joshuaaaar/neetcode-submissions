class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1 

        # two pointer approach 
        while left < right :

            # if left side isn't alphanumeric

            while left < right and s[left].isalnum() is False:

                left += 1
            
            # if right side isn't alphanumber

            while right > left and s[right].isalnum() is False:

                right -= 1
            
            if s[right].lower() != s[left].lower():
                return False
            
            left +=1 
            right -= 1

        return True

            


    
        
            

            


