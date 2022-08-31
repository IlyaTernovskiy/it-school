# Getting Started 

Запуск локальный:
1. скачать и установить NodeJS - https://nodejs.org/download/release/v16.14.2/node-v16.14.2-x64.msi
2. перейти в корень набрать команду `npm install` - долждаться установки пакетов 
3. Если npm повисает можно установить yarn - https://classic.yarnpkg.com/latest.msi,
запустить в корне `yarn install`.
Если собираете вне периметра ГПН, то удалите yarn.lock
4. набрать команду `npm start` для запуска проекта 
5. открыть приложение [http://localhost:3000](http://localhost:3000)


# Docker
1. сбилдить \
`docker build -t my-front .`
2. собрать контейнер с переменной окружения BACKEND_HOST \
`docker run --env BACKEND_HOST='хост:порт' -d -p 3002:8080 ид_контейнера`
3. Например:
`docker run --env BACKEND_HOST='172.29.0.1:8004' -d -p 3002:8080 7f46ae786127`
4. проверить по [http://localhost:3002](http://localhost:3002)

