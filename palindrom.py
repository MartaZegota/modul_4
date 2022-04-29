print("This program helps you to find palindrome.")
def palindrome(s):
    """Program asks to enter a string, next checks if it:
     - is palindrome (ans True) or
     - not palindrome (ans False)
    """
    s = str
print("Enter word:")
s = input()
s = s.lower()
print(False if s != s[::-1] else True)