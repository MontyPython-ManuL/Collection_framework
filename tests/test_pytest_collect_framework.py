import pytest
from unittest.mock import patch
from unittest import mock
import io
from io import StringIO
import sys
from collection_framework.collect_framework import count_unique_char, main


def test_cache_in_count_unique_char():
    texts = ['hello', 'gello', 'hello', 'gello']
    list(map(count_unique_char, texts))
    assert count_unique_char.cache_info().hits == 2


@mock.patch('sys.stdout', new_callable=StringIO)
def test_main_when_input_string_and_file(mock_stdout):
    test_args = ["collection_framework/collect_framework.py", "--string", "adasdagl", '--file', 'test_file']
    with patch.object(sys, 'argv', test_args), patch('builtins.open', return_value=io.StringIO('test data')):
        main()
        assert(mock_stdout.getvalue() == "4\n")


@mock.patch('sys.stdout', new_callable=StringIO)
def test_main_when_input_only_string(mock_stdout):
    test_args = ["collection_framework/collect_framework.py", "--string", "adasdagl"]
    with patch.object(sys, 'argv', test_args):
        main()
        assert (mock_stdout.getvalue() == "3\n")


@mock.patch('sys.stdout', new_callable=StringIO)
def test_main_when_input_only_file(mock_stdout):
    test_args = ["collection_framework/collect_framework.py", '--file', 'test_file']
    with patch.object(sys, 'argv', test_args), patch('builtins.open', return_value=io.StringIO('test data')):
        main()
        assert (mock_stdout.getvalue() == "4\n")


@mock.patch('sys.stdout', new_callable=StringIO)
def test_main_when_input_incorrect_argument(mock_stdout):
    test_args = ["collection_framework/collect_framework.py", '--filename', 'test_file']
    with patch.object(sys, 'argv', test_args), patch('builtins.open', return_value=io.StringIO('test data')):
        main()
        assert (mock_stdout.getvalue() == "0\n")


@mock.patch('sys.stdout', new_callable=StringIO)
def test_main_when_input_string_file_incorrect_argument(mock_stdout):
    test_args = ["collection_framework/collect_framework.py", "--string", "adasdagl", '--file', 'test_file',
                 '--filename', 'filename']
    with patch.object(sys, 'argv', test_args), patch('builtins.open', return_value=io.StringIO('test data')):
        main()
        assert (mock_stdout.getvalue() == "4\n")


@pytest.mark.parametrize("input_text, expected_result",
                         [
                             ('abbc', 2),
                             ('aassdgjdfghdjhgkdjf', 1),
                             ('1231241569', 5),
                             ('ffffffffffffffafffffff', 1),
                             ('asdfghjklzxcvbnm', 16),
                             ('!@##$%^&*!', 6),
                         ])
def test_count_unique_char(input_text, expected_result):
    assert count_unique_char(input_text) == expected_result
