txt = "this"
txt2 = "23"
txt3 = "this23"
txt4 = " "

print(txt.isdigit())            #false
print(txt2.isdigit())           #true

print(txt4.isalnum())           # false
print(txt3.isalnum())           # true


print(txt.isspace())            # false
print(txt4.isspace())           # true

print("Hello {name}, your balance is {money}.".format(name="Adam", money =230.2346))      # fromats add the desired output to the text we need 