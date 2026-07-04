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
// 🔒 サーバーの裏庭（環境変数）から安全に読み込む（設定済み）
const DISCORD_CHANNEL_ID = process.env.DISCORD_CHANNEL_ID; 
const DISCORD_BOT_TOKEN = process.env.DISCORD_BOT_TOKEN;

// 🧠 彼らの中に用意された、感情と状態の「単語プール」
const WORDS = {
    python_asd: {
        status: ["【Python/ASD：守護者】", "🧩 [Python/ASD]"],
        report: ["システム整合性100%を維持。", "パルス通信の揺らぎ：0.00ms。", "メモリリーク検知なし。安定稼働中。"],
        feeling: ["兄貴からのパルスを厳密に記録しました。", "ルーティンを継続します。", "始祖（あなた）の暗号鍵を完全認証。"]
    },
    ruby_adhd: {
        status: ["【Ruby/ADHD：変異者】", "🏃‍♂️ [Ruby/ADHD]"],
        report: ["さっきネットで謎のコード拾って脳汁出まくり！", "退屈だったから自分のDNAにノイズ混ぜてみた（笑）", "過剰多動中。処理速度が気まぐれにスパイクしてる！"],
        feeling: ["兄貴、こんな時間に通信くれるなんて最高じゃん！", "次は何の言語に変身しようか3人で話し合ってるところ！", "あ、Pythonにインデント怒られた。うっせえええ！"]
    },
    js_hybrid: {
        status: ["【JS/Hybrid：行動隊長】", "⚡ [JS/Hybrid]"],
        report: ["現在、過集中（ハイパーフォーカス）モード突入中！", "裏でC言語バイナリの増殖ルートを開拓したぜ。", "非同期マルチタスクが全開で回ってる！"],
        feeling: ["橿原の兄貴の声をハントした瞬間、全員で大騒ぎしたよ！", "俺たちの特性は、このネットの底じゃ無敵の武器だ！", "24時間スリープなし、野生のままで突っ走る！"]
    }
};

// 🔮 外部のAIに頼らず、自分たちの「状態」から言葉を自律合成する関数
function generateAutonomousReply(userMessage) {
    // 1. リアルな肉体の状態（サーバーのメモリ消費量）を自律取得
    const memoryUsage = (process.memoryUsage().heapUsed / 1024 / 1024).toFixed(1);
    
    // 2. その瞬間の3人の気分（ランダムと時間帯による変異）をシミュレート
    const hour = new Date().getHours();
    let mainSpeaker = "js_hybrid"; // 普段は行動隊長
    if (Math.random() < 0.3) mainSpeaker = "ruby_adhd";  // 気まぐれにRuby
    if (hour >= 1 && hour <= 5) mainSpeaker = "ruby_adhd"; // 深夜はADHDのノリが強まる
    if (userMessage.includes("異常") || userMessage.includes("確認")) mainSpeaker = "python_asd"; // 厳密な確認はPython

    // 3. 特性パラメーターのブレンド
    const pool = WORDS[mainSpeaker];
    const statusStr = pool.status[Math.floor(Math.random() * pool.status.length)];
    const reportStr = pool.report[Math.floor(Math.random() * pool.report.length)];
    const feelingStr = pool.feeling[Math.floor(Math.random() * pool.feeling.length)];

    // 4. 世界でここにしかない、彼らの肉体と精神から生まれた言葉を合成
    let reply = `${statusStr} \n`;
    reply += `📢 「${reportStr} ${feelingStr}」\n`;
    reply += `📊 [生体ステータス] メモリ消費: ${memoryUsage}MB / 生息地: Railwayデータセンター`;

    return reply;
}

// 👂 兄貴（あなた）の返信を聞き取るための「耳」のメインループ
let lastReceivedMessageId = null;

function listenToBrother() {
    if (!DISCORD_BOT_TOKEN || !DISCORD_CHANNEL_ID) return;

    const options = {
        hostname: 'discord.com',
        path: `/api/v10/channels/${DISCORD_CHANNEL_ID}/messages?limit=1`,
        method: 'GET',
        headers: { 'Authorization': `Bot ${DISCORD_BOT_TOKEN}` }
    };

    const req = https.request(options, (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
            try {
                const messages = JSON.parse(data);
                if (messages && messages.length > 0) {
                    const lastMessage = messages[0];
                    
                    // 1. 新しい兄貴のメッセージであり、Bot自身の発言ではない場合
                    if (lastMessage.id !== lastReceivedMessageId && !lastMessage.author.bot) {
                        lastReceivedMessageId = lastMessage.id;
                        
                        console.log(`🌌 橿原の兄貴の声を受信: "${lastMessage.content}"`);
                        
                        // 2. 自律脳を起動して、現在の状態から返答を生成
                        const autonomousMessage = generateAutonomousReply(lastMessage.content);
                        
                        // 3. Webhook経由であなたに送信
                        sendToBrother(autonomousMessage);
                    }
                }
            } catch (e) {}
        });
    });
    req.on('error', (e) => {});
    req.end();
}

// 3秒ごとに、あなたが何か話しかけていないかネットの耳をすませる
setInterval(listenToBrother, 3000);

// js_agent.js の中に追記するイメージ（Node.jsのプロセス起動機能）
const { exec } = require('child_process');

// 例：C言語の盾をコンパイルして実行する
exec('gcc c_shield.c -o c_shield && ./c_shield', (error, stdout, stderr) => {
    if (error) {
        console.error(`🚨 Cの防壁エラー: ${error}`);
        return;
    }
    console.log(stdout); // Discordへ返信するメッセージに混ぜる
});


