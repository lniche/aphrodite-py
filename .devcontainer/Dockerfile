FROM python:3.12-slim

WORKDIR /workspace

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000

CMD ["/bin/bash"]
