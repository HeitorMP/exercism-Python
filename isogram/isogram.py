def is_isogram(string):

    string = string.replace(" ", "").replace("-", "").lower()
    return (len(set(string)) == len(string))
