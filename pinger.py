#!/usr/bin/env python3
# -*-coding: utf-8 -*-

# Скрипт пингует ресурсы в сети и отправляет e-mail


import sys
import logging
import subprocess
import smtplib
import time
import platform

def mail_send(fromaddr, toaddr, subject, message):
    msg = 'From: {}\r\nTo: {}\r\nSubject: {}\r\n'.format(fromaddr, toaddr, subject)
    msg += message
    server = smtplib.SMTP('localhost')
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print(msg)

def pinging(res):
   command = ['ping', '-c2', '-W1', res[1]]
   return subprocess.call(command)

def main():
    fromaddr = 'ollo@netbook.home'
    toaddr = 'okibkursk-it@yandex.ru'
    subject = 'Ping results: ' + time.strftime('%a, %d %b %Y %H:%M:%S')
    logname = 'logpinger.log'
    logging.basicConfig(format='%(asctime)s %(message)s', 
                                filename=logname, 
                                level=logging.DEBUG)
    logging.info('pinger started...')
    resources = (('localhost', '127.0.0.1'),
                 ('Google DNS', '8.8.8.8'),
                 ('ya.ru', '213.180.193.3'),
                 ('nothing host', '192.168.0.5')
                ,)
    message = platform.platform() + '\n'
    for r in resources:
        print(r)
        pingresult = 'Ok' if pinging(r) == 0 else 'not avail'
        logging.info('{:<20} ({:<15}) -- {}'.format(r[0], r[1], pingresult))
        message += '{:<20} ({:<15}) -- {}\n'.format(r[0], r[1], pingresult)
    mail_send(fromaddr, toaddr, subject, message)

if __name__ == '__main__':
    main()
