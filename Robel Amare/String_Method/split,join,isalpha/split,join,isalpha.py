txt = "this sentence uses words, letters , sy@#$%s, and more. "
txt2 = "thisisfullyalphabetical"

print(txt.split())              # used to split the given values
print(txt.split(","))


print(",".join(txt))            # used to merge the required values
print(" ".join(txt))

print(txt.isalpha())            # returns false if there is another value other than aplhabets
print(txt2.isalpha())           # returns true if all the values are alphabets 