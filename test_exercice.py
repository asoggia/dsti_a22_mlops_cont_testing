# The simplest function to get the user email (copy to src/user_functions.py)
# just a quick modification to check something with git
def get_email_from_input():
    """ Contains '@' and '.' """
    return input("Write down your email: ")

# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Write down your email: ")

    if ("@" not in email or "." not in email or "!" not in email ): #quick modification to trick the test > want to see it the workflow
        print('Email is not valid.')
    else:
        return email

# Tests (copy to tests/test_user_functions.py)
import io

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com!')) #modify to make the test pass
    assert get_email_from_input() == 'petra@adaltas.com!' #modify to make the test pass > this time it should be good

# Do the same for the following functions
# Functions in src/user_functions.py and tests in tests/test_user_functions.py

def get_user_name_from_input():
    """ Not empty string. No spaces. """
    return input("Create your user name: ")

def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    return input("Create your password: ")