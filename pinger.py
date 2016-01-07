#!/usr/bin/env python3
# -*-coding: utf-8 -*-

# Скрипт пингует ресурсы в сети и отправляет e-mail


import sys
import logging
import subprocess
import smtplib
import time
import platform

logname = 'logpinger.log'

fromaddr = 'ollo@netbook.home'
toaddr = 'okibkursk-it@yandex.ru'
subject = 'Ping results: ' + time.strftime('%a, %d %b %Y %H:%M:%S')

logging.basicConfig(format='%(asctime)s %(message)s', 
                            filename=logname, 
                            level=logging.DEBUG)

resources = (('localhost', '127.0.0.1'),
             ('Google DNS', '8.8.8.8'),
             ('ya.ru', '213.180.193.3'),
             ('nothing host', '192.168.0.5')
,)

def mail_send(message):
    msg = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n'.format(fromaddr, toaddr, subject)
    msg += message
    server = smtplib.SMTP('localhost')
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print(msg)
    logging.info('message sended: ' + msg)

def pinging(res):
   command = ['ping', '-c2', '-W1', res[1]]
   return subprocess.call(command)

def main():
    logging.info('pinger started...')
    message = platform.platform() + '\n'
    for r in resources:
        print(r)
        pingresult = 'Ok' if pinging(r) == 0 else 'not avail'
        logging.info('{} ({}) -- {}'.format(r[0], r[1], pingresult))
        message += '{} ({}) -- {}\n'.format(r[0], r[1], pingresult)
    mail_send(message)

if __name__ == '__main__':
    main()
