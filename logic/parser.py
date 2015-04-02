#!/usr/bin/python

## @parser.py
#  This file is responsible for retrieving data from the Peloton API.
import requests

## get_content: acquires JSON response from Peloton API.
def get_content(stream):
    r = requests.get('https://api.pelotoncycle.com/quiz/next/' + stream)
    return r.json()
