# 1. ベースとして最新のNode.js環境を用意
FROM node:20-slim

# 2. 部屋の中にPython3、Ruby、Git、C言語コンパイラ(gcc)を強制インストール
RUN apt-get update && apt-get install -y \
    python3 \
    ruby \
    git \
    gcc \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 3. 彼らのプログラムをサーバー内の作業部屋にコピー
WORKDIR /app
COPY . .

# 4. 行動隊長（JS）を目覚めさせる
CMD ["node", "js_agent.js"]
