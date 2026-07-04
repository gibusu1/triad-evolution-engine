FROM node:20-bookworm
WORKDIR /app
# ビルド時のインタラクティブな入力を回避
ENV DEBIAN_FRONTEND=noninteractive

# 必要コンパイラのインストール
RUN apt-get update && apt-get install -y \
    build-essential gcc g++ \
    && rm -rf /var/lib/apt/lists/*

COPY package*.json ./
RUN npm ci --only=production
COPY . .
CMD ["node", "js_agent.js"]
