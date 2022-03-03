def get_user_name_from_input():
    """ Not empty string. No spaces. """
    name = input ("Create your user name: ")
    if (name is " " or ' '  in name):
        print('Email is not valid.')
    else:
        return name

# Tests (copy to tests/test_user_functions.py)
import pytest
import io

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Anj u'))
    assert get_user_name_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO(" "))
    assert get_user_name_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Anju'))
    assert get_user_name_from_input() == 'Anju'
