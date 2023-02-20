#Task 1
def rev_text(text):
    result = ''
    for i in range(len(text.split())):
        result += ''.join([i for i in text.split()[i][::-1]]) + ' '
    return result[:-1]


if __name__ == '__main__':
    cases = [
        ('Oleh rymydoloV', 'helO Volodymyr'),
        ('rymydoloV Oleh', 'Volodymyr helO'),
        ('', '')
    ]
    for text, reversed_text in cases:
        assert rev_text(text) == reversed_text
        print('good job')

