def is_pangram(sentence):
    formated_sentence = set([c.lower() for c in sentence if c.isalpha()])
    return len(formated_sentence) == 26
