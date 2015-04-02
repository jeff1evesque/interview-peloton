#!/usr/bin/python

## @memcached_settings.py
#  This file contains the required class methods required to set, and
#      get the memcache host, port, or the entire hostname.

## Class: Memcached_Settings, explicitly inherit 'new-style' class.
class Memcached_Settings(object):

    ## constructor:
    def __init__(self):
        self.host     = 'localhost'
        self.port     = '5000'
        self.hostname = self.host + ':' + self.port

    ## get_hostname
    def get_hostname(self):
        return self.hostname

    ## set_hostname
    def set_hostname(self, hostname):
        self.hostname = hostname

    ## set_host
    def set_host(self, host):
        self.host     = host
        self.hostname = host + ':' + self.port

    ## set_port
    def set_port(self, port):
        self.port     = port
        self.hostname = self.host + ':' + port
