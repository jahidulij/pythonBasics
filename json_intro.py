book = {}

book['tom'] = {
    "name": 'Tom',
    "address": '1 red street, NY',
    "phone": 919191910
}

book['bob'] = {
    "name": 'Bob',
    "address": '2 red street, NY',
    "phone": 919191911
}

import json
s = json.dumps(book)
with open("C://Users//Asus//workspace_python//pythonBasics//test_josn.txt", 'w') as f:
    f.write(s)

# s = f.read()
book = json.loads(s)
print(book)