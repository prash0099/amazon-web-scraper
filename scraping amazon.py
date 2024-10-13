from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import csv

# Headless mode for Firefox
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

product = 'laptop'

# Open CSV to write data
with open('scraped_product_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product Name', 'Price', 'Product Link'])

    for i in range(1, 3):
        driver.get(f"https://www.amazon.in/s?k={product}&page={i}")
        wait = WebDriverWait(driver, 20)
        product_in = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.sg-col-20-of-24.s-result-item.s-asin')))
        
        for info in product_in:
            try:
                name = info.find_element(By.CSS_SELECTOR, '.a-size-medium.a-color-base.a-text-normal').text
            except:
                name = 'N/A'
            try:
                price = info.find_element(By.CLASS_NAME, 'a-price-whole').text
            except:
                price = 'N/A'
            try:
                href = info.find_element(By.CSS_SELECTOR, 'a.a-link-normal.s-underline-text.s-link-style.a-text-normal').get_attribute('href')
            except:
                href = 'N/A'
            
            writer.writerow([name, price, href])

driver.close()
