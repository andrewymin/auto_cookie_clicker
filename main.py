from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.common.action_chains import ActionChains

############## Getting browser to open on correct site ################

chrome_driver_path = Service(r"C:\Users\krazy\Desktop\Code\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

############## Getting clicks on cookie to automate ################
# actions = ActionChains(driver=driver)
browser_up = True
big_cookie = driver.find_element(By.ID, "bigCookie")

# testing
def every_five_sec():
    return time.time() + 5


check_store = every_five_sec()
end_game = time.time() + 60*5
test_sec = time.time() + 60
time.sleep(1)

while browser_up:
    big_cookie.click()
    if time.time() > check_store:
        total_cookies = driver.find_element(By.CSS_SELECTOR, "#sectionLeft #cookies").text.split()[0]
        total_cookies_num = int(total_cookies.replace(",", ''))
        store_items = driver.find_elements(By.CSS_SELECTOR, ".content .price")

        for item in store_items[::-1]:
            # Find what the index of item is first
            position = store_items.index(item)
            price_string = item.text
            if price_string == '':
                continue
            else:
                price = int(price_string.replace(",", ''))
                if total_cookies_num > price:
                    # If able to buy item than find item and use .click()
                    driver.find_element(By.ID, f"product{str(position)}").click()
        # adding another 5 sec for next loop
        check_store = every_five_sec()

    elif time.time() > end_game:
        cookies_per_sec = driver.find_element(By.CSS_SELECTOR, "#sectionLeft #cookies").text.split(":")[1]
        print(f"cookies/second: {cookies_per_sec}")
        break


