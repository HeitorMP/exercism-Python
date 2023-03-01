"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    separator = ' :: '
    word_group = vocab_words[0] + separator

    for index in range(1, len(vocab_words)):
        word_group += vocab_words[0] + vocab_words[index]
        if index < len(vocab_words) - 1:
            word_group += separator

    return word_group


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word[-5:] == "iness":
        return word[:-5] + 'y'
    elif word[-4:] == "ness":
        return word[:-4]
    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """
    word_list = sentence.split(' ')
    verb = ''

    for char in word_list[index]:
        if char.isalnum():
            verb += char

    return verb + 'en'


# print(add_prefix_un('teste'))
# print(make_word_groups(['inter', 'twine', 'connected', 'dependent', 'galactic']))
# print(remove_suffix_ness("joao"))
# print("darken.".endswith('.'))
# print(adjective_to_verb('His expression went dark.', -1))
