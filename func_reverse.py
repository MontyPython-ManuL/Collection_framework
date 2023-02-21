def rev_text(text):
    result = []
    symbol = "!@#$%^&*()_+?|}{[]'/.;,<>|:!№;%:?*()_+1234567890"
    spl = [i for i in text]

    for i in range(len(spl)):
        if spl[i] not in symbol:
            result.insert(0, spl[i])

    for i in range(len(spl)):
        if spl[i] in symbol:
            result.insert(spl.index(spl[i]), spl[i])
    return ''.join([i for i in result])



if __name__ == '__main__':
    cases = [
        ('Ol@eh rymy3doloV', 'Vo@lodymyr3 helO'),
        ('O!!!leh rymy???doloV', 'V!!!olodymyr??? helO'),
        ('', '')
    ]
    for text, reversed_text in cases:
        assert rev_text(text) == reversed_text
        print('good job')

