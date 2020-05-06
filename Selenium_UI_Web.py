# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.google.com')
#
# print(driver.title)
#
# driver.quit()

# --------------------------------------------------
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get("www.google.com")
#
# driver.find_elements_by_id("userA")
#
# element = driver
# from selenium import webdriver
#
# driver = webdriver.chrome()
#
# driver.get()
#----------------------------------------------------------
# import from time import sleep
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get("http://www.google.com/")
#
# driver.find_element_by_css_selector("#user").send_keys("admin")
# sleep(3)
#
# driver.find_element_by_css_selector("#password").send_keys("123456")
# sleep(3)
#
# driver.find_element_by_css_selector("#tel").send_keys("1861111111")
# sleep(3)
#
# driver.find_element_by_css_selector("mail").send_keys("123@gmail.com")
# sleep(3)
#
# driver.find_element_by_css_selector(".telA").clear()
# driver.find_element_by_css_selector("tel").send_keys("1860000000")
# sleep(3)
#
# driver.find_element_by_css_selector("button").click()
# sleep(3)
#
# driver.quit()

# -----------------------------------
# from time import sleep
#
# from selenium import webdriver
#
# driver = webdriver.Chrome
#
# driver.get("http://www.google.com/")
# sleep(3)
#
# driver.maximize_window()
# sleep(3)

# ------------------------------------------------------
# from time import sleep
#
# from selenium import webdriver
#
# driver = webdriver.Chrome
#
# driver.get("http://www.google.com")
#
# size = driver.find_element_by_css_selector("#user").size
# print("the size of text: ",size)
#
# text = driver.find_element_by_link_text("seek").text
# print("the text of alink: ",text)
#
# get_attribute = driver.find_element_by_link_text("seek").get_attribute("href")
# print("the value of alink: ".get_attribute)
#
# print("--------------------------------------------")
#
# title = driver.title
# print("the titlte: ",title)
#
# current_url = driver.current_url
# print("the url: ",current_url)
#
# print("--------------------------------------------")
#
# is_displayed = driver.find_element_by_css_selector("span").is_displayed()
# print("span: ", is_displayed)
#
# is_enabled = driver.find_element_by_css_selector("#cancel").is_enabled()
# print("the button enabled: ",is_enabled)

# ---------------------------------------------------------------------------
# from time import sleep
#
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("www.google.com")
#
# element = driver.find_element_by_css_selector("#user")
# ActionChains(driver).context_click(element).perform()
#
# driver.find_element_by_css_selector("#user").send_keys(Keys.BACK_SPACE)
# sleep(2)
#
# driver.find_element_by_css_selector("#user").send_keys(Keys.CONTROL,'a')
#
# sleep(2)
#
# driver.find_element_by_css_selector("#user").send_keys(Keys.CONTROL,'c')
#
# sleep(2)
#
# driver.find_element_by_css_selector("#user").send_keys(Keys.CONTROL,'v')
#
#
# sleep(2)
#
# driver.quit()
#
# --------------------------------------------------------------------------------
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("www.google.com")
# sleep(2)
#
# elements = (By.CSS_SELECTOR,"#user")
# #
# # WebDriverWait(driver,10).until(EC.presence_of_elements_located(elements)).send_keys("admin")
# wait = WebDriverWait(driver,10)
# elements = wait.until(EC.presence_of_element_located(elements))
# elements.send_keys("admin")
# sleep(2)
#
# # wait.until(EC.presence_of_element_located(elements))
#
#
#
# sleep(2)
#
# driver.quit()
# ------------------------------------------------

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.get("www.google.com")
#
# #option 1_name
# tags = driver.find_element_by_tag_name("option")
# for tag in tags:
#     if tag.get_atribute("value") == "sh":
#         sleep(2)
#         tag.click()
# for tag in tags:
#     if tag.text == "chongqing":
#         sleep(2)
#         tag.click()
# for tag in tags:
#     if tag.get_atribute("value") == "gz":
#         sleep(2)
#         tag.click()
#
# #option2_css
# driver.find_element_by_css_selector("[value = 'sh'").click()
# sleep(2)
# driver.find_element_by_css_selector("[value = 'qc'").click()
# sleep(2)
# driver.find_element_by_css_selector("[value = 'gz'").click()
# sleep(2)
#
# #option3_Select_only for select
# webelement = driver.find_element_by_css_selector("seleect")
#
#
# Select(webelement).select_by_index(1)
# sleep(2)
#
# Select.select_by_index(2)
# Select.select_by_visible_text("sh")
# sleep(2)
#
# Select.select_by_index(3)
# sleep(2)
#
# select = Select(webelement)
#
# select.select_by_index(1)
# sleep(2)
#
# select.select_by_index(3)
# sleep(2)
#
# select.select_by_index(2)
# sleep(2)
#
# driver.quit()
# ---------------------------------------------------
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
# driver.get("www.google.com")
#
# driver.find_element_by_css_selector("#alert").click()
#
# alert = driver.switch_to.alert
#
# text = alert.text
# print("the text of alert is %s"%text)
#
# # alert.accept()
# alert.dismiss()
#
# driver.find_element_by_css_selector("#user").send_keys("admin")
# driver.find_element_by_css_selector("#password").send_keys("123456")
# driver.find_element_by_css_selector("#tel").send_keys("0211200010")
# driver.find_element_by_css_selector("#email").send_keys("123@gmail.com")
# sleep(2)
#
#
# driver.quit()
# ------------------------------------------------------------

# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.get("www.google.com")
#
# js1 = "window.scrollTo(0,10000)"
# driver.execute_script(js1)
# sleep(2)
#
# js2 = "window.scrollTo(0,0)"
# driver.execute_script(js2)
# sleep(2)
#
# driver.quit()

# -------------------------------------------------

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

str = ("id":"userId","name": "tsstName")

driver.add_cookie(str)

cookies = driver.get_cookies()

print("-------------------------")

print(cookies)

driver.quit()







