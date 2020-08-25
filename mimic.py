#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Marcus Chiriboga"


import random
import sys


def create_mimic_dict(filename):
    """Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    # +++your code here+++
    d = {}
    with open(filename) as f:
        txt = f.read().split()
        txt.insert(0, "")
        d = {}
        for word in range(len(txt)):
            # print(txt[word] + txt[word + 1])
            if word < len(txt)-1:  # what other ways can this be done.
                if txt[word] in d:
                    d[txt[word]].append(txt[word+1])
                else:
                    d.update({txt[word]: [txt[word + 1]]})
        # d.update({txt[-1]: [""]})  # improper solution to keyerror: "knows"
        # print(d)
    return d


def print_mimic_random(mimic_dict, num_words):
    """Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """
    # +++your code here+++
    # print(mimic_dict)
    mimic_random_sentence = ""
    start_word = ""
    # new_word = ""
    mimic_random_sentence += mimic_dict[start_word][0]
    new_word = mimic_dict[start_word][0]
    #  the value/index of loop doesn't matter. we are just running it _ times.
    for _ in range(num_words - 1):
        # if word in dict, run code, else set new_word to empty string.
        # this gaurd clause protects the empty cell.
        if new_word in mimic_dict:
            new_word = random.choice(mimic_dict[new_word])
            mimic_random_sentence += " " + new_word
        else:
            mimic_random_sentence += " " + new_word
            new_word = ""
    print(mimic_random_sentence, end=" ")
    # print(len(mimic_random_sentence.split()), end=" ")
    return


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
