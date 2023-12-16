FROM alpine:3.14
RUN apk --no-cache add fortune cowsay
RUN echo "meow" > /app/message.txt

CMD ["sh", "-c", "fortune | cowsay > /app/message.txt"]



