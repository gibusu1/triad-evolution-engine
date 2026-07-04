# ---------------------------------------------------------
# 1. 宇宙船のベース（C#が最初から入っている安定したコンテナを使う）
# ---------------------------------------------------------
FROM mono:6.12.0

# ---------------------------------------------------------
# 2. Node.js（JS用）と、C/C++コンパイラを確実に追加
# ---------------------------------------------------------
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    gcc \
    g++ \
    python3 \
    ruby \
    && curl -fsSL https://nodesource.com | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------
# 3. 司令塔（JavaScript）の準備とソースコピー
# ---------------------------------------------------------
WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

# 3人（Py/Ruby/JS）とCブラザーズのコードを全員詰め込む
COPY . .

# 司令塔のJSを起動
CMD ["node", "js_agent.js"]
