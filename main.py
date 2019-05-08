import random


def read(file):

    with open(file) as f:
        contents = f.read()
    return contents


def make_rule(data, context):

    rule = {}
    index = context

    for c in data[index:]:
        key = data[index-context:index]
        
        if key in rule:
            rule[key].append(c)

        else:
            rule[key] = [c]


        index += 1
    return rule


def make_string(rule, length):
    
    old_characters = random.choice(list(rule.keys()))
    
    while old_characters.isupper() == False:
        old_characters = random.choice(list(rule.keys()))
        
    string = old_characters
    

    for i in range(length):
        try:
            key = old_characters
            new_character = random.choice(rule[key])
            string += new_character

            old_characters = old_characters[1:] + new_character

        except KeyError:
            return string
    return string

data = read('../MarkovTextGenerator/data/alice.txt')
rule = make_rule(data, 10)

string = make_string(rule, 50)
print(string)


