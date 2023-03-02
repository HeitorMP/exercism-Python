"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    splited = title.split()

    for index, word in enumerate(splited):
        splited[index] = word.capitalize()
    return ' '.join(splited)


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    marks = ['.', '!', '?', ';', ':']

    return sentence[len(sentence) - 1] in marks


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    return ' '.join(sentence.split())


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    splited = sentence.split()
    if splited[len(splited) - 1].endswith('.'):
        splited[len(splited) - 1] = splited[len(splited) - 1][:-1]

    if old_word not in splited:
        return sentence

    splited[splited.index(old_word)] = new_word

    return ' '.join(splited) + '.'


# print(capitalize_title("heitor    amasd asd"))
# print(clean_up_spacing("     asdasd sadasd    asdasd"))
# print(replace_word_choice("lala lele lili.", "lili", "lulu"))
