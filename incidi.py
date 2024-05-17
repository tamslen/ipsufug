from selenium.webdriver.common.by import By

guild_to_leave = driver.find_element(By.XPATH, f'//*[contains(@aria-label, " {guild}")]')
