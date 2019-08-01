# stepic_web_project
Создание проекта в рамках курса на [stepic.org](https://stepik.org/course/154)

## Рабочее окружение:
* [Ubuntu 14.04.6 LTS (Trusty Tahr)](http://releases.ubuntu.com/14.04/)
* python2 (v. 2.7.6)
* nginx (v. 1.4.6)
* gunicorn (v. 17.5.0)
* django (v. 1.10.5)

## Этапы проекта:
1. Отдача статических файлов([п. 1.8](https://stepik.org/lesson/14825/step/12?unit=4174))
2. Запуск WSGI приложений([п. 1.9](https://stepik.org/lesson/14826/step/11?unit=4175))
3. Создание Django приложения([п. 2.1](https://stepik.org/lesson/14827/step/11?unit=4176))

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
