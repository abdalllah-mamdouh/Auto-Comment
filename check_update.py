# !/usr/bin/env python
# -*- coding: utf-8 -*-
# V: 1.0
####################################################################
#                        Import Module
from colored import fg, bg, attr
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from requests_html import HTMLSession
import pyperclip
from os import getlogin


###################################################################

def check_up():
    ###################################################################
    #                       Static Variables & Colors
    # Request From Github Repositories/Project
    session = HTMLSession()
    req = session.get('https://github.com/AbdallahOfficial/Auto-Comment/blob/main/2-%20script.py')

    # Locate Attribute By Css Class
    row = req.html.find('.pl-c')[0]

    # Remove Space From The ٌ Result (If found)
    rw = row.text.strip()
    print(rw)
    # Open Main File
    file = open("2- script.py", "r")

    # Check Version From First Line & Remove Space (If found)
    file = file.readline().strip()

    ###################################################################

    print("%s%s Checking Updates, Please Wait .. %s" % (fg(3), bg(15), attr(0)))

    if rw == file:
        print("%s%s Script Updated! %s" % (fg(46), bg(15), attr(0)))
    elif rw != file:
        print("%s%s Downloading New Updates, Please Wait ..../ %s" % (fg(196), bg(15), attr(0)))
        # Locate Attribute By Css Class
        row = req.html.find('.pl-c')[1]

        # Remove Space From The ٌ Result (If found) & Comment "#"
        result = row.text.strip("# ")
        # get Name your PC
        pc_user = getlogin()

        # Add Options For Open WebDriver In incognito Page
        options = Options()
        options.add_argument("--incognito")
        # open WebDriver From PATH
        driver = webdriver.Chrome(r"C:/Users/" + pc_user + "/Desktop/Auto-Comment/chromedriver.exe", options=options)
        driver.minimize_window()
        # Go to Facebook Website
        driver.get(result)
        copy_code = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[3]/div[3]/div[1]/div[1]/div[3]/span[1]/a[1]")
        copy_code.click()
        code = pyperclip.paste()
        driver.close()
        with open('2- script.py.py', 'w') as f:
            f.write(code)
        print("%s%s Script Updated! %s" % (fg(46), bg(15), attr(0)))
