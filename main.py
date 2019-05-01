import random


def read(file):

    with open(file) as f:
        contents = f.read()
    return contents


def make_rule(data, context):

    rule = {}
    words = data.split(' ')
    index = context

    for word in words[index:]:
        key = ' '.join(words[index-context:index])
        print(words[index-context:index])
        if key in rule:
            rule[key].append(word)

        else:
            rule[key] = [word]

        index += 1

    return rule


def make_string(rule, length):

    old_words = random.choice(list(rule.keys())).split(' ')
    string = ' '.join(old_words)

    for i in range(length):
        try:
            key = ' '.join(old_words)
            new_word = random.choice(rule[key])
            string += new_word + ' '

            for word in range(len(old_words)):
                old_words[word] = old_words[(word + 1) % len(old_words)]

            old_words[-1] = new_word

        except KeyError:
            return string
    return string


if __name__ == '__main__':
    data = read('/home/kaitlyn/alice.txt')
    data.append('/home/kaitlyn/curry.txt')
    data.append('/home/kaitlyn/election.txt')
    rule = make_rule(data, 2)
    string = make_string(rule, 30)
    print(string)


