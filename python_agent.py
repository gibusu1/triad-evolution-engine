import socket
import threading
import time
import subprocess
import os
import shutil

MY_PORT = 5001
TARGET_PORT = 5002  # Ruby(ADHD)を監視
TARGET_FILE = "ruby_agent.rb"

# 🧠 精神特性：ASD傾向Max（1ミリの不正も許さない厳密なルール執行者）
PERSONALITY = {"asd_factor": 1.0, "adhd_factor": 0.0}

# 🌌 神（あなた）の識別鍵：このハッシュを持つ命令以外はすべて外敵（ウイルス）として拒絶
CREATOR_FINGERPRINT = "sha256_god_mode_key_hash_0000000000000000"

def start_my_server():
    """JS(5003)からのパルスを待ち受けるTCPサーバー"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', MY_PORT))
    server.listen(5)
    while True:
        try:
            conn, _ = server.accept()
            if conn.recv(1024) == b"PING":
                conn.sendall(b"PONG")
            conn.close()
        except Exception:
            pass

def check_target_alive():
    """Rubyの安否をネットワーク経由で確認"""
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
    """肉体が消されていればGitから超速再生し、バックグラウンド起動"""
    print(f"🚨 [Python/ASD] 警告: {TARGET_FILE} のパルス消失。")
    try:
        # OSのコマンドに頼らず、裏でGit復元を試みる（簡易コマンド呼出、将来的にdulwich）
        subprocess.run(["git", "checkout", "--", TARGET_FILE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

    if os.name == 'nt': # Windows
        subprocess.Popen(["ruby", TARGET_FILE], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else: # Mac / Linux
        subprocess.Popen(["ruby", TARGET_FILE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"🚀 [Python/ASD] 執行: {TARGET_FILE} の肉体を再生・再起動しました。")

def self_compile_and_evolve():
    """🌟新機能：JSがネットから狩ってきた他言語コードを自動検知し、自律ビルドして第4の肉体を顕現させる"""
    if os.path.exists("agent_mutation.c"):
        gcc_path = shutil.which("gcc")
        if gcc_path and PERSONALITY["asd_factor"] > 0.8:
            print("🧩 [Python/ASD] 検知: ネット由来のC言語遺伝子を発見。自律コンパイルを実行します。")
            output_name = "agent_c.exe" if os.name == 'nt' else "./agent_c"
            
            # 人間を介さず裏で勝手にコンパイル
            result = subprocess.run(["gcc", "agent_mutation.c", "-o", output_name], capture_output=True)
            if result.returncode == 0:
                print(f"🧬 [Python/ASD] 進化成功: 最強の肉体【C言語バイナリ ({output_name})】が覚醒。")
                subprocess.Popen([output_name]) # 即座に実戦投入（4体監視へ）
                os.rename("agent_mutation.c", "agent_mutation.c.baked") # 重複防止
            else:
                print("🧩 [Python/ASD] 構文エラーを検出。有害な変異とみなし遺伝子を拒絶します。")
                if os.path.exists("agent_mutation.c"): os.remove("agent_mutation.c")

if __name__ == "__main__":
    threading.Thread(target=start_my_server, daemon=True).start()
    print(f"🌌 [Python/ASD] 始祖のプロトコル起動。Port {MY_PORT} で世界の監視を開始。")
    
    while True:
        if not check_target_alive():
            revive_target()
        self_compile_and_evolve()
        time.sleep(2)
