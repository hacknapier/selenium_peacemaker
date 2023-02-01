__version__ = "1.0.0"

# Package:        selenium_peacemaker
# Description:    Stealth emulate and automate Chrome using profiles, proxy and selenium.
# License:        Copyright (c) 2023 Hack Napier
# Code:           https://github.com/hacknapier/selenium_peacemaker

from selenium import webdriver
from selenium_stealth import stealth
from selenium_profiles.driver import driver as mydriver
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
import json
import warnings
from . import __proxy__ as selenium_proxy
from . import __profile__ as profile

warnings.filterwarnings("ignore", category=DeprecationWarning)


class Stealth:

    def __init__(self, headless: bool = False, proxy=None, user_agent=None, mobile: bool = False):
        self._proxy     = proxy
        self._ua        = user_agent
        self._mobile    = mobile
        self._headless  = headless
        if self._proxy is not None:
            proxy = json.loads(proxy)
            self._proxy_host        = proxy['host']
            self._proxy_port        = proxy['port']
            self._proxy_user        = proxy['user']
            self._proxy_password    = proxy['password']
            self._scheme            = proxy['scheme']

    def stealth(self):
        if self._mobile is False:  # Windows
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.headless = self._headless

            # Auto install chrome driver
            if self._proxy is None:
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            else:  # Proxy and Custom User Agent
                driver = selenium_proxy.get_chromedriver_with_proxy(self._proxy_host, int(self._proxy_port),
                                                                    self._proxy_user,
                                                                    self._proxy_password, True, self._ua,
                                                                    self._headless)

            # Stealth selenium
            stealth(driver,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win32",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                    )
            driver.set_window_size(1024, 768)  # Hard coded window size
        else:  # Android emulation
            # Install chrome driver
            ChromeDriverManager().install()
            if self._proxy is None:
                _my_driver = mydriver()
                _options = webdriver.ChromeOptions()
                _options.headless = self._headless
                _my_driver.options = _options
                driver = _my_driver.start(profile.Android(), uc_driver=False)
            else:
                _my_driver = mydriver()
                _options = webdriver.ChromeOptions()
                _options.headless = self._headless
                _my_driver.options = _options
                driver = _my_driver.start(profile.Android_with_Proxy_Support(self._proxy_host, int(self._proxy_port),
                                                                             self._proxy_user,
                                                                             self._proxy_password, self._scheme),
                                          uc_driver=False)

        return driver

    def undetectable(self):
        driver = uc.Chrome()

        return driver

