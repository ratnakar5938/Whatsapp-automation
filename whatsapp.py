from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# pip install selenium
# download compatible version of chromedriver and add its path to environment variables

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("Please scan QR code and press any key to continue")


receiver = driver.find_element_by_css_selector('span[title="Amit jio"]')
receiver.click()

textinput = driver.find_element_by_xpath(r"/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
time.sleep(15) # this will delay the sending
for i in range(20):
    textinput.send_keys("Hemlo domst")
    textinput.send_keys(Keys.RETURN)
