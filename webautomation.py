from selenium import webdriver

driver = webdriver.Chrome("--log-level=3")
driver.get('https://login.salesforce.com')

searchbox = driver.find_element_by_xpath('//*[@id="username"]')
searchbox.send_keys('nvillalobos@labsxd.com.labsxd')

searchbox = driver.find_element_by_xpath('//*[@id="password"]')
searchbox.send_keys('S4l3sf0rc3')

searchButton = driver.find_element_by_xpath('//*[@id="Login"]')
searchButton.click()

searchtitle = driver.title

if searchtitle == 'Iniciar sesión | Salesforce':
    driver.get_screenshot_as_file("result_fail_login.png")
else:
    print('Login Satisfactorio')
