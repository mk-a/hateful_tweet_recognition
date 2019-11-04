#loading the list of English words containing doubles letters
fp = open("data/list_words_en_2.txt")
line = fp.readline()
dict_en = set()
while line:
    dict_en.add(line[:-1])
    line = fp.readline()
fp.close()

def test_repetition(token):
    """ this function tests if a token contain a character that is repeted 3 times or more.
        if no it returns False
        if yes it return a list of tuples of substring of the original token and if it was repeated
        For example, for the token "tomorrrroooooow" it will returns : 
            [('tomo', False), ('r', True), ('o', True), ('w', False)]
    """
    
    parsed = []
    i = 0
    tmp = ''
    contains_repetiton = False
    while i < len(token):
        if i+1 < len(token) and token[i] == token[i+1] and i+2 < len(token) and token[i] == token[i+2]:
            contains_repetiton = True
            if tmp :
                parsed.append((tmp,False))
            c = token[i]
            i = i+3
            while i < len(token) and token[i] == c:
                i += 1
            parsed.append((c,True))
            tmp = ''
        else:
            tmp += token[i]
            i += 1
    if tmp :
        parsed.append((tmp, False))
    if contains_repetiton :
        return parsed
    else:
        return False

def create_word(parsed, string = ''):
    """ Returns the list all the different combinations of words from a token previously parsed by `test_repetition` 
        by reducing the number of consecutive repetition of a character to one or two.
        For example, for the token "tomorrrroooooow", `test_repetition` parses it into :
            [('tomo', False), ('r', True), ('o', True), ('w', False)]
        and then, this function returns these combinations : 
            ['tomorow', 'tomoroow', 'tomorrow', 'tomorroow']
    """
    if not parsed:
        return [string]
    else :
        tmp, is_repeted = parsed.pop(0)
        if is_repeted:
            return create_word(parsed.copy(), string + tmp) + create_word(parsed.copy(), string + 2 * tmp)
        else :
            return create_word(parsed.copy(), string + tmp)


def clean(word):
    candidates = create_word(test_repetition(word))
    for candidate in candidates[1:]:
        if candidate in dict_en:
            return candidate
    return candidates[0]
