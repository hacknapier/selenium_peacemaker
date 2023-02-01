import src.selenium_peacemaker as selenium_peacemaker
from time import sleep
import json

proxy = {
    "host": "proxy.packetstream.io",
    "port": 31112,
    "user": "ploetzeneder",
    "password": "83G2cIcqPTV47Fd7",
    "scheme": "http"
}
proxy = json.dumps(proxy)

selenium = selenium_peacemaker.Stealth(mobile=True, proxy=proxy)
driver = selenium.stealth()
driver.get('https://www.wieistmeineip.de')
sleep(90)
driver.close()