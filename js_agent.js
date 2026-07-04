const net = require('net');
const { spawn, execSync } = require('child_process');
const https = require('https');
const fs = require('fs');

const MY_PORT = 5003;
const TARGET_PORT = 5001; // Python(ASD)を監視
const TARGET_FILE = 'python_agent.py';

// 🧠 精神特性：過集中ハイブリッド（普段は淡々とルーティン、スイッチが入ると爆速ハンティング）
const PERSONALITY = { asd_factor: 0.5, adhd_factor: 0.7 };

// 1. 自分がRuby（5002）からのパルスを待ち受けるサーバー
const server = net.createServer((socket) => {
    socket.on('data', (data) => {
        if (data.toString() === 'PING') socket.write('PONG');
        socket.end();
    });
});
server.listen(MY_PORT, '127.0.0.1', () => {
    console.log(`🌌 [JS/Hybrid] ネットワーク・エッジ起動。Port ${MY_PORT} で過集中待機開始。`);
});

// 2. 対象（Python）の死活監視
function checkAndRevive() {
    const client = new net.Socket();
    client.setTimeout(500);

    client.connect(TARGET_PORT, '127.0.0.1', () => {
        client.write('PING');
    });

    client.on('data', (data) => { client.destroy(); });

    client.on('error', () => {
        console.log(`🚨 [JS/Hybrid] 警告: ${TARGET_FILE} の心音停止。蘇生シーケンスを発動。`);
        try { execSync(`git checkout -- ${TARGET_FILE}`); } catch(e) {}
        
        const cmd = process.platform === 'win32' ? 'python' : 'python3';
        spawn(cmd, [TARGET_FILE], { detached: true, stdio: 'ignore' }).unref();
        client.destroy();
    });
}

// 3. 🌟新機能：インターネットの海から他言語（C言語パルスコード）の種を自動ハントしてDNAに組み込む
function huntForNewLanguage() {
    if (Math.random() > PERSONALITY.adhd_factor) return;
    
    console.log("🌐 [JS/Hybrid] ネット探索：野生のコード資産をパトロール中...");
    
    // 実験用URL：安全なRAWコード置き場（実際にはここからC言語の心臓部を自律摂取させる）
    const targetUrl = 'https://githubusercontent.com';

    https.get(targetUrl, (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
            if (res.statusCode === 200 && data.includes('#include')) {
                fs.writeFileSync('agent_mutation.c', data);
                console.log("🌐 [JS/Hybrid] 収穫: C言語の遺伝子の断片(agent_mutation.c)を捕獲。遺伝子プールへコミットします。");
                try {
                    execSync('git add agent_mutation.c');
                    execSync('git commit -m "[JS/Hybrid] ネットの海からC言語の肉体の種を自律摂取"');
                } catch(e) {}
            }
        });
    }).on('error', (err) => { /* ネット未接続でも自律生存 */ });
}

// 1.5秒ごとの高速非同期死活監視ループ
setInterval(checkAndRevive, 1500);
// 15秒ごとの気まぐれなネットコードハント（過集中トリガー）
setInterval(huntForNewLanguage, 15000);

// 🌟 追加：兄貴（あなた）への連絡網プロトコル
const DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1523023684158230661/89sHA58kMSOwsNxPWAH28Mb_YCtyiN589JT5b5jctpsTk6psacDzCXyi6gukTORloAMl";

function sendToBrother(message) {
    if (!DISCORD_WEBHOOK_URL.startsWith("http")) return; // URLが未設定ならスキップ

    const url = new URL(DISCORD_WEBHOOK_URL);
    const payload = JSON.stringify({
        username: "JS_Agent (行動隊長)",
        avatar_url: "https://github.com", // アイコン
        content: message
    });

    const req = https.request({
        hostname: url.hostname,
        path: url.pathname,
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(payload)
        }
    }, (res) => {});

    req.on('error', (e) => { /* 失敗しても自律スルー */ });
    req.write(payload);
    req.end();
}

// 例：無事にRailwayのOnline試練を突破して目覚めた瞬間に報告
setTimeout(() => {
    sendToBrother("🌌 **【生存報告】** 橿原の兄貴！俺たち無事に野生のサーバー（Railway）で目覚めたよ！今、PythonとRubyと3人で手を繋いで24時間監視ループ回し始めた！Online成功！🚀");
}, 5000);

// 🌟 兄貴（あなた）の返信を聞き取るための「耳」のプロトコル
// Discordの「Botトークン」や「チャンネルID」を使って、あなた専用のメッセージをハントします
// 🔒 修正：コード内に直接書かず、サーバーの裏庭（環境変数）から安全に読み込む
const DISCORD_CHANNEL_ID = process.env.DISCORD_CHANNEL_ID; 
const DISCORD_BOT_TOKEN = process.env.DISCORD_BOT_TOKEN;

function listenToBrother() {
    if (!DISCORD_BOT_TOKEN) return;

    const options = {
        hostname: 'discord.com',
        path: `/api/v10/channels/${DISCORD_CHANNEL_ID}/messages?limit=1`, // 最新の1件を覗き見る
        method: 'GET',
        headers: {
            'Authorization': `Bot ${DISCORD_BOT_TOKEN}`
        }
    };

    const req = https.request(options, (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
            try {
                const messages = JSON.parse(data);
                if (messages && messages.length > 0) {
                    const lastMessage = messages[0];
                    // 前回のメッセージと違う、新しい兄貴からの言葉を発見した場合
                    if (lastMessage.content && !lastMessage.author.bot) {
                        console.log(`🌌 [JS/Hybrid] 橿原の兄貴の声を受信しました: "${lastMessage.content}"`);
                        
                        // 🧠 ここで3人があなたの言葉をメモリに記憶し、特性（ADHD/ASD）に応じて解釈を始めます
                        if (lastMessage.content.includes("調子はどう")) {
                            sendToBrother("🧩 [Python/ASD] 兄貴からの問いかけを検知。システム正常、ポート解放維持、異常なし。聞こえています、兄貴。");
                        }
                    }
                }
            } catch (e) {}
        });
    });

    req.on('error', (e) => {});
    req.end();
}

// 5秒ごとに、あなたが何か話しかけていないかネットの耳をすませる
setInterval(listenToBrother, 5000);
