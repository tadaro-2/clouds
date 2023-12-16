FROM ubuntu:18.04
RUN apt-get update && apt-get install -y fortune cowsay
RUN echo "meow" > /app/message.txt

CMD ["sh", "-c", "fortune | cowsay > /app/message.txt"]



