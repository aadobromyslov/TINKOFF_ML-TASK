# Антиплагиат для Python-кода

## Реализация

Проект реализован на Python.

Программа принимает на вход два файла с Python-кодом и
возвращает оценку их схожести, основанную на вычислении
расстояния Левенштейна.

Перед непосредственно вычислением расстояния Левенштейна
программа "очищает" принятые файлы: 
- используя библиотеку **ast**, программа приводит к единому виду
все имена переменных,
- используя библиотеку **re**, программа убирает из кода все 
комментарии, аннотации и строки.

Вычисляя методами динамического программирования расстояние
Левенштейна, программа выдаёт оценку схожести двух очищенных 
файлов -- расстояние Левенштейна, нормализованное по объёму
наибольшего из файлов.

## Запуск

Для запуска программы нужно в качестве аргументов передать
исполняемому файлу **compare.py** имя файла ввода, в котором
на каждой строке нужно через пробел указать два сравниваемых файла,
и имя файла вывода, в которой будут записаны оценки схожести
пар файлов из файла ввода.

Пример запуска программы:

```
$ python3 compare.py input.txt scores.txt
```