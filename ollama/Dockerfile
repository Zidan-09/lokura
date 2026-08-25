FROM ollama/ollama:latest

ARG MODEL=llama3.2

ENV MODEL=${MODEL}

COPY entrypoint.sh /entrypoint.sh

RUN sed -i 's/\r$//' /entrypoint.sh && \
    chmod +x /entrypoint.sh

EXPOSE 11444

ENTRYPOINT ["/entrypoint.sh"]