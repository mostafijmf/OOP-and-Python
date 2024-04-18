# Make file
with open('test.txt', 'w') as file:
    file.write('Hello World! Its python')

# Add text in file
with open('test.txt', 'a') as file:
    file.write('\n\nHello World! Its python')

# Read file
with open('test.txt', 'r') as file:
    text = file.read()
    print(text)