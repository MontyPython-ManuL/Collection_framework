def rev_text(text):
    result = []
    for item in text.split():
        part_word2 = iter([i for i in item if i.isalpha()][::-1])
        for i in [i for i in item]:
            if not i.isalpha():
                result.append(i)
            elif i.isalpha():
                result.append(next(part_word2))
        result.append(' ')

    return ''.join([i for i in result]).strip()


if __name__ == '__main__':
    cases = [
        ('O@leh rymy3doloV h2appy', 'h@elO Volo3dymyr y2ppah'),
        ('O!!!leh rymy???doloV', 'h!!!elO Volo???dymyr'),
        ('', '')
    ]
    for text, reversed_text in cases:
        assert rev_text(text) == reversed_text
        print('good job')

