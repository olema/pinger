#!/usr/bin/env python3
# -*-coding: utf-8 -*-

# Скрипт пингует ресурсы в сети и отправляет e-mail


import sys
import logging
import subprocess
import smtplib
import time
import platform
import os

def mail_send(fromaddr, toaddr, subject, message):
    from_header = 'From: router2 <{}>\r\n'.format(fromaddr)
    to_header = 'To: recipients <{}>,<{}>\r\n'.format(toaddr[0],
                                                      toaddr[1])
    subject_header = 'Subject: {}\r\n'.format(subject)
    msg = '{}{}{}\n{}'.format(from_header, to_header, subject_header, message)
    server = smtplib.SMTP('localhost')
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print(msg)

def pinging(res):
   command = ['ping', '-c2', '-W1', res[1]]
   return subprocess.call(command)

def main():
    fromaddr = 'semashko@kursktelecom.ru'
    toaddr = ['matushkin.oleg@gmail.com', 'okibkursk-it@yandex.ru']
    subject = 'Ping results: ' + time.strftime('%a, %d %b %Y %H:%M:%S')
    logname = os.path.dirname(sys.argv[0]) + os.sep + 'logpinger.log'
    logging.basicConfig(format='%(asctime)s %(message)s', 
                                filename=logname, 
                                level=logging.DEBUG)
    logging.info('===')
    logging.info('pinger started...')
    resources = (('localhost', '127.0.0.1'),
                 ('Google DNS', '8.8.8.8'),
                 ('Server HP', '192.168.0.2'),
                 ('NAS', '192.168.0.3'),
                 ('router ubuntu', '192.168.0.1'),
                 ('router wi-fi', '192.168.0.254'),
                 ('kursktelecom gate', '178.249.242.1'),
                )
    message = platform.platform() + '\n\n'
    for r in resources:
        print(r)
        pingresult = 'Ok' if pinging(r) == 0 else 'not avail'
        logging.info('{:<20} ({:<15}) -- {}'.format(r[0], r[1], pingresult))
        message += '{:<20} ({:<15}) -- {}\n'.format(r[0], r[1], pingresult)
    mail_send(fromaddr, toaddr, subject, message)

if __name__ == '__main__':
    main()
