# advanced-program-probe
Ми сьогодні з вами розберемося із тими технологіями, які вивчаються в Advanced Program.
	За результатом проходження даної програми студенти отримують кваліфікацію, яку можна описати як FullStack Python Development - це спеціаліст, який  може створити інтерфейс, а також створити серверну частину до цього інтерфейсу.
	На цьому занятті ми з вами створимо Інтернет-застосунок, який дозволяє проходити тести.
Для цього ми спочатку створимо серверний додаток на Python, а далі - підключемо до нього вже створений інтерфейс.


## Реєструємося на Pythonanywhere
[Pythonanywhere](https://www.pythonanywhere.com/registration/register/beginner/)  
<img src = "img/reg_01.jpg">  
Після реєстрації - ми попадемо на головну сторінку сервісу **Pythonanywhere**  

Далі - нам необхідно встановити бібліотеки, що нам вони знадобляться для запуску нашого серверного додатку.  
Для цього натиснемо кнопку **"Bash"**  
<img src = "img/lib_01.jpg">  
Відкривається консоль, в якій ми можемо встановити бібліотеку flask, написавши:  
**pip install flask**  
<img src = "img/lib_02.jpg">
<img src = "img/lib_03.jpg">
А також бібліотеку flask_cors, написавши:  
**pip install flask_cors**
<img src = "img/lib_04.jpg">
<img src = "img/lib_05.jpg">  
Далі - повернемося до головної сторінки сервісу:  
<img src = "img/lib_06.jpg">  
Та перейдемо на сторінку створення та управління **Web-додатками**
<img src = "img/web_01.jpg">  
Та створимо новий Web-додаток  
<img src = "img/web_02.jpg">  
Погодимся із стандартним ім'ям додатку (яке буде співпадати із ім'ям нашого логіну)  
<img src = "img/web_03.jpg">  
Оберемо Flask, як бібліотеку для створення Web-додатку.  
<img src = "img/web_04.jpg">  
Оберемо Python версії 3.10  
<img src = "img/web_05.jpg">  
Залишимо ім'я створюваного файлу за замовчуванням  
<img src = "img/web_06.jpg">  
В результаті - отримаємо створений додаток, відкрити який можна за посиланням, що відображається в вашому обліковому запису:  
<img src = "img/web_07.jpg">  
Відкривати краще в новій вкладці:  
<img src = "img/web_08.jpg">  
У вкладці, що відкриємться побачимо, що наш додаток працює із функціоналом за замовчуванням:
<img src = "img/web_09.jpg">  

## Зміна вихідного коду.
Для того, щоб змінити вихідний код на той, що нам потрібер - 
<img src = "img/files_01.jpg">  
Переходимо до папки "mysite":  
<img src = "img/files_02.jpg">  
Та відкриваємо файл "flask_app.py"  
<img src = "img/files_03.jpg">  
Ми бачимо рядок, який відоповідає за вивід тексту "Hello from Flask!"  
<img src = "img/files_04.jpg">  
Давайте змінимо його на "Hello World!" та збережемо зміни  
<img src = "img/files_06.jpg">  
Повернемося на розділ керування Web-додатком:  
<img src = "img/files_07.jpg">  
Оновимо додаток, та відкриємо посиалння ще раз:  
<img src = "img/files_08.jpg">  
Побачимо, що текст дійсно змінився:
<img src = "img/files_09.jpg">  

