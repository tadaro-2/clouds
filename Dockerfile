FROM ubuntu:18.04
RUN apt-get update && apt-get install -y fortune cowsay
RUN echo "meow" > /DevOps_labs/Lab-3/files/message.txt

CMD ["sh", "-c", "fortune | cowsay > /DevOps_labs/Lab-3/files/message.txt"]