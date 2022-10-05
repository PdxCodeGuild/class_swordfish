with open('test.txt', 'r') as f:
    contents = f.read()

contents = contents.upper()

with open('test.txt', 'w') as f:
    f.write(contents)