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
    message = ''
    for r in resources:
        print(r)
        pingresult = 'Ok' if pinging(r) == 0 else 'not avail'
        logging.info('{} ({}) -- {}'.format(r[0], r[1], pingresult))
        message += '{} ({}) -- {}\n'.format(r[0], r[1], pingresult)
    print(message)

if __name__ == '__main__':
    main()
