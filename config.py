import os

from python_anticaptcha import AnticaptchaClient

CAPTCHA_KEY = 'ВАШ КЛЮЧ'  # https://anti-captcha.com/
# PROXY_KEY = ''  # https://best-proxies.ru/

anticaptcha_client = AnticaptchaClient(CAPTCHA_KEY)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/90.0.4430.85 Safari/537.36'}

WORK_SITE_DIR = f'file:///{os.getcwd()}//js//index.html'  # создание сайта с API WAX

headless = True  # скрыто ли окно браузера


# не забываем что куки надо положить в папку /Cookies
























MAIN_ACCOUNT = 'aestk.wam' # аккаунт смарт контракта для работы бота. НЕ менять.
