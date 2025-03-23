import string


txt = "this is a text message for you to check the validity"   # reference sentence

print(txt.startswith("this"))                                  # true
print(txt.startswith("is"))                                    # false


print(txt.endswith("validity"))                         # true
print(txt.endswith("this"))                             # false


print(txt.count("t"))               # counts the number of "t"s in the sentence above
