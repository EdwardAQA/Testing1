import time #позволяет задавать ожидание между командами, пример: time.sleep(15)
import math #позволяет производить сложные математические расчеты
from selenium import webdriver #импортируем драйвер
from selenium.webdriver.common.by import By #импортируем библеотеку By (хороша для Page Object)
driver = webdriver.Chrome()  #переменная driver открывет браузер Хром

#для запуска кода в консоли используем команду venv\STEPIK1.py и меняем в зависимости от расположения и имени
#полный вариант запуска C:/Users/353/PycharmProjects/TAU/venv/STEPIK1.py

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#функция для теста 7. Рассчитывает выражение и возвращает результат в calc(x)

try:
    #тест1
    driver.get("https://stepik.org/lesson/25969/step/12")  #открываем ссылку
    time.sleep(15)   #время ожидания после выполнения предыдущего действия
    textarea = driver.find_element_by_css_selector(".textarea") #находим поле ввода по селектору
    time.sleep(5)
    textarea.send_keys("get()")   #вводим в поле значение из скобок
    time.sleep(5)
    submit_button = driver.find_element_by_css_selector(".submit-submission") #находим нужную кнопку по селектору
    submit_button.click() #кликаем на найденную кнопку
    time.sleep(5)

    #тест2
    driver.get("http://suninjuly.github.io/simple_form_find_task.html") #открываем другую ссылку
    time.sleep(15)
    button = driver.find_element_by_id("submit_button") #находим на открытой странице элемент с арибутом "submit_button"
    time.sleep(5)

    #тест3
    link = "http://suninjuly.github.io/simple_form_find_task.html" #записываем ссылку отдельной переменной
    driver.get(link) #находим ранее записанную ссылку переменной
    time.sleep(15)
    input = driver.find_element_by_tag_name("input") #ищем элемент с помощью имени тэга (так как в коде их несколько, найдет первый из них)
    input.send_keys("Ivan") #подставляем в найденный элемент значение "Ivan"
    time.sleep(5)
    button1 = driver.find_element(By.ID, "submit_button") #находим на открытой страице атрибут уже с помощбю библеотеки By
    time.sleep(5)
    button1.click() #кликаем на найденную кнопку
    time.sleep(5)

    #тест4
    driver.get("http://suninjuly.github.io/find_link_text") #открываем другую ссылку
    time.sleep(15)
    link1 = str(math.ceil(math.pow(math.pi, math.e)*10000)) #производим расчет с помощью подключенной библиотеки math и выводим в отдельную переменную
    time.sleep(5)
    link2 = driver.find_element_by_link_text(link1) #ищем элемент по полному совпаденю текста ссылки. В данном случае это результат расчета переменной link1
    link2.click() #кликаем на найденный элемент
    input1 = driver.find_element_by_tag_name("input") #ищем элемент с помощью имени тэга (так как в коде их несколько, найдет первый из них)
    input1.send_keys("Ivan") #вписываем значение Ivan в найденный элемент
    input2 = driver.find_element_by_name("last_name") #ищем элемент по значению атрибута name
    input2.send_keys("Petrov") #вписываем значение в найденный элемент
    input3 = driver.find_element_by_class_name("city") #ищем эдемент по значению атрибута class
    input3.send_keys("Smolensk") #вписываем значение в найденый элемент
    input4 = driver.find_element_by_id("country") #ищем элемент по значению уникального атрибута id
    input4.send_keys("Russia") #вписываем значение в найденный элемент
    button = driver.find_element_by_css_selector("button.btn") #ищем элемент по селектору (в основном,это комбинайия нескольких локаторов)
    button.click() #кликаем на найденный элемент
    time.sleep(30) #вреня на то,чтобы подтвердить действие

    #тест5
    driver.get("http://suninjuly.github.io/huge_form.html") #переходим по ссылке с множеством форм
    elements = driver.find_elements_by_tag_name ("input") #ищем все элементы с тегом input
    for element in elements: #цикл для каждого элемента среди всх элементов
        element.send_keys("Хуй") #ставим значение в скобках для элемента
    button = driver.find_element_by_css_selector("button.btn") #ищем элемент по составному селектору
    button.click() #кликаем на найденный элемент
    time.sleep(30)

    #тест6
    driver.get("http://suninjuly.github.io/simple_form_find_task.html") #переходим на другую страницу
    elements1 = driver.find_elements_by_tag_name("input")  # ищем все элементы с тегом input
    for element1 in elements1:  # цикл для каждого элемента среди всх элементов
        element1.send_keys("Выключай порно")  # ставим значение в скобках для элемента
    assert len(elements1) == 4 #проверка на то, что количество найденныйх элементов переменной elements1 равно 4
    button = driver.find_element_by_xpath("//button[@type='submit']") #поиск эдемента с помощью Xpath селектора
    button.click()  # кликаем на найденный элемент
    time.sleep(10)

    #тест7
    link = "http://suninjuly.github.io/math.html"
    driver.get(link)

    x_element = driver.find_elements_by_id("input_value") #находим элемент по id
    for value in x_element: #цикл, который перебирает все значения для переменной x_element
        x = value.text #берем элемент из цикла и считываем его текст между тегами
    y = calc(x) #считанный текст вычисляем с помощью функции

    textarea1 = driver.find_element_by_id("answer")
    textarea1.send_keys(y)

    radiobutton1 = driver.find_element_by_id("robotsRule") #находим элемент по id
    radiobutton1.click() #кликаем на найденный жлемент (переключатель), активируя его

    checkbox1 = driver.find_element_by_id("robotCheckbox") #находим элемент по id
    checkbox1.click() #кликаем на найденный жлемент (чек-бокс), активируя его

    checkbox1 = driver.find_element_by_class_name("btn")
    checkbox1.click()
    time.sleep(10)

    #тест8
    link = "http://suninjuly.github.io/math.html"

    driver.get(link)

    # проверяем значение атрибута checked у people_radio
    people_radio = driver.find_element_by_id("peopleRule") #находим элемент по id (переключатель)
    people_checked = people_radio.get_attribute("checked") #проверяем, что у переключателся есть атрибут cheked, то есть переключатель активирован по умолчанию
    print("value of people radio: ", people_checked) #в консоль выводится True, если переключатель активирован, и None, если нет
    assert people_checked is not None, "People radio is not selected by default" #выводится сообщение об ошибке с текстом в кавычках в консоль, если переключатель вернет значение None
    time.sleep(10)

    # проверяем значение атрибута checked у robots_radio
    robots_radio = driver.find_element_by_id("robotsRule") #поиск элемента по id (чек-бокс)
    robots_checked = robots_radio.get_attribute("checked") #проверяем, что у чек-бокса есть атрибут cheked, то есть переключатель активирован по умолчанию
    print("value of robots_radio: ", robots_checked) #в консоль выводится True, если чек-бокс активирован, и None, если нет
    assert robots_checked is None #выводится сообщение об ошибке в консоль, если переключатель вернет значение True
    time.sleep(10)

    # проверяем значение атрибута disabled у кнопки Submit
    button = driver.find_element_by_css_selector('.btn') #поиск элемента по селектору (кнопка)
    button_disabled = button.get_attribute("disabled") #проверяем, что кнопки есть атрибут disabled, то есть кнопка заблокирована по умолчанию
    print("value of button Submit: ", button_disabled) #в консоль выводится True, если кнопка заблокирована, и None, если нет
    assert button_disabled is not None #выводится сообщение об ошибке в консоль, если кнопка вернет значение None

finally:
    time.sleep(30)
    driver.quit() #закрываем браузер
# оставляем пустую строку в качестве хорошего тона (обязательно в unix/linux)
