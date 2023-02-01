from collections import defaultdict

DEVICE_JSON = {
  "Android": {
    "options": {
      "browser": {
      "gpu": False,
      "window_size": {"x":384,"y":700}}
    },
    "cdp": {
      "touch": True,
      "maxtouchpoints": 1,
      "emulation": {"mobile":True,"width": 384, "height": 700, "deviceScaleFactor": 4,
        "screenOrientation": {"type": "portraitPrimary", "angle": 0}},
      "useragent": {
                "platform": "Linux aarch64",
                "acceptLanguage":"en-US",
                "userAgent": "Mozilla/5.0 (Linux; Android 11; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36",
                "userAgentMetadata": {
                    "brands": [{"brand": "Google Chrome", "version": "105"}, {"brand": "Not)A;Brand", "version": "8"},
                               {"brand": "Chromium", "version": "105"}],
                    "fullVersionList": [{"brand": "Google Chrome", "version": "105.0.5195.136"},
                                        {"brand": "Not)A;Brand", "version": "8.0.0.0"},
                                        {"brand": "Chromium", "version": "105.0.5195.136"}],
                    "fullVersion": "105.0.5195.136",
                    "platform": "Android",
                    "platformVersion": "11.0.0",
                    "architecture": "",
                    "model": "HD1913",
                    "mobile": True,
                    "bitness": "",
                    "wow64": False}
      }
    }
  }
}


def return_default_profile(platform: str):
    from selenium_profiles.utils.utils import read_json
    profile = defaultdict(lambda: None)
    profile.update(DEVICE_JSON[platform])
    return profile


def Android():
    return return_default_profile("Android")

def Android_with_Proxy_Support(host: str, port: int, user: str, password: str, scheme: str):
    profile = return_default_profile("Android")
    host = host
    port = port
    user = user
    password = password
    scheme = scheme # http

    auth_proxy = {"host": host, "port": port, "username": user, "password": password, "scheme": scheme}

    profile["options"]["extensions"] = {"auth_proxy": auth_proxy}

    return profile
