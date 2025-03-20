def change_my_string(my_text):

  print("Here is my string:")
  print(my_text)

  # Make it title case (first letter of each word big)
  title_version = my_text.title()
  print("Here is title case:")
  print(title_version)

  # Make first letter big
  capital_version = my_text.capitalize()
  print("Here is capitalized:")
  print(capital_version)

  # make all letters big
  upper_version = my_text.upper()
  print("Here is all uppercase:")
  print(upper_version)
  
my_string = "hello WORLD this is a Test 123 string!@#"
change_my_string(my_string)
