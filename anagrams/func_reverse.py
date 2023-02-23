def rev_text(text):
    result = []
    for word in text.split():
        result.append(compact_word(word))
    return ' '.join([word for word in result])


def compact_word(word):
    result = []
    alfa_iter = iter([char for char in word[::-1] if char.isalpha()])
    for letter in word:
        if letter.isalpha():
            result.append(next(alfa_iter))
        else:
            result.append(letter)
    return ''.join(result)

