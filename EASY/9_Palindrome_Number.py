def isPalindrome(x: int) -> bool:
    return False if x < 0 else str(x)[::-1] == str(x)

# Sample testcases
print(isPalindrome(-121))  # False
print(isPalindrome(212))  #True