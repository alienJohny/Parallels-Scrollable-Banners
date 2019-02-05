# Parallels Scrollable Banners Task

Фреймворк: `Django version 2.1.3`
<br />
## Первый запуск
Клонировать репозиторий и настроить права доступа к скриптам запуска: <br />
`$ git clone https://github.com/alienJohny/Parallels-Scrollable-Banners.git`
<br />
`$ cd Parallels-Scrollable-Banners/psb/`
<br />
`$ chmod +x ./init.sh && ./init.sh`
<br />
После этого должно запуститься веб-приложение по адресу: http://127.0.0.1:8000/ 
<br />
В дальнейшем запускать веб сервер можно командой `$ ./run.sh` из директории проекта `../psb/`
<br />

## API
HTTP GET пример: `http://127.0.0.1:8000/get?category=auto&category=trains` <br />
```bash
$ curl -X GET "http://127.0.0.1:8000/get?category=auto&category=trains"
```
