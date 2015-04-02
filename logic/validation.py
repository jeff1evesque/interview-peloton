#!/usr/bin/python

## @validation.py
#  This file contains validation functions.

## validate_alnum: validates if string is a non-trivial alphanumeric.
def validate_alphanum(str):
    if len(str) > 0 and str.isalnum():
        return True
    else:
        return False
