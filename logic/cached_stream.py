#!/usr/bin/python

## @cached_stream.py
#  This file caches two streams of data, using python memcache.
import json
import memcache
from logic.memcached_interface import Memcached

## cached_stream: either append data stream to existing memcached
#                 object, or create a new memcached object, with
#                 the supplied argument as its value.
def cached_stream(content_1, content_2):
    # local variables
    list_stream_1   = []
    list_stream_2   = []
    cached          = Memcached()
    cached_stream_1 = cached.get('cStream1')
    cached_stream_2 = cached.get('cStream2')

    # cache first data stream
    if cached_stream_1:
        list_stream_1 = json.loads(cached_stream_1)
        list_stream_1.append(content_1)
        cached.set('cStream1', json.dumps(list_stream_1))
    else:
        list_stream_1.append(content_1)
        cached.set('cStream1', json.dumps(list_stream_1))

    # cache second data stream
    if cached_stream_2:
        list_stream_2 = json.loads(cached_stream_2)
        list_stream_2.append(content_2)
        cached.set('cStream2', json.dumps(list_stream_2))
    else:
        list_stream_2.append(content_2)
        cached.set('cStream2', json.dumps(list_stream_2))

    # return streams
    return {'first': list_stream_1, 'second': list_stream_2}
