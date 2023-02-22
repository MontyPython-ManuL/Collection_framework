# Task 1 Reverse str


### It`s so easy code we should press -start and this code reverse text, but all words stay on the same place

## So `What it do`?
### - If you need reverse all wards like this 
````python
'O@leh rymy3doloV' ==>>  'h@elO Volo3dymyr'.
````
### - You see that all word reverse but symbol like that !!! or that ??? stay the same place
````python
'O!!!leh rymy???doloV' ==>> 'h!!!elO Volo???dymyr'.
````
## So `next` i`m explain how it's work.

1. We create the function `rev_text(text):` 
````python
def rev_text(text):
````
text = str

2. We create two cycles for ignore symbol and append revers words.
````python
        for part_word in text.split():
            n = 0
            for i in [i for i in part_word]:
                if not i.isalpha():
                    result.append(i)
                elif i.isalpha():
                    part_word2 = [i for i in part_word if i.isalpha()][::-1]
                    result.append(part_word2[n])
                    n += 1
            result.append(' ')

        return ''.join([i for i in result]).strip()
````
2. Create list for test to assert
````python
if __name__ == '__main__':
    cases = [
        ('Oleh rymydoloV', 'helO Volodymyr'),
        ('rymydoloV Oleh', 'Volodymyr helO'),
        ('', '')
    ]
````
3. We are сheck for correct return of function
````python
if __name__ == '__main__':
    cases = [
        ('Oleh rymydoloV', 'helO Volodymyr'),
        ('rymydoloV Oleh', 'Volodymyr helO'),
        ('', '')
    ]
    for text, reversed_text in cases:
        assert rev_text(text) == reversed_text
        print('good job')
````