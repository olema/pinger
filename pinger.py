#!/usr/bin/env python3
# -*-coding: utf-8 -*-

# Скрипт пингует ресурсы в сети и отправляет e-mail


import sys
import logging
import subprocess


logging.basicConfig(format='%(asctime)s %(message)s', 
                            filename='logpinger.log', 
                            level=logging.DEBUG)

resources = (('Google DNS', '8.8.8.8'),
             ('ya.ru', '213.180.193.3')
,)
def pinging(res):
   command = ['ping', '-c2', '-W1', res[1]]
   return subprocess.call(command)

def main():
    logging.info('pinger started...')
    for r in resources:
        print(r)
        logging.info('pinging {} ({}) .. - {}'.format(r[0], 
                       r[1],
                       'Ok' if not pinging(r) else 'not available..'))

if __name__ == '__main__':
    main()
