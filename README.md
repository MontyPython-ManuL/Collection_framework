# Task 1 Reverse str


### It`s so easy code we should press -start and this code reverse text, but all words stay on the same place



1. We create the function rev_text(text): 
````python
def rev_text(text):
````
text = str
2. We create сhangeable where we will have result of function
````python
def rev_text(text):
    result = ''
````
3. Here we add сycle that have len of text.word in text
````python
def rev_text(text):
    result = ''
    for i in range(len(text.split())):
````
4. We reverse text with itterator and finally make str from itterator list with join and append to result
````python
def rev_text(text):
    result = ''
    for i in range(len(text.split())):
        result += ''.join([i for i in text.split()[i][::-1]]) + ' '
````
5. Add return - result of function with not using 'space' from last word in str [:-1]
````python
def rev_text(text):
    result = ''
    for i in range(len(text.split())):
        result += ''.join([i for i in text.split()[i][::-1]]) + ' '
    return result[:-1]
````
6. if this is ‘__main__’, it implies that the module is being run standalone by the user and we can do corresponding appropriate actions.
````python
if __name__ == '__main__':
````
7.Create list for test to assert
````python
if __name__ == '__main__':
    cases = [
        ('Oleh rymydoloV', 'helO Volodymyr'),
        ('rymydoloV Oleh', 'Volodymyr helO'),
        ('', '')
    ]
````
8.We сheck for correctness return of function
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