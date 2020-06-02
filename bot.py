from config import keys
from selenium import webdriver
import time

#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())


# do this with a headless browser?
# speed? different language?

# python decorator to record time of the order function
def timeme(method):
    def wrapper(*args, **kw):
        start_time = int(round(time.time() * 1000))
        result = method(*args, **kw)
        end_time = int(round(time.time() * 1000))
        print("Execution time: {}".format((end_time - start_time)/1000))
        return result
    return wrapper

# x path a way to target specific tags in the html file (buttons)
@timeme
def order(k):

    driver.get(k['product_url'])
    # size, options are relative to whats in stock and what the item is
    driver.find_element_by_xpath('//*[@id="s"]/option[1]').click()
    # add to cart
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    # wait for checkout button to appear
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k['tel'])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k['address'])
    # if you need a box number, apt number, etc
    # driver.find_element_by_xpath('//*[@id="oba3"]').sendkeys(k['apt_num'])

    # zip code
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k['zip'])
    # card number
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k['card_num'])
    # card exp month
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(k['card_exp_month'])).click()
    # card exp year 1 is 2020 2 is 2021, etc
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(k['card_exp_year'])).click()
    # cvv
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k['cvv'])
    # terms and conditions
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    # process payment button
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()
    # now solve the captcha!!!!!!!!



if __name__ == "__main__":
        driver = webdriver.Chrome("./chromedriver")
        #driver = webdriver.Safari()
        order(keys)