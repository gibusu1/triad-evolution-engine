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
