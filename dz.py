# from selenium import webdriver
# from time import sleep
# import datetime
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# file=open('Selenium_practice','a')
# option=webdriver.ChromeOptions()
# option.add_experimental_option('detach',True)
# driver=webdriver.Chrome(options=option)
#
# #  ВХОД НА САЙТ
# def set_up():
#     driver.get('http://www.saucedemo.com')
#     driver.maximize_window()
#     print(f'Вход на сайт www.saucedemo.com')
#
# # АВТОРИЗАЦИЯ
# def login():
#     user_name=driver.find_element(By.XPATH,'//input[@id="user-name"]')
#     login='standard_user'
#     user_name.send_keys(login)
#     file.write('Success write login\n')
#     user_pass=driver.find_element(By.XPATH,'//input[@id="password"]')
#     password='secret_sauce'
#     user_pass.send_keys(password)
#     file.write('Success write password\n')
#     login_butt=driver.find_element(By.XPATH,'//input[@id="login-button"]')
#     login_butt.click()
#     file.write('Success click login\n')
#     print(f'Успешная авторизация')
#
# # ПРОВЕРКА ПЕРЕХОДА В КАТАЛОГ
# def test_login_redirect():
#     correct_url='https://www.saucedemo.com/inventory.html'
#     get_url=driver.current_url
#     assert  correct_url==get_url,'test_login_redirect is Failed'
#     file.write('test_login_redirect is Ok\n')
# def test_context_after_login_is_correct():
#     correct_text='Products'
#     current_text=driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
#     sleep(1)
#     # driver.save_screenshot('Test_task\\screenshot_test_context_after_login_is_correct_'
#     #                        f'{datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')}.png')
#     assert correct_text==current_text.text,'test_context_after_login_is_correct is Failed'
#     file.write('test_context_after_login_is_correct is Ok\n')
#     print(f'Переход в каталог')
#
# # ДОБАВЛЕНИЕ ТОВАРОВ В КОРЗИНУ И СОХРАНЕНИЕ ИХ НАЗВАНИЯ И ЦЕНЫ В ПЕРЕМЕННЫЕ
# def add_to_cart():
#     first_product_button=driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]')
#     first_product_button.click()
#     first_product_name=driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div')
#     global name_first_product
#     name_first_product=first_product_name.text
#     #print(name_first_product)
#     first_product_price=driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
#     global price_first_product
#     price_first_product=first_product_price.text.replace('$','')
#     print(f'Первый товар в корзине: {name_first_product}, Цена: {price_first_product}')
#     second_product_button=driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
#     second_product_button.click()
#     second_product_name=driver.find_element(By.XPATH,'//*[@id="item_1_title_link"]/div')
#     global name_second_product
#     name_second_product=second_product_name.text
#     second_product_price=driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div')
#     global price_second_product
#     price_second_product=second_product_price.text.replace('$','')
#     print(f'Второй товар в корзине: {name_second_product}, Цена: {price_second_product}')
#     global sum
#     sum=float(price_first_product)+float(price_second_product)
#     print(f'Сумма выбранных товаров: {sum}')
#     cart=driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
#     cart.click()
#     print(f'Товары добавлены в корзину')
#
# # ПРОВЕРКА ПЕРЕХОДА В КОРЗИНУ
# def test_to_cart_redirect():
#     correct_url='https://www.saucedemo.com/cart.html'
#     get_url=driver.current_url
#     assert  correct_url==get_url,'test_to_cart_redirect is Failed'
#     file.write('test_to_cart_redirect is Ok\n')
# def test_context_after_to_cart_is_correct():
#     correct_text='Your Cart'
#     current_text=driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
#     sleep(1)
#     # driver.save_screenshot('Test_task\\screenshot_test_context_after_to_cart_is_correct_'
#     #                        f'{datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')}.png')
#     assert correct_text==current_text.text,'test_context_after_to_cart_is_correct is Failed'
#     file.write('test_context_after_to_cart_is_correct is Ok\n')
#     checkout_button=driver.find_element(By.XPATH,'//*[@id="checkout"]')
#     checkout_button.click()
#     print(f'Переход в корзину')
#
# # ПРОВЕРКА ПЕРЕХОДА НА СТРАНИЦУ ВВОДА ДАННЫХ КЛИЕНТА
# def test_checkout_redirect():
#     correct_url='https://www.saucedemo.com/checkout-step-one.html'
#     get_url=driver.current_url
#     assert  correct_url==get_url,'test_checkout_redirect is Failed'
#     file.write('test_checkout_redirect is Ok\n')
# def test_context_after_checkout_is_correct():
#     correct_text='Checkout: Your Information'
#     current_text=driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
#     sleep(1)
#     # driver.save_screenshot('Test_task\\screenshot_test_context_after_checkout_is_correct_'
#     #                        f'{datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')}.png')
#     assert correct_text==current_text.text,'test_context_after_checkout_is_correct is Failed'
#     file.write('test_context_after_checkout_is_correct is Ok\n')
#     print(f'Подтвержение и переход к оформлению заказа')
#
# # ВВОД ДАННЫХ КЛИЕНТА
# def your_information():
#     first_name=driver.find_element(By.XPATH,'//*[@id="first-name"]')
#     name1='Ivan'
#     first_name.send_keys(name1)
#     file.write('Success write first_name\n')
#     last_name=driver.find_element(By.XPATH,'//*[@id="last-name"]')
#     name2='Ivanov'
#     last_name.send_keys(name2)
#     file.write('Success write last_name\n')
#     postalCode=driver.find_element(By.XPATH,'//*[@id="postal-code"]')
#     zip='1111111111'
#     postalCode.send_keys(zip)
#     file.write('Success write postalCode\n')
#     continue_button=driver.find_element(By.XPATH,'//*[@id="continue"]')
#     continue_button.click()
#     print(f'1 шаг оформления. Ввод данных клиента')
#
# # ПРОВЕРКА ПЕРЕХОДА НА СТРАНИЦУ С ОПИСАНИЕМ И ПОДТВЕРЖЕНИЕМ ЗАКАЗА
# def test_overview_redirect():
#     correct_url='https://www.saucedemo.com/checkout-step-two.html'
#     get_url=driver.current_url
#     assert  correct_url==get_url,'test_overview_redirect is Failed'
#     file.write('test_overview_redirect is Ok\n')
# def test_context_after_overview_is_correct():
#     correct_text='Checkout: Overview'
#     current_text=driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
#     sleep(1)
#     # driver.save_screenshot('Test_task\\screenshot_test_context_after_overview_is_correct_'
#     #                        f'{datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')}.png')
#     assert correct_text==current_text.text,'test_context_after_overview_is_correct is Failed'
#     file.write('test_context_after_overview_is_correct is Ok\n')
#     print(f'2 шаг оформления. Описание товаров')
#
# # СВЕРКА СОХРАНЁННЫХ ПЕРЕМЕННЫХ С ФАКТИЧЕСКИМИ ЗНАЧЕНИЯМИ НА САЙТЕ
# def data_comparison():
#     first_name=driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div')
#     name_first=first_name.text
#     first_price=driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
#     price_first=first_price.text.replace('$','')
#     print(f'Первый товар в заказе: {name_first}, Цена: {price_first}')
#     second_name=driver.find_element(By.XPATH,'//*[@id="item_1_title_link"]/div')
#     name_second=second_name.text
#     second_price=driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
#     price_second=second_price.text.replace('$','')
#     print(f'Второй товар в заказе: {name_second}, Цена: {price_second}')
#     total_sum=driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
#     sum_total=float(total_sum.text.replace('Item total: $', ''))
#     print(f'Сумма товаров в заказе: {sum_total}')
#     assert name_first_product==name_first,'test_first_name_is_correct is Failed'
#     file.write('test_first_name_is_correct is Ok\n')
#     assert price_first_product==price_first,'test_ffirst_price_is_correct is Failed'
#     file.write('test_first_price_is_correct is Ok\n')
#     assert name_second_product==name_second, 'test_second_name_is_correct is Failed'
#     file.write('test_second_name_is_correct is Ok\n')
#     assert price_second_product==price_second, 'test_second_price_is_correct is Failed'
#     file.write('test_second_price_is_correct is Ok\n')
#     assert sum==sum_total, 'test_sum_is_correct is Failed'
#     file.write('test_sum_is_correct is Ok\n')
#     finish=driver.find_element(By.XPATH,'//*[@id="finish"]')
#     finish.click()
#     print(f'Проверка суммы заказа и оплата')
#
# # ПРОВЕРКА ПЕРЕХОДА НА СТРАНИЦУ  С СООБЩЕНИЕМ ОБ УСПЕШНОМ ЗАКАЗЕ
# def test_complete_redirect():
#     correct_url='https://www.saucedemo.com/checkout-complete.html'
#     get_url=driver.current_url
#     assert  correct_url==get_url,'test_complete_redirect is Failed'
#     file.write('test_complete_redirect is Ok\n')
# def test_context_after_complete_is_correct():
#     correct_text='Checkout: Complete!'
#     current_text=driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
#     sleep(1)
#     # driver.save_screenshot('Test_task\\screenshot_test_context_after_complete_is_correct_'
#     #                        f'{datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')}.png')
#     assert correct_text==current_text.text,'test_context_after_complete_is_correct is Failed'
#     file.write('test_context_after_complete_is_correct is Ok\n')
#     back_home_button=driver.find_element(By.XPATH,'//*[@id="back-to-products"]')
#     back_home_button.click()
#     print(f'Заказ успешно оформлен')
#
# # ПРОВЕРКА ВОЗВРАТА В КАТАЛОГ
# def test_return_to_catalog_redirect():
#     correct_url='https://www.saucedemo.com/inventory.html'
#     get_url=driver.current_url
#     assert  correct_url==get_url,'test_return_to_catalog_redirect is Failed'
#     file.write('test_return_to_catalog_redirect is Ok\n')
# def test_context_after_return_to_catalog_is_correct():
#     correct_text='Products'
#     current_text=driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
#     sleep(1)
#     # driver.save_screenshot('Test_task\\screenshot_test_context_after_return_to_catalog_is_correct_'
#     #                        f'{datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')}.png')
#     assert correct_text==current_text.text,'test_context_after_return_to_catalog_is_correct is Failed'
#     file.write('test_context_after_return_to_catalog_is_correct is Ok\n')
#     print(f'Возврат в каталог')
#
# # ВЫХОД ИЗ СИСТЕМЫ
# def logout():
#     menu_button = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
#     menu_button.click()
#     sleep(2)
#     logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
#     logout_button.click()
#     file.write('Success logout\n')
# def test_logout_redirect():
#     correct_url='https://www.saucedemo.com/'
#     get_url=driver.current_url
#     assert  correct_url==get_url,'test_logout_redirect is Failed'
#     file.write('test_logout_redirect is Ok\n')
# def test_context_after_logout_is_correct():
#     correct_text='Accepted usernames are:'
#     current_text=driver.find_element(By.XPATH,'//*[@id="login_credentials"]/h4')
#     # driver.save_screenshot('Test_task\\screenshot_test_context_after_logout_is_correct_'
#     #                        f'{datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')}.png')
#     assert correct_text==current_text.text,'test_context_after_logout_is_correct is Failed'
#     file.write('test_context_after_logout_is_correct is Ok\n')
#     print(f'Выход из системы')
#
#
# set_up()
# login()
# test_login_redirect()
# test_context_after_login_is_correct()
# add_to_cart()
# test_to_cart_redirect()
# test_context_after_to_cart_is_correct()
# test_checkout_redirect()
# test_context_after_checkout_is_correct()
# your_information()
# test_overview_redirect()
# test_context_after_overview_is_correct()
# data_comparison()
# test_complete_redirect()
# test_context_after_complete_is_correct()
# test_return_to_catalog_redirect()
# test_context_after_return_to_catalog_is_correct()
# logout()
# test_logout_redirect()
# test_context_after_logout_is_correct()
# file.close()


