"API-методы для получения статистики. Методы созданы на FastAPI. 
main.py - view-функции для сохранения события (create_user_with_event) и 
получения информации (read_events).
Функция для сохранения событий принимает path-параметр с номером события, запрашивает
дату и ip пользователя и возварщает экземпляр класса EventWithUser.
Функция для получения информации принимает в виде query-параметров номер события и дату
и, в зависимости от переданных необязательных query-параметров ip и status, возвращает 
количество событий в зависимости от переданных аргументов.
"