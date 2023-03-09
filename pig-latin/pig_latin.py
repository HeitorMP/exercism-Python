def rules(word):
    if word[0] not in 'aieou' and word[1:3] == 'qu':
        return word[3:] + word[:3] + 'ay'
    if word[0] in 'aieou':
        return word + 'ay'
    if word[:2] in ['yt', 'xr']:
        return word + 'ay'
    if word[:2] in ['qu']:
        return word[2:] + word[:2] + 'ay'
    if set('aieou') - set(word) == set('aieou') and 'yt' not in word:
        return word[1:] + word[:1] + 'ay'
    #return rules(word[1:] + word[0])


def translate(text):
    return ' '.join([rules(word) for word in text.split(' ')])