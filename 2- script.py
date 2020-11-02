# !/usr/bin/env python
# -*- coding: utf-8 -*-
# V: 1.0
####################################################################
#                        Import Module
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pyautogui
import pyfiglet
from colored import attr, bg, fg
from os import getlogin
from check_update import check_up
###################################################################
###################################################################
#                       Static Variables & Colors
slogan = 'Z A K'
fb = 'FB : https://www.facebook.com/zak9999m'
usageRights = 'Scripting By Abdallah Mamdouh. All rights reserved ©2020.'
version = "Auto Comment | Version: 1.0"
###################################################################

# print My Slogan & My FB Link
print(f"%s{pyfiglet.figlet_format(slogan)}%s" % (fg(1), attr(0)))
print(f'%s%s {usageRights} %s' % (fg(1), bg(15), attr(0)))
print(f'%s%s {fb} %s' % (fg(1), bg(15), attr(0)))
print(f'%s%s {version} %s' % (fg(1), bg(15), attr(0)))

check_up()

# get Name your PC
pc_user = getlogin()

# Add Options For Open WebDriver In incognito Page
options = Options()
options.add_argument("--incognito")
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)

# open WebDriver From PATH
driver = webdriver.Chrome(r"C:/Users/" + pc_user + "/Desktop/Auto-Comment/chromedriver.exe")
driver.implicitly_wait(5)

# Set Window Position & Size
driver.set_window_position(500, 0)
driver.set_window_size(465, 830)

# Go to Facebook Website
driver.get("https://www.facebook.com/login/")
sleep(1)

# Get & Write Username
username = driver.find_element_by_id("email")
usr = pyautogui.prompt("Type your UserName or Email", "UserName")
username.click()
username.send_keys(usr)
sleep(0.5)

# Get & Write Password
password = driver.find_element_by_id("pass")
psw = pyautogui.password("Type your Password", "Password", mask="*")
password.click()
password.send_keys(psw)
sleep(0.5)

# Click Login Button
login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/button")
login.click()
sleep(1.5)
# Check if Login Success Or Not
if driver.current_url == 'https://www.facebook.com/':
    print("%s%s Logging Success .. %s" % (fg(10), bg(15), attr(0)))
    link_acc = pyautogui.prompt("Type your Post Link", "Post Link")
    driver.get(link_acc)
    pyautogui.press("left", presses=6, interval=0.1)
    sleep(2)
    comment = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div["
        "1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[2]/span["
        "2]/div")
    comment.click()
    # Open & Loop In Words File
    with open('words.txt', 'r') as file:
        for line in file:
            for word in line.split():
                sleep(5)
                pyautogui.typewrite(word, 0.1)
                pyautogui.press("enter")
            print("=>", "%s%s Commented %s" % (fg(94), bg(15), attr(0)))
else:
    # Close your Browser if your information False
    print('%s%s Login Error!! %s' % (fg(1), bg(15), attr(0)))
    sleep(5)
    print("%s%s Prepare to Close your Browser .. %s" % (fg(1), bg(15), attr(0)))
    sleep(1)
    driver.close()
