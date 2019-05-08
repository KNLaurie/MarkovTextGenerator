import random


def read(file):

    with open(file) as f:
        contents = f.read()
    return contents


def make_rule(data, context):

    rule = {}
    index = context

    for char in data[index:]:
        key = data[index-context:index]
        
        if key in rule:
            rule[key].append(char)

        else:
            rule[key] = [char]


        index += 1
    return rule


def make_string(rule, length):

    old_chars = random.choice(list(rule.keys()))
    print(old_chars)
    string = old_chars
    

    for i in range(length):
        try:
            key = old_chars
            new_char = random.choice(rule[key])
            string += new_char

            old_chars = old_chars[1:] + new_char

        except KeyError:
            return string
    return string

data = read('../MarkovTextGenerator/data/alice.txt')
rule = make_rule(data, 10)

for i in range(5):
    string = make_string(rule, 50)
    print(i + 1)
    print(string)


