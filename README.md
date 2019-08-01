# stepic_web_project
Создание проекта в рамках курса на [stepic.org](https://stepik.org/course/154)

## Рабочее окружение:
* [Ubuntu 14.04.6 LTS (Trusty Tahr)](http://releases.ubuntu.com/14.04/)
* python2 (v. 2.7.6)
* nginx (v. 1.4.6)
* gunicorn (v. 17.5.0)
* django (v. 1.10.5)
* mysql (v. 5.5.62)

## Этапы проекта:
1. Отдача статических файлов([п. 1.8](https://stepik.org/lesson/14825/step/12?unit=4174))
2. Запуск WSGI приложений([п. 1.9](https://stepik.org/lesson/14826/step/11?unit=4175))
3. Создание Django приложения([п. 2.1](https://stepik.org/lesson/14827/step/11?unit=4176))
4. Создание моделей в Django приложении([п. 2.3](https://stepik.org/lesson/14829/step/10?unit=4178))
5. Отображение данных([п. 2.5](https://stepik.org/lesson/14831/step/8?unit=4179))
6. Обработка форм([п. 2.6](https://stepik.org/lesson/14832/step/11?unit=4181))

### Отдача статических файлов
* Название ветки *nginx*, чтобы перейти к данному этапу введите:
> `git checkout nginx`
* Установка nginx
> `sudo apt-get install nginx`

### Запуск WSGI приложений
* Название ветки *gunicorn*, чтобы перейти к данному этапу введите:
> `git checkout gunicorn`
* Установка gunicorn
> `sudo apt-get install gunicorn`

### Создание Django приложения
* Название ветки *django*, чтобы перейти к данному этапу введите:
> `git checkout django`
* Установка django
> `sudo apt-get install python-pip`

> `sudo pip install django==1.10.5`

### Создание моделей в Django приложении
* Название ветки *mysql*, чтобы перейти к данному этапу введите:
> `git checkout mysql`
* Установка mysql
> `sudo apt-get install mysql-client mysql-server`

> `sudo apt-get install python-dev libmysqlclient-dev build-essential`

> `sudo pip install mysqlclient`
* Игнорьте ошибку (ERROR 2002) - баг на локальной машине Stepik'a
(обращается к сокету до создания, после последующих restart'ов ошибки нет)

### Отображение данных
* Название ветки *pages*, чтобы перейти к данному этапу введите:
> `git checkout pages`

### Обработка форм
* Название ветки *forms*, чтобы перейти к данному этапу введите:
> `git checkout forms`
