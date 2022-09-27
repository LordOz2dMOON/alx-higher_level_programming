#!/usr/bin/python3
def multiple_returns(sentence):
    a = ()
    length = (len(sentence),)
    first_letter = (sentence[0],)
    if len(sentence) == 0:
         a = a + None
    else:
        a = a + length
        a = a + first_letter
        return a
