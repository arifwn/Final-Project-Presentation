from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.context_managers import cd, lcd
import datetime

env.hosts = []

def compile_less():
    local('lessc --compress static/less/main/main.less > static/css/main.css')
    
def compile_coffee():
    local('coffee -o static/js -c static/coffee/*.coffee')

def startserver():
    local('twistd web --path=.')

def stopserver():
    local('kill `cat twistd.pid`')
