from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# pip install selenium
# download compatible version of chromedriver and add its path to environment variables

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("Please scan QR code and press any key to continue")


while True:
    name = input("Enter the receiver's name properly and it is case sensitive: ")
    receiver = driver.find_element_by_css_selector(f'span[title="{name}"]')
    receiver.click()
    textinput = driver.find_element_by_xpath(r"/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
    n = int(input("Enter the number of times you want to send the message: "))
    message = input("Enter the message: ")
    delay = float(input("Enter the minutes after which you want to send the message: "))
    time.sleep(delay*60) # this will delay the sending
    for i in range(n):
        textinput.send_keys(message)
        textinput.send_keys(Keys.RETURN)
    end = input("Enter exit to exit the program else just press enter: ")
    if end == "exit":
        break