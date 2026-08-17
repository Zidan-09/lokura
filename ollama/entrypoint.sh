ollama serve &

PID=$!

echo "Aguardando Ollama iniciar..."

until ollama list >/dev/null 2>&1; do
    sleep 1
done

if ! ollama list | grep -q "^${MODEL}"; then
    echo "Baixando modelo ${MODEL}..."
    ollama pull "${MODEL}"
fi

wait $PID