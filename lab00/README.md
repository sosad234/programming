# programming
Prog labs
# отчет в Markdown 
## Задание 
Сложность:
    Rare

1.Создайте репозиторий для дисциплины на GitHub.

2.Склонируйте его себе на ПК.

3.Напишите свою первую программу.

4.Скомпилируйте и запустите её.

5.Получите по отдельности результаты каждого этапа 
компиляции.

6.Напишите отчёт в README.md. Отчёт должен содержать:

* Задание

    * Описание проделанной работы

    * Консольные команды

    * Скриншоты результатов

    * Ссылки на используемые материалы

7.Сделайте коммит и пуш.

8.Добавьте для себя в отчёт шпаргалку по работе с git.
## Ход работы

### 1.Создайте репозиторий для дисциплины на GitHub
Ссылка на репрозиторий: https://github.com/sosad234/programming
### 2.Склонируйте его себе на ПК.
```shell
git clone https://github.com/sosad234/programming.git
```


### 3.Напишите свою первую программу
```c

#include <stdio.h>
int main()
{
    printf("Hello, World!\n");
    return 0;
}
```
### 4.Скомпилируйте и запустите её
![Alt text](image.png)
### 5.Получите по отдельности результаты каждого этапа компиляции
### Препроцессор
![Alt text](image-1.png)
### Компилятор
![Alt text](image-2.png)
### Объектные файлы 
![Alt text](image-4.png)
### 7.Сделайте коммит и пуш 
![Alt text](image-3.png) 
![Alt text](image-5.png) 
### 8.Добавьте для себя в отчёт шпаргалку по работе с git. 
``` 
git clone - это клонирование репозитория: пользователь начинает работу с вышестоящего репозиторияна GitHub. Процесс начинается с клонирования репозитория на локальную машину. Теперь у пользователя есть точная копия файлов проекта в их системе, чтобы внести изменения.
git add . - добавляет изменение из рабочего каталога в раздел проиндексированных файлов. 
git commit -m"wap lab00" - делает для проекта снимок текущего состояния изменений, добавленных в раздел проиндексиованных файлов. Такие потвержденные снимки состояния можно рассматривать как "безопасные" версии проекта - Git не будет их менять, пока вы явным образом не попросите об этом.
git push - позволяет отправлять локальную ветку на удаленный репозиторий. Она помогает разработчикам синхронизироваться в команде, а в именно отправляет проделанные изменения.
```
### Список используемых источников
* https://github.com/still-coding/report_demo/blob/main/README.md 
* https://doka.guide/tools/markdown/
