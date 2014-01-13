__author__ = 'salmantariqmirza'

from selenium.webdriver.support.ui import Select

def get_rate(driver, country):
    country_select = Select(driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddCountryTo"]'))
    country_select.select_by_visible_text(country[1])
    driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtAmount"]').send_keys("100")
    driver.find_element_by_class_name("btn-est-price").click()
    return driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_xRateBarDiv"]/div[1]/span[2]').text

def get_fee(driver, country, rate):
    country_select = Select(driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddCountryTo"]'))
    country_select.select_by_visible_text(country[1])
    driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtAmount"]').send_keys(rate)
    driver.find_element_by_class_name("btn-est-price").click()
    options = driver.find_elements_by_xpath('//*[@id="ContentPlaceHolder1_resultsDiv"]/div[2]/ul/li')
    fees = []
    for option in options:
        method = option.find_element_by_class_name("icon-bank-txt").text.replace("\n", " ")
        fee = option.find_element_by_class_name("starting-at-price").text
        fees.append([method, fee])
    return fees


