from selenium import webdriver
from time import sleep
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
AMAZON_URL = config_ini['SiteURL']['amazon'] # PS5商品ページ
AMAZON_ITEM = "PlayStation 5 デジタル・エディション"

def is_amazon_buyable():
    """
    該当商品のページを開いているかcheckする
    開いていた場合に注文可能かcheckする

    Returns:
        [str]: 商品があれば'buyable!'、なければ空文字
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)


    driver.get(AMAZON_URL)

    page_title = driver.title
    if AMAZON_ITEM not in page_title:
        return ""
    else:
        is_buyable = driver.find_element_by_id('rightCol').text
        if "カートに入れる" in is_buyable:
            return "buyable!"
        else:
            return ""

    """
    # デジタルエディション版のボタンをクリック
    driver.find_element_by_id("a-autoid-9-announce").click()

    sleep(10)
    is_buyable = driver.find_element_by_class_name('a-button-input').get_attribute("value")

    driver.close()
    driver.quit()
    return is_buyable
    """

if __name__ == '__main__':
    is_amazon_buyable()
