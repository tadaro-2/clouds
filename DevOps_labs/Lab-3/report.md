# Лабораторная работа 3

### Цель работы
Сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь.
(например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер). 



### Создание Dockerfile

Создадим какой-нибудь Dockerfile, из которого будет собираться образ. 
Например, пусть выведет нам корову, которая сообщит рандомное предсказание.

```dockerfile
FROM ubuntu:18.04
RUN apt-get update && apt-get install -y fortune cowsay

CMD ["sh", "-c", "fortune | cowsay > /DevOps_labs/Lab-3/files/message.txt"]
```

Положим его в папку лабораторной. Его можно там найти и посмотреть, там написано всё то же самое.




### Создание GitHub Actions

Для автоматической сборки образа настроим GitHub Actions для нашего репозитория.
Для этого в корне создадим файл .github/workflows/docker.yml

```yml
name: Docker Build

on:
  push:
    branches:
      - main

jobs:
  docker:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v2

    - name: Build Docker Image
      run: docker build -t message-image .

    - name: Save Docker Image Result
      run: |
        docker save message-image -o result.tar
        mkdir -p github_workspace/artifacts
        mv result.tar github_workspace/artifacts
      if: success()

    - name: Upload Result
      uses: actions/upload-artifact@v2
      with:
        name: result
        path: github_workspace/artifacts

```

В нём мы указываем, что при пуше в ветку main будет происходить сборка образа и его сохранение.


### Проверка

После пуша в репозиторий во вкладке Actions можно увидеть, что сборка прошла успешно.

![Сборка](./Pictures/сборка.png)

Во вкладке Artifacts можно увидеть файлы, которые были сохранены.

![Артефакты](./Pictures/артефакты.png)


### Выполнение сборки

Так как мы используем Github Actions, сборка происходит на удалённом сервере, а не на локальной машине. Можно настроить свою локальную машину, чтобы она собирала образы, но мы этого делать не будем, так как гитхаб предоставляет нам бесплатно сервер для сборки образов.
Про это можно почитать [тут](https://docs.github.com/ru/actions/learn-github-actions/understanding-github-actions).


### Выводы

В данной работе мы научились работать с GitHub Actions, настроили автоматическую сборку образа и сохранение его в файл.