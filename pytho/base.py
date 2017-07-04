

# https://en.wikipedia.org/wiki/Vietnamese_language

LEVEL = 'aăâeêioôơuưy'  # AKA "ngang"
HANGING = 'àằầèềìòồờùừỳ'  # AKA "huyền"
SHARP = 'áắấéếíóốớúứý'  # AKA "sắc"
ASKING = 'ảẳẩẻểỉỏổởủửỷ'  # AKA "hỏi"
TUMBLING = 'ãẵẫẽễĩõỗỡũữỹ'  # AKA "ngã"
HEAVY = 'ạặậẹệịọộợụựỵ'  # AKA "nặng"

FULL_VOWELS = LEVEL + HANGING + SHARP + ASKING + TUMBLING + HEAVY


class InvalidWord(Exception):
    pass


def split_cons_vowel(word):
    '''Returns tuple consists of consonant and vowel parts
    '''

    # TODO Fix when left side is "gi"
    for idx, char in enumerate(word):
        if char in FULL_VOWELS:
            return (word[:idx], word[idx:])

    raise InvalidWord("Vietnamese word must contain at least 1 vowel")
