# discordLimit25mb

![](https://i.imgur.com/bGnhrGR.png)

![](https://i.imgur.com/ZR94TDk.png)

## Описание

В [дискорде](https://discord.gg/Jgmf7AJ) есть проблемка для обычных пользователей - им тяжело делиться видео, т.к присутствует лимит в 25 МБ.

Данный репозиторий - это микро решение данной проблемы, при помощи Python.

Мы будем быстро, в 1-н клик - нарезать видео на 15-ти секундные части, перед отправкой.

> 15 сек можно изменить на любой другой свой тайминг!

```bash
# 15
def split_video(input_file, output_prefix, chunk_duration=15):
```

---

## Установка

- скачать
    - `git clone git@github.com:gitalexhubuser/discordLimit25mb.git`
- поместить по адресу `E:\PythonProjects\discordLimit25mb`
- активировать виртуальное окружение в папке с проектом
    - python -m venv venv
- установить все необходимые библиотеки
    - `pip install -r requirements.txt`
- запустить скрипт через `run.cmd`

> При желании путь `E:\PythonProjects\discordLimit25mb` - можно изменить на свой!

---

## Использование

Для нарезки достаточно:
- запустить скрипт `run.cmd`
- перетащить видео в окно `tkinter`
- получить результат

---

# Ссылки
| Описание | Ссылка |
| ------ | ------ |
Репо: | [github.com/gitalexhubuser/discordLimit25mb](https://github.com/gitalexhubuser/discordLimit25mb)
