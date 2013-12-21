#!/usr/bin/python
# -*- coding: utf8 -*-

'''
通过python获取本地 mac地址 ip地址

需要安装 cherrypy    
easy_install cherrypy
'''

import os
import uuid
import socket
import json
import time
import sys


import cherrypy


class LocalInfo(object):
    '''
    url /info/mac
    '''
    @cherrypy.expose
    def mac(self, **kwargs):
        params = kwargs
           
        node = uuid.getnode()
        mac = uuid.UUID(int = node).hex[-12:]
        
        if params.get('callback') != None:
            return str(params.get('callback')) + '(' + json.dumps({'mac': mac}) + ')'
        else:
            return json.dumps({'mac': mac})
    
    @cherrypy.expose
    def ip(self):
        myname = socket.getfqdn(socket.gethostname())
        ip = socket.gethostbyname(myname)
        
        if params.get('callback') != None:
            return str(params.get('callback')) + '(' + json.dumps({'ip': ip}) + ')'
        else:
            return json.dumps({'ip': ip})

class Clock:
    def __init__(self):
        self.settings = { 
                'global': {
                    'server.socket_port' : 30051,
                    'server.socket_host': '0.0.0.0',
                    'server.socket_file': '',
                    'server.socket_queue_size': 100,
                    'server.protocol_version': 'HTTP/1.1',
                    'server.log_to_screen': True,
                    'server.log_file': '',
                    'server.reverse_dns': False,
                    'server.thread_pool': 200,
                    'server.environment': 'production',
                    'engine.timeout_monitor.on': False
                }
        }
        
    def start(self):
        cherrypy.engine.autoreload.stop()
        cherrypy.engine.autoreload.unsubscribe()
        
        cherrypy.config.update(self.settings)
        cherrypy.tree.mount(LocalInfo(), '/info')
        cherrypy.engine.start()
        
    def stop(self):
        cherrypy.engine.stop()
        cherrypy.engine.exit()
        time.sleep(0.1)
        
    def restart(self):
        self.stop()
        time.sleep(1)
        self.start()


                
def test():
    clock = Clock()
    clock.start()
    
if __name__ == '__main__':
    test()
