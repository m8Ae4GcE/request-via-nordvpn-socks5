from selenium.webdriver.common.by import By
from seleniumwire import webdriver

# list of NordVPN's SOCKS5 hosts
domains = [
    "socks-nl1.nordvpn.com",
    "socks-nl2.nordvpn.com",
    "socks-nl3.nordvpn.com",
    "socks-nl4.nordvpn.com",
    "socks-us1.nordvpn.com",
    "socks-us2.nordvpn.com",
    "socks-us3.nordvpn.com",
    "socks-us4.nordvpn.com",
    "socks-us5.nordvpn.com",
    "socks-us6.nordvpn.com",
    "socks-us7.nordvpn.com",
    "socks-us8.nordvpn.com",
    "socks-us9.nordvpn.com",
    "socks-us11.nordvpn.com",
    "socks-us12.nordvpn.com",
    "socks-us13.nordvpn.com",
    "socks-us14.nordvpn.com",
    "socks-us15.nordvpn.com",
    "socks-se1.nordvpn.com",
    "socks-se2.nordvpn.com",
    "socks-se3.nordvpn.com",
    "socks-se4.nordvpn.com",
    "socks-se5.nordvpn.com",
    "socks-ie1.nordvpn.com",
    "socks-ie2.nordvpn.com",
    "socks-ie3.nordvpn.com",
    "socks-ie4.nordvpn.com",
    "socks-ie5.nordvpn.com",
]

# choose srv from 'domains' list above
for choose_srv in range(len(domains)):

    options = {
        'proxy': {
            'https': f'socks5://<nordvpn_id>:<nordvpn_psswd>@{domains[choose_srv]}:1080',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }
    driver = webdriver.Chrome(seleniumwire_options=options)

    driver.get('https://www.whatismyip.com/')
    print(driver.find_element(By.CSS_SELECTOR, "#ipv4").text)

    driver.quit()
