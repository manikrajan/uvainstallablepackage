import re

def afunction():
    print("This is the installed function")

def clean_string(str_word):
    """
    INPUTS:
    str_word     string string contining several words to clean
    RETURNS:
    string       the string after removal of extra spaces, punctuation and lowercasing
    """
    str_word = re.sub(r'\W+', ' ', str_word)
    assert isinstance(str_word, str), "String expected but recieved type {} instead".format(type(str_word))

    return str_word.strip()

def space_compress(words):
  assert type(words) is str, "Expected string but got {ty}".format(ty=type(words))  
  cmpressed_string = " ".join(words.split())
  return cmpressed_string

def new_func():
    pass
