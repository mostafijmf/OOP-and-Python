# Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])
  for kid in kids:
    print(kid)

my_function("Emil", "Tobias", "Linus")


# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])
  for key, name in kid.items():
    print(key, ':',name)

my_function(fname = "Tobias", lname = "Refsnes")
