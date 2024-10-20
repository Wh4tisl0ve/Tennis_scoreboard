# Табло теннисного матча

Проект представляет собой веб-приложение, реализующее табло счёта теннисного матча.

Проект создан в рамках **Python Roadmap Сергея Жукова** -> [ссылка](https://zhukovsd.github.io/python-backend-learning-course/)
  

<p align="center">
  <img src="./docs/logo.png" width="250" height="250" alt="logo"/>
</p>

## Запуск проекта
1. Выполните клонирование проекта `git clone git@github.com:Wh4tisl0ve/Tennis_scoreboard.git`
2. Запустите скрипт выполнив `python3 -m src.app.run` в терминале.

## Структура проекта

* [run.py](src/run.py) Файл, позволяющий запустить wsgi приложение
* [src/tests](src/tests) Директория, содержащая тесты логики подсчета очков
* [src/app/mini_framework](src/app/mini_framework) Директория, содержащая реализацию простейшего фреймворка
* [src/app/repository](src/app/repository) Директория, содержащая слой "Репозиторий"
* [src/app/static](src/app/static) Директория, содержащая статические файлы
* [src/app/templates](src/app/templates) Директория, содержащая HTML шаблоны, используемые для рендеринга
* [src/app/tennis_logic](src/app/tennis_logic) Директория, содержащая логику подсчета очков в теннисном матче
* [src/app/config.py](src/app/config.py) Файл, содержащий конфигурацию приложения, сервера и базы данных
* [src/app/models.py](src/app/models.py) Файл, содержащий объекты, описывающие структуру данных
* [src/app/controllers.py](src/app/controllers.py) Файл, содержащий функции, обрабатывающие пользовательские запросы

## Реализация логики подсчета очков в теннисном матче
Логика подсчета очков в матче, была реализована в ООП-стиле с целью избежания дублирования кода.

<p align="center">
  <img src="./docs/tennis-schema.png" width="500" height="500" alt="new-match"/>
</p>

## Описание страниц проекта
### Страница нового матча 
Адрес - `/`.
Представляет собой форму для создания нового матча. 
Содержит два поля для ввода имен игроков и кнопку для отправления POST запроса.  
Результатом нажатия кнопки будет редирект на страницу `/match-score?uuid=$match_id`

<img src="./docs/new-match.jpg" alt="new-match"/>

### Страница счёта матча
Адрес - `/match-score?uuid=$match_id`. GET параметр uuid содержит UUID матча.  
Представляет собой таблицу для ведения счета матча.  
Нажатие кнопок приводит к POST запросу по адресу `/match-score?uuid=$match_id`, в полях отправленной формы содержится выигравший очко игрок

<img src="./docs/match-score.jpg" alt="new-match"/>

Теннисный матч играется по системе BOF3.  
При достижении 2 очков в Match, игра считается завершенной. Определяется победитель и результат выводится на страницу.

<img src="./docs/match-score-end.jpg" alt="new-match"/>

### Страница сыгранных матчей
Адрес - `/matches?page=$page_number&filter_by_player_name=$player_name&per_page=$per_page`. GET параметры:
* `page` - номер страницы. Если параметр не задан, подразумевается первая страница  
* `filter_by_player_name` - имя игрока, матчи которого ищем. Если параметр не задан, отображаются все матчи
* `per_page` - количество записей на страницу. Если параметр не задан, отображается 10 записей.

Постранично отображает список сыгранных матчей. 
Нажатие кнопки "применить" приводит к формированию GET запрос вида `/matches?filter_by_player_name=${NAME}&per_page=${per_page}`.  
Позволяет искать матчи игрока по его имени. 
Для переключения страниц реализована пагинация.

<img src="./docs/matches.jpg" alt="new-match"/>

## База данных
В качестве системы управления базами данных была выбрана MySQL. 
Для управления объектами бд была использована ORM SqlAlchemy.
База данных содержит в себе 3 таблицы:
1. `Players` - таблица, содержащая информацию об игроках.
2. `Matches` - таблица, содержащая информацию о теннисном матче.
3. `Match story` - таблица, содержащая информацию о забитых голах в теннисном матче.

<img src="./docs/db-schema.jpg" alt="new-match"/>

## Тесты
В качестве фреймворка для тестирования был выбран [pytest](https://docs.pytest.org/en/stable/index.html).
Юнит тестами была покрыта логика подсчета очков в теннисном матче. Основные тест-кейсы:
* Проверка корректности начисления очков для игроков
* Проверка работы механизма преимущества(AD) игроков
* Проверка работы механизма потери преимущества
* Проверка работы механизма сброса очков после взятия очка при преимуществе(AD)
* Проверка корректности начисления победы в сете для игроков
* Проверка работы механики начисления очков после объявления тай-брейка
* Проверка победы в матче

## Стек 

* Python 3.12
* pytest
* Waitress
* jinja2
* MySQL
* SqlAlchemy
* html-css-js
