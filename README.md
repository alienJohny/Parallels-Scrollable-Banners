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

## Тестирование

Тестировал сервис на 100 изображениях (далее баннерах) из датасета cifar10. <br />
Каждому баннеру я приписываю N случайных категорий, N также генерируется случайно в диапозоне от 1 до 10. <br />
Также к каждому баннеру я генерирую число P - то, сколько раз он должен показаться. <br />
Далее я запускаю простой веб-сервер на Python для хранения изображений и эмуляции их получения с веб-сервера. <br />
<br />
Сборка: <br />
1. Скачать архив с баннерами: `https://yadi.sk/d/IVpd0wEb-Ayo_g` <br />
2. В директории, где находятся баннеры открыть Терминал и запустить веб-сервер: `python3 -m http.server 9000` <br />
3. В этой же директории создать Python файл со следующим содержимым и запустить его: <br />
```python
import glob
import numpy as np
import random

BASE_URL = "http://0.0.0.0:9000/"

f = open("cfg.csv", "w")
header = "Image_URL;prepaid_shows_amount;" + \
         ";".join(["category" + str(n) for n in range(1, 11)])
f.write(header + "\n")

cats = ["truck", "dog", "cat", "ship", "bird", "airplane", "auto", "horse", "deer", "frog"]

for img in glob.glob("*.png"):
    imgurl = BASE_URL + img
    psa = str(random.randint(10, 5 * 1000))

    ncats = random.randint(1, 10)
    current_cats = list(np.random.choice(cats, ncats, replace=False))
    
    entry = ";".join([imgurl, psa] + current_cats) + "\n"
    f.write(entry)
        
f.close()
```

**Если все сделано верно, создался файл cfg.csv. Его можно отправлять на submit в форму на домашней страницы веб-приложения PSB.** <br />


## API
HTTP GET пример: `http://127.0.0.1:8000/get?category=auto&category=trains` <br />
```bash
$ curl -X GET "http://127.0.0.1:8000/get?category=auto&category=trains"
```

## Способ минимизировать показы объявления 2 раза подряд
В качестве способа я выбрал с вероятностью 33% заменять баннер на один из списка подходящих по категории. <br />
Вероятность выбрал эвристически. Таким образом есть вероятность 66%, что баннер все же будет показан 2 раза подряд. <br />
И 10% вероятность, что баннер будет заменем на другой 2 раза подряд. <br />
Функционал реализован в классе `DataManager` по [ссылке](https://github.com/alienJohny/Parallels-Scrollable-Banners/blob/4db2f824ab2dce4a896bb8ab89b87b2188882470/psb/DataManager/DataManager.py#L57).

## Дополнительно
Если конфигурационный файл не был загружен, но произошел запрос на /get, то возвращается страница 404 not found.