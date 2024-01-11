
# telegram-always-online

  

🇺🇸 Keep your Telegram always online.

🇷🇺 Поддерживает в вашем аккаунте постоянный онлайн.

Thanks: https://github.com/abusetelegram/AlwaysOnline-

  

# Information | Информация

🇺🇸 Don't let others peak on your daily routine with recent online! So keep yourself always online.

🇷🇺 Не позволяйте посторонним людям отслеживать ваш онлайн, ведь это может сыграть не в вашу пользу. Так что сбейте их с толку - будьте онлайн постоянно!

  

# Requeriments | Требования

  
#### Python3
There is nothing tricky here (тут ничего хитрого нет):
`sudo apt install python3`
#### Telethon
🇺🇸 We will need an older version of Telethon. The script will not work with the latest version.  
🇷🇺 Версия Telethon нам нужна более старшая. С последнией версией скрипт не будет работать.
`pip3 install telethon==0.19.1.6`
#### python-dotenv
`pip install python-dotenv `

  

# How to use | Как использовать?

  

 1. 🇺🇸 You need to get telegram API access data. You can obtain it here:  

🇷🇺 Вам небходимо получить данные для доступа к Telegram API. Это можно сделать тут:  

https://my.telegram.org  

![9704fe13c382b5a4682727f859edce82.png](https://imgtr.ee/images/2024/01/11/9704fe13c382b5a4682727f859edce82.png)

 2. 🇺🇸 You need the `api_id` and `api_hash` values. Rename file `.env.example` to `.env` then specify them in your `.env` file.  
 
 🇷🇺 Вам необходимы значения `api_id` и `api_hash`. Переименуйте файл `.env.example`  в `.env` и укажите их в вашем `.env` файле.

 3. 🇺🇸 If you wish, you can change the delay in updating your online service. Specify the interval in seconds in `DELAY` in `.env`. Settings below 15 seconds are not recommended.  

🇷🇺 По желанию, вы можете изменить задержку в обновлении вашего онлайна. Укажите интервал в секундах в `DELAY` в `.env`. Не рекомендуется установка ниже 15 секунд.

 4.  `python3 main.py`

 5. Follow the instruction and you are good to go !

  

# Tips | Заметки

### 🇺🇸 English
- Do not deploy this script in an **unsecure** location and take care to have the necessary permissions on the `Session` file in the directory. Leaking this file is tantamount to giving **anyone permission to access your Telegram account**.
- This script does not mark your messages as read and works silently.
- You can still use your account as normal.

### 🇷🇺 Русский
 - Не развертывайте этот скрипт в **небезопасном** месте и позаботьтесь о необходимых правах доступа к файлу `Session` в каталоге. Утечка этого файла  равносильна предоставлению **кому-либо разрешения на доступ к вашему аккаунту Telegram**.
 - Этот скрипт не отмечает ваши сообщения прочитанными и работает незаметно.
- Вы по-прежнему можете пользоваться своей учетной записью в обычном режиме.


  

# How it works | Как это работает?
### 🇺🇸 English
The script is a very ordinary Telegram client that works similar to the application on your phone.
At the time of the first launch, you will need to indicate your phone number in international format (+...), indicate a one-time password that will be sent to you in Telegram on another device, as well as *two-factor authentication password*, if you have one. *If two-factor authentication is disabled, then the request `If you have 2FA password, please enter right now. This Password will not be stored.`, do not enter anything, just press Enter.*

*Please note that in some cases the one-time password may be requested twice by the script. You need to enter it in both cases.*

After successful authorization, you will see the message `You are now always ONLINE`, this means that the script has launched and is working successfully.

### 🇷🇺 Русский
Скрипт представляет собой самый обычный Telegram-клиент, который работает по аналогии с приложением в вашем телефоне.
В момент первого запуска, вам необходимо будет указать ваш номер телефона в международном формате (+...), указать одноразовый пароль, который придёт вам в Telegram на другом устройстве, а также *пароль двухфакторной авторизации*, если он у вас установлен. *Если двухфакторная авторизация у вас отключена, то на запрос `If you have 2FA password, please enter right now. This Password will not be stored.` ничего не вводите, просто нажмите Enter.*

*Обратите внимание, что в некоторых случаях одноразовый пароль может быть запрошен скриптом дважды. Вам необходимо в обоих случаях его ввести.*

После успешной авторизации вы увидете сообщение `You are now always ONLINE`, это значит, что скрипт запустился и успешно работает.