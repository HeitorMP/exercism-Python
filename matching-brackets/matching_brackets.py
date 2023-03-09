def is_match(symbs):
    symbols = [['{', '}'], ['(', ')'], ['[', ']']]
    return symbs in symbols


def is_paired(input_string):
    input_string = ''.join([c for c in input_string if c in '{}()[]'])
    if len(input_string) == 0:
        return True

    i = -1
    while len(input_string):
        i += 1
        try:
            if (is_match([input_string[i], input_string[i+1]])):
                if len(input_string) == 2:
                    return True
                input_string = input_string[:i] + input_string[i+2:]
                i = -1
        except IndexError:
            return False