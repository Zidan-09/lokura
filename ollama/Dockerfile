FROM ollama/ollama:latest

ARG MODEL=llama3.2

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 11444

ENTRYPOINT ["/entrypoint.sh"]