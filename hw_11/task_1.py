# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
sbis_site = "https://sbis.ru/"
sbis_site_next = "https://tensor.ru/about"


def find_btn(btn_class, btn_text):
    # Поиск кнопки
    btn = driver.find_element(By.CSS_SELECTOR, btn_class)
    btn_txt = btn_text
    # Проверка на название кнопки
    assert btn.text == btn_txt
    # Проверка, что кнопка присутствует на сайте
    assert btn.is_displayed()
    return btn


try:
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, "Не верно открыт сайт"
    tabs = driver.find_elements(By.CSS_SELECTOR, ".sbisru-Header__menu-item")
    assert len(tabs) == 4, "Должно быть 4 вкладки"

    # Поиск кнопки "Контакты"
    contact_btn = find_btn('.sbisru-Header__menu-item-1', 'Контакты')
    # Нажать на кнопку "Контакты"
    contact_btn.click()
    sleep(1)

    # Поиск баннера Тензор
    logo_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor[title = "tensor.ru"]')
    # Проверка, что баннер Тензор присутствует на сайте
    assert logo_btn.is_displayed()
    # Нажать на баннер Тензор
    logo_btn.click()
    sleep(1)

    # Переключиться на вторую вкладку
    driver.switch_to.window(driver.window_handles[1])

    # Поиск блока "Сила в людях"
    block = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content")
    # Проверка, что заголовок блока присутствует на сайте
    assert block.is_displayed()
    sleep(2)
    # Проверка на название блока
    name_block = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-Index__card-title")
    name_block_txt = 'Сила в людях'
    assert name_block.text == name_block_txt
    # Проверка, что заголовок блока присутствует на сайте
    assert name_block.is_displayed()
    sleep(2)

    # Поиск кнопки "Подробнее"
    more_btn = find_btn('.tensor_ru-Index__block4-content .tensor_ru-link', 'Подробнее')
    # Нажать на кнопку "Подробнее"
    # FIXME уточнить почему не кликается
    # more_btn.click()
    driver.execute_script("arguments[0].click();", more_btn)
    sleep(1)

    # Проверка, что перешли на сайт https://tensor.ru/about
    assert driver.current_url == sbis_site_next, "Не верно открыт сайт"
    sleep(2)
finally:
    driver.quit()

