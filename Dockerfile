# ---------------------------------------------------------
# 1. ベース環境（安定したNode.js環境）
# ---------------------------------------------------------
FROM node:20-bookworm

# 安定動作のための作業ディレクトリ
WORKDIR /app

# ビルド時の余計な確認画面を完全に無視する設定
ENV DEBIAN_FRONTEND=noninteractive

# ---------------------------------------------------------
# 2. Cブラザーズ（C, C++, C#）の環境だけを厳選インストール
# ---------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    mono-runtime \
    mono-mcs \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------
# 3. 司令塔（JavaScript）の準備とソースコピー
# ---------------------------------------------------------
COPY package*.json ./
RUN npm ci --only=production

# 3人のエージェントと、追加したC兄弟のコードをすべて宇宙船に詰め込む
COPY . .

# 司令塔のJSを起動
CMD ["node", "js_agent.js"]
