from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.in/JBL-Adaptive-Cancellation-Playtime-Compatible/dp/B0B1SJ7YSK/ref=pd_ci_mcx_mh_mcx_views_0_image")
driver.get("https://www.python.org/")
# price_rupees = driver.find_element(By.CLASS_NAME, value = "a-price-whole")
# print(f"${price_rupees}")

search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value = "submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value = ".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.get_attribute("href"))




# driver.close() closes that particular tab
# driver.quit() quits entire browser
driver.quit()


