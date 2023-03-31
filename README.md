# -- Instalation --

---

## Development
* install <a href="https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe"> Python 3.8.0. </a>
* run `pip install requirments.txt`

---

## Launching 🙂

### Local
* `python collection_framework/collect_framework.py --string adafa --file text_file` -  run our script
---
* `python pytest discover ` - run test files
---

### Links
* <a href='https://coverage.readthedocs.io/en/7.2.0/'> coverage </a> - documentation
* <a href='https://docs.pytest.org/en/7.2.x/'> pytest </a> - documentation
* <a href='https://docs.python.org/3/library/argparse.html'> argparse </a> - documentation
* <a href='https://docs.python.org/3/library/functools.html'> functools </a> -  documentation
---

## Instruction for using coverage testing 🙂
`Use coverage run to run your test suite and gather data`
* `$ coverage run -m pytest`
* `$ coverage report -m` - to report on the results:
* `$ coverage html` - for a nicer presentation

--- 

## Directory-packages for using coverage testing. ✊🏻

1. File requirements.txt have module for install before you will use testing. Before run testing you should in your terminal write `pip install -r requirements.txt`
and you install all of there.

![Іллюстрація до проєкту](docs/image_2023-02-27_20-06-34.png)

---
## Use Command-line
* `python collection_framework/collect_framework.py --string "string" --file "file"`
* if you are input only string `python src/collect_framework.py --string "adasdagl"`
* if you are input only string `python src/collect_framework.py --file "src/test.txt"`
* if you are input string and file `python src/collect_framework.py --string "adasdagl" --file "src/test.txt"` - string went be ignor
___
## Test coverage
### pytest `coverage report`
![Іллюстрація до проєкту](docs/img.png)