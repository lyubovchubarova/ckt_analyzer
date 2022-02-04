verb_endings = []
noun_endings = []
dictionary = []

with open('verb_morphology.txt', encoding = 'utf-8') as f:
    lines = f.read().splitlines()
    for line in lines:
        verb_endings.append(line)

with open('noun_morphology.txt', encoding = 'utf-8') as f:
    lines = f.read().splitlines()
    for line in lines:
        noun_endings.append(line)

with open('ckt_dictionary.txt', encoding = 'utf-8') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split('   ')
        dictionary.append([line[0], line[1], line[2]])

def change_harmony_to_strong(word):
    word = word.replace('e', 'a')
    word = word.replace('i', 'e')
    word = word.replace('u', 'o')
    return word

def define_pos(word):
    for n_end in noun_endings:
        if word.endswith('ɬʔ' + n_end):
            return 'PTCP'
        elif word.endswith(end):
            return 'NOUN'
    for v_end in verb_endings:
        if word.endswith(v_end):
            return 'VERB'
    for elem in dictionary:
        if word == elem[0]:
            return elem[1]
    return 'X'





