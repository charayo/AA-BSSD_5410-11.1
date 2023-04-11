# Code taken for: https://rosettacode.org/wiki/Markov_chain_text_generator#Procedural
# Accessed On 04/05/2023

import math
import random
from collections import Counter


def makerule(data, context):
    '''Make a rule dict for given data.'''
    rule = {}
    words = data.split(' ')
    index = context

    for word in words[index:]:
        key = ' '.join(words[index - context:index])
        # print(key, word, rule)
        if key in rule:
            rule[key].append(word)
        else:
            rule[key] = [word]
        index += 1

    return rule


def makestring(rule, length, temp):
    '''Use a given rule to make a string.'''
    oldwords = random.choice(list(rule.keys())).split(' ')  # random starting words
    string = ' '.join(oldwords) + ' '

    for i in range(length):
        try:
            key = ' '.join(oldwords)
            newword = highest_choice(rule[key], temp)
            string += newword + ' '
            oldwords = oldwords[1:] + [newword]

        except KeyError:
            return string
    return string


def countrules(rules_dict):
    stats = {}
    for key in rules_dict.keys():
        stats[key] = Counter(rules_dict[key])
    return stats


def highest_choice(counter, temp):
    opt = counter.most_common()
    return opt[math.floor((len(opt) - 1) * temp)][0]


def readdata(name):
    with open(name, encoding='utf8') as f:
        return f.read()


if __name__ == '__main__':
    data = readdata("alice.txt")
    rule = makerule(data, 1)
    stats = countrules(rule)
    string = makestring(stats, 10, 1)
    print(string)
