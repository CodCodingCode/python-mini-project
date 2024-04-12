# @author : Nathan Yan
# Description: This script scrapes the web for hackathons hosted by companies in the list below.
# @date : 2024-03-30


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from removeMonths import months
import time
import selenium

# List of companies to search for hackathons
list = ["OpenAI", "Deepmind", "Cohere", "EleutherAI", "Mistral", "META", "Microsoft", "IBM", "Google", "Tesla"]
driver = webdriver.Chrome()
possible_hackathons = []

# Scan through the list of companies and search for hackathons in the current month, 2024
for company in list:
    driver.get('https://www.google.com')
    try:
        # Search for hackathons hosted by the company
        input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))
        input_element.clear()
        search_query = f"{company} Hackathon '{months[0]}' 2024"
        input_element.send_keys(search_query + Keys.ENTER)
        link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "hackathon")))
        link.click()
        time.sleep(5)
        possible_hackathons.append(driver.current_url)
        driver.back()
    except TimeoutException:
        print(f"Element not found for {search_query}")

# Close the browser
driver.quit()

# Print the list of possible hackathons
print(possible_hackathons)
