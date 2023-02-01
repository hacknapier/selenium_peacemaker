import src.selenium_peacemaker as selenium_peacemaker
from time import sleep

selenium = selenium_peacemaker.Stealth(mobile=False)
driver = selenium.stealth()
driver.get('https://www.google.com')
sleep(90)
driver.close()