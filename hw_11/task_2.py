# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = 'https://fix-online.sbis.ru'

try:
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    driver.get(sbis_site)
    sleep(1)
    # Поиск поля логин на сайте
    login = driver.find_element(By.NAME, 'Login')
    # Ввод логина и переход на ввод пароля
    login.send_keys('pers_zp', Keys.ENTER)
    sleep(1)
    # Проверка на то, что введено в поле логин
    assert login.get_attribute('value') == 'pers_zp'

    # Поиск поля пароль на сайте
    password = driver.find_element(By.NAME, 'Password')
    # Ввод пароля и авторизация
    password.send_keys('pers_zp654321', Keys.ENTER)
    sleep(7)

    # Поиск Контакты в аккордеоне
    contact = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"] .NavigationPanels-Accordion__title')
    # Проверка, что кнопка присутсвует
    assert contact.is_displayed()
    # Нажать на кнопку "Контакты"
    contact.click()
    sleep(5)
    # В новом аккордеоне снова найти Контакты
    contact_more = driver.find_element(By.CSS_SELECTOR, '[name="headTitle"] .NavigationPanels-SubMenu__headTitle')
    # Проверка, что кнопка присутсвует
    assert contact_more.is_displayed()
    # Нажать на кнопку "Контакты"
    contact_more.click()
    sleep(5)
    # Поиск кнопки + для отправки сообщения
    plus = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    # Проверка, что кнопка присутсвует
    assert plus.is_displayed()
    # Нажать на кнопку +
    plus.click()
    sleep(3)
    # Отображение панели поиска сотрудника для отправки сообщения
    #panel_fio = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate-content')
    panel_fio = driver.find_element(By.CSS_SELECTOR, '.addressee-selector-popup__browser')
    # Проверка, что панель присутсвует
    assert panel_fio.is_displayed()

    # Поиск поля для ввода
    search_fio = driver.find_element(By.CSS_SELECTOR, '.addressee-selector-popup__browser .controls-InputBase__nativeField_hideCustomPlaceholder')
    # Проверка, что поле для ввода присутсвует
    assert search_fio.is_displayed()

    # Ввод ФИО в строку поиска
    search_fio.send_keys('Крюков Борис Викторович', Keys.ENTER)
    sleep(2)
    # Проверка на то, что введено в поле поиска
    #assert login.get_attribute('value') == 'Крюков Борис Викторович'

    # Отображение найденного ФИО
    fio_employer = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-selector__addressee')
    # Проверка, что найденный сотрудник отображается
    assert fio_employer.is_displayed()
    # Выбрать найденного адресата
    fio_employer.click()
    sleep(2)

    # Поиск поля для ввода текста сообщения
    message_txt = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    assert message_txt.is_displayed()
    # Ввод сообщения
    message_txt.send_keys('Текст сообщения')
    sleep(3)

    # Поиск кнопки для отправки
    send_btn = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    assert send_btn.is_displayed()
    # Отправка сообщения
    send_btn.click()
    sleep(5)

    # Поиск отправленного сообщения в реестре
    seng_msg = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__message-text')
    # берем именно последнее сообщение
    last_msg = seng_msg[0]
    # Сверить текст отправленного сообщения
    msg_txt = 'Текст сообщения'
    assert last_msg.text == msg_txt

    # Навести на сообщения для открытия до меню
    action = ActionChains(driver)
    action.move_to_element(last_msg).perform()
    sleep(2)
    # Поиск кнопки удаления сообщения при наведении на строку
    del_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    assert del_btn.is_displayed()
    # Удаление сообщения в архив
    del_btn.click()
    sleep(2)

    # Проверка отсутствия удаленного сообщения в реестре
    another_msg = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__message-text')
    # берем именно последнее сообщение
    find_del_msg = another_msg[0]
    # Сверить текст отправленного сообщения
    del_msg_txt = 'Текст сообщения'
    assert find_del_msg.text != del_msg_txt

finally:
    driver.quit()
