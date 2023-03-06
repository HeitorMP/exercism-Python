protein_dict = {
    'Methionine': ['AUG'],
    'Phenylalanine': ['UUU', 'UUC'],
    'Leucine': ['UUA', 'UUG'],
    'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
    'Tyrosine': ['UAU', 'UAC'],
    'Cysteine': ['UGU', 'UGC'],
    'Tryptophan': ['UGG'],
    'STOP': ['UAA', 'UAG', 'UGA']
}


def proteins(strand):
    cod_li = []
    sep_size = 3
    codons = [strand[i:i + sep_size] for i in range(0, len(strand), sep_size)]

    for item in codons:
        print(item)
        if item in protein_dict['STOP']:
            break
        for key, value in protein_dict.items():
            if item in protein_dict[key]:
                cod_li.append(key)

    return cod_li
