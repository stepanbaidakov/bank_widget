# Виджет для банковских операций

## Описание
Виджет, который показывает несколько последних успешных банковских операций клиента

## Установка
1. Клонируйте репозиторий:
`git clone https://github.com/username/bank_widget.git`
2. Установка зависимости:
`pip install -r requirements.text`
## Тестирование
1. Установка pytest:
`poetry add --group dev pytest`
2. Запуск тестов:
`pytest <file_name>`
## Использование
### В модуле `generators.py` реализованы следующие возможности:
* Функция `filter_by_currency` позволяет фильтровать список транзакций по заданной валюте. Она возвращает итератор, 
который поочередно выдает транзакции, соответствующие указанной валюте.
* Функция `transaction_descriptions` возвращает описание каждой операции из списка транзакций. Если список транзакций
пуст или описание отсутствует, функция возвращает сообщение "Описание отсутствует".
* Функция card_number_generator генерирует номера карт в заданном диапазоне чисел. Номера автоматически форматируются в
стандартный вид банковских карт: XXXX XXXX XXXX XXXX.
### В Модуле `decorators.py` реализован декоратор, который логирует начало и конец выполнения функции, а также ее 
результаты или возникшие ошибки
## Документация
Для получения дополнительной информации, обратитесь к [документации]()

