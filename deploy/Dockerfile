FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./ /app

RUN if [ -f .env.example ]; then cp .env.example .env; fi

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
