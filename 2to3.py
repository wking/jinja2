#!/usr/bin/python3.3
import sys
from lib2to3.main import main

def run(fixer_pkg):
    ret = main(fixer_pkg)
    if ret:
        sys.exit(ret)

run('lib2to3.fixes')
run('custom_fixers')
