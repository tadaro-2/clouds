FROM ubuntu:18.04
RUN apt-get update && apt-get install -y fortune cowsay

CMD ["sh", "-c", "fortune | cowsay > /DevOps_labs/Lab-3/files/message.txt"]