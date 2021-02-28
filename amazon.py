from selenium import webdriver
from time import sleep
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
AMAZON_URL = config_ini['SiteURL']['amazon'] # PS5商品ページ

def is_amazon_buyable():
    """アマゾンに商品があるかcheckする

    Returns:
        [str]: 商品があれば'カートに入れる'、なければ空文字
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)


    driver.get(AMAZON_URL)
    # デジタルエディション版のボタンをクリック
    # テスト用にコメントアウト driver.find_element_by_id("a-autoid-9-announce").click()

    sleep(1)
    is_buyable = driver.find_element_by_class_name('a-button-input').get_attribute("value")

    driver.close()
    driver.quit()
    return is_buyable

if __name__ == '__main__':
    is_amazon_buyable()
