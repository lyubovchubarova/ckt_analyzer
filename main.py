from classes import *
import re

suffixes = []
prefixes = []
circumfixes = []
verb_suffixes = []

with open('suffixes.txt', encoding='utf8') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split()
        suffixes.append(Affix(line[0], line[1], int(line[2])))

with open('prefixes.txt', encoding='utf8') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split()
        prefixes.append(Affix(line[0], line[1], int(line[2])))

with open('verb_suffixes.txt', encoding='utf8') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split()
        verb_suffixes.append(Affix(line[0], line[1], int(line[2])))

with open('circumfixes.txt', encoding='utf8') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split()
        circumfixes.append(Circumfix(line[0], line[1], line[2], line[3], int(line[4])))

def rreplace(s, old, new, count):
    return (s[::-1].replace(old[::-1], new[::-1], count))[::-1]

def normalize_output(string):
    return re.sub(r'''-{2,}''', '-', string)

def main():

    phrase = input()

    phrase = phrase.split()

    result = ''
    result_glossed = ''

    for word in phrase:
        word_parsed = word
        word_glossed = word

        for elem in circumfixes:
            if word.startswith(elem.prefix) and word.endswith(elem.suffix):

                word_parsed = word_parsed.replace(elem.prefix, elem.prefix + '-', 1)
                word_parsed = rreplace(word_parsed, elem.suffix, '-' + elem.suffix, 1)
                word_glossed = word_glossed.replace(elem.prefix, elem.prefix_gloss + '-' , 1)
                word_glossed = rreplace(word_glossed, elem.suffix, '-' + elem.suffix_gloss, 1)

        for elem in verb_suffixes:
            if word.endswith(elem.morpheme):
                word_parsed = rreplace(word_parsed, elem.morpheme, '-' + elem.morpheme, 1)
                word_glossed = rreplace(word_glossed, elem.morpheme, '-' + elem.gloss, 1)

        for elem in suffixes:
            if word.rfind(elem.morpheme) != -1:
                word_parsed = rreplace(word_parsed, elem.morpheme, '-' + elem.morpheme, 1)
                word_glossed = rreplace(word_glossed, elem.morpheme, '-' + elem.gloss, 1)
        result += ' ' + word_parsed
        result_glossed += ' ' + word_glossed
    result = normalize_output(result)
    result_glossed = normalize_output(result_glossed)

    print(result)
    print(result_glossed)


if __name__ == "__main__":
    main()