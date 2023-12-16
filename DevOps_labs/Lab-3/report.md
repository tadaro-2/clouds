# Лабораторная работа 3

### Цель работы
Сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь.
(например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер). 



### Создание Dockerfile

Создадим какой-нибудь Dockerfile, из которого будет собираться образ. 
Например, пусть создаётся текстовый файл с коровой, которая сообщит нам рандомное предсказание. Будем сохранять его в папку ./files.

```dockerfile
FROM alpine:3.14
RUN apk --no-cache add fortune cowsay

CMD ["fortune | cowsay", ".files/message.txt"]
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
      run: docker build -t message-image "DevOps_labs\Lab-3\Dockerfile"

    - name: Save Docker Image Result
      run: |
        docker save message-image -o result.tar
        mkdir -p $GITHUB_WORKSPACE/artifacts
        mv result.tar $GITHUB_WORKSPACE/artifacts/result.tar
      if: success()

    - name: Extract message.txt
      run: |
        docker create --name temp-container message-image
        docker cp temp-container:/app/message.txt $GITHUB_WORKSPACE/artifacts/message.txt
        docker rm temp-container

    - name: Upload Artifact
      uses: actions/upload-artifact@v2
      with:
        name: docker-image
        path: $GITHUB_WORKSPACE/artifacts

```

В нём мы указываем, что при пуше в ветку main будет происходить сборка образа, сохранение его в файл и его загрузка.


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