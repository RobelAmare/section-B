
def check_is_upper(string):
    if string.isupper():
        print(f"The string '{string}' is completely uppercase!")
    else:
        print(f"The string '{string}' is NOT completely uppercase.")

check_is_upper("HELLO")   # Should print that the string is completely uppercase which in this case is true
check_is_upper("Hello")   # Should print that the string is NOT completely uppercase this time its false 
check_is_upper("12345")   # Should print that the string is NOT completely uppercase this time its false
