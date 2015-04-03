#!/usr/bin/python

## @cached_stream.py
#  This file caches two streams of data, using python memcache.
import json
import memcache
from logic.memcached_interface import Memcached

## cached_stream:
def cached_stream():
    cached = Memcached()
    cached_stream_1 = cached.get('cStream1')
    cached_stream_2 = cached.get('cStream2')

    if cached_stream_1:
        list_stream_1 = json.loads(cached_stream_1)
        list_stream_1.append(content_1['current'])
        cached.set('cStream1', json.dumps(list_stream_1))
    else:
        list_stream_1.append(content_1['current'])
        cached.set('cStream1', json.dumps(list_stream_1))

    if cached_stream_2:
        list_stream_2 = json.loads(cached_stream_2)
        list_stream_2.append(content_2['current'])
        cached.set('cStream2', json.dumps(list_stream_2))
    else:
        list_stream_2.append(content_2['current'])
        cached.set('cStream2', json.dumps(list_stream_2))
