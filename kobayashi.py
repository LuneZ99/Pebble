#!/usr/bin/env python
#-*- coding:utf-8 -*-
import subprocess
import os
import sys

def execute_cmd(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line
        if not line and proc.poll() is not None:
            break

if __name__ == '__main__':
    cmd = 'top'
    for line in execute_cmd(cmd):
        sys.stdout.write(line)