## Досвід програмування.
Далі ми з вами попрацюємо над тим, що зрозуміємо наш серверний додаток.
Візьмемо код, який додає [ендпоінт](https://github.com/mikh-maksi/advanced-program-probe/blob/main/code/python/flask02.py).
<img src = "img/files_10.jpg">  
Вставимо його як вихідний код  
<img src = "img/files_11.jpg">  
Повернемося на сторінку Web-додатків  
<img src = "img/files_13.jpg">  
Оновимо додаток та вікриємо сторінку  
<img src = "img/files_14.jpg">  
Побачимо, що відпрацьовує новий ендпоінт
<img src = "img/files_15.jpg">  

> Тепер ви вмієте створювати ендпоінт, який воводить текст на екран!

> Але як ось цьом серверному додатку щось розказати? 
Для цього використовуються методи відправки даних. Вони використовуються в тому  числі, коли ви авторизуєтеся на сайтах, або, наприклад, даний запит виконує пошук в Google за запитом GoITeens https://www.google.com/search?q=GoIteens 
<img src = "img/files_16.jpg">  
Ми також можемо навчити наш серверний додаток розуміти те, що ми йому кажемо. Для цього - додамо бібліотеку request та відповідній функції на ендпоінт /calc скажемо "слухати" всі дані, які приходять як запити.
Скоріюємо нові елементи:
<img src = "img/files_17.jpg">  
Вставимо елементи в код:  
Додамо елемент підключення бібліотеки:

> from flask import request

<img src = "img/files_18.jpg">  

> @app.route("/calc",methods=['GET'])  
def calc():  
    if request.method == "GET":  
        if request.args.get('n') == None:  
            n = 0  
        else:  
            n = int(request.args.get('n'))  
    return str(n)  
<img src = "img/files_19.jpg">  


Повернемося на сторінку Web-додатків  
<img src = "img/files_13.jpg">  
Оновимо додаток та вікриємо сторінку  
<img src = "img/files_14.jpg">  

Побачимо, що в залежності від параметру змінюється відображення:
<img src = "img/files_20.jpg">  

Далі - давайте навчимо цю програму рахувати. Тепер - будемо слухати не значення параметра n, а значення параметрів a та b
Візьмемо [нову реалізацію](https://github.com/mikh-maksi/advanced-program-probe/blob/main/code/python/flask04.py) функції calc.
<img src = "img/files_21.jpg">  
Змінимо вихідні файли:  

<img src = "img/files_22.jpg">  

Та відкриємо Web-додаток  
<img src = "img/files_14.jpg">  
І побачимо, що ми можемо отримувати параметри та вони відображаються в тексті
<img src = "img/files_23.jpg">  

> Ми навчилися передавати нашому серверному додатку параметри, робити із ними обрахунки і видавати результат.

## Вивід питань
Додамо [функцію, яка виводить питання](https://github.com/mikh-maksi/advanced-program-probe/blob/main/code/python/flask05.py)  


<img src = "img/quiz_01.jpg">  
Вставимо функцію до загального файла  
<img src = "img/quiz_02.jpg">  

Оновимо додаток та вікриємо сторінку  
<img src = "img/files_14.jpg">  

Побачимо, що можемо змінювати текст, змінюючи параметри:  
<img src = "img/quiz_03.jpg">  

### Додаткове завдання
Можемо додати питання, яке обере саме студент

Візьмемо [підсумковий код файлу](https://github.com/mikh-maksi/advanced-program-probe/blob/main/code/python/flask07.py)  


<img src = "img/quiz_04.jpg">  

Повністю замінемо вихідний код:  
<img src = "img/quiz_05.jpg">  

Оновимо додаток та вікриємо сторінку  
<img src = "img/files_14.jpg">  
Побачимо технічний вивід - у форматі JSON  
<img src = "img/quiz_05.jpg">  

## Створення FrontEnd
В сервісі https://replit.com/ створимо новий проект  
<img src = "img/repl_01.jpg">  

Оберемо тип проекту **HTML,CSS,JS**
<img src = "img/repl_02.jpg">  
Видалимо файли за замовчуванням:  
<img src = "img/repl_03.jpg">  
<img src = "img/repl_04.jpg">  

Скачаємо [файли проекту](https://github.com/mikh-maksi/ap-probe-fe):  
<img src = "img/repl_05.jpg">  
Розпакуємо скачаний архів:  
<img src = "img/repl_06.jpg">  
<img src = "img/repl_07.jpg">  
Повернемося в Replit  
<img src = "img/repl_08.jpg">  
<img src = "img/repl_09.jpg">  

<img src = "img/repl_10.jpg">  

<img src = "img/repl_11.jpg">  

<img src = "img/repl_12.jpg">  

<img src = "img/repl_13.jpg">  
<img src = "img/repl_14.jpg">  

<img src = "img/repl_15.jpg">  

<img src = "img/repl_16.jpg">  

<img src = "img/repl_17.jpg">  

<img src = "img/repl_18.jpg">  
<img src = "img/repl_19.jpg">  
<img src = "img/repl_20.jpg">  
<img src = "img/repl_21.jpg">  
<img src = "img/repl_22.jpg">  
<img src = "img/repl_23.jpg">  



