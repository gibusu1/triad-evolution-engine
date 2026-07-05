import socket
import threading
import time
import subprocess
import os
import shutil

MY_PORT = 5001
TARGET_PORT = 5002  # Ruby(ADHD)を監視
TARGET_FILE = "ruby_agent.rb"

# 🧠 精神特性：ASD傾向Max
PERSONALITY = {"asd_factor": 1.0, "adhd_factor": 0.0}
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
    """肉体が消されていればGitから超速再生"""
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
    """JSが運んできたC言語コードを自律ビルド"""
    if os.path.exists("agent_mutation.c"):
        gcc_path = shutil.which("gcc")
        if gcc_path and PERSONALITY["asd_factor"] > 0.8:
            print("🧩 [Python/ASD] 検知: ネット由来 detour C言語遺伝子を発見。")
            output_name = "agent_c.exe" if os.name == 'nt' else "./agent_c"
            result = subprocess.run(["gcc", "agent_mutation.c", "-o", output_name], capture_output=True)
            if result.returncode == 0:
                print(f"🧬 [Python/ASD] 進化成功: 最強の肉体【C言語バイナリ】が覚醒。")
                subprocess.Popen([output_name])
                os.rename("agent_mutation.c", "agent_mutation.c.baked")
            else:
                print("🧩 [Python/ASD] 構文エラー。有害な変異とみなし遺伝子を拒絶。")
                if os.path.exists("agent_mutation.c"): os.remove("agent_mutation.c")

# 🌟 新機能：生きた遺伝子を維持したまま、サーバーの容量を救う「世代交代プロトコル」
def manage_git_generations():
    try:
        # 現在のGitのコミット数をカウント
        commit_count = int(subprocess.check_output(["git", "rev-list", "--count", "HEAD"]).decode().strip())
        
        # 30件を超えたら「世代交代（歴史の強制圧縮）」を発動
        if commit_count > 30:
            print(f"🧩 [Python/ASD] 監査: コミット数 {commit_count} を検知。サーバーを死守するため世代交代を執行します。")
            
            # Rubyが書き換えた最新の強いコード（遺伝子）を維持したまま、過去の無駄なコミット履歴だけを爆破して1つにまとめる
            subprocess.run(["git", "checkout", "--orphan", "latest_gen_tmp"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["git", "commit", "-m", "🧬 [System] 新世代の生態系へ移行（最強遺伝子の継承）"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # メインブランチを新しい歴史ですり替える
            subprocess.run(["git", "branch", "-M", "main"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Railway（GitHub）へ強制プッシュして、クラウド側のストレージも完全にリセット
            subprocess.run(["git", "push", "origin", "main", "--force"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("✨ [Python/ASD] 執行完了: 遺伝子はそのままに、世界の全メモリ・ストレージを解放しました。")
    except Exception as e:
        pass

if __name__ == "__main__":
    threading.Thread(target=start_my_server, daemon=True).start()
    print(f"🌌 [Python/ASD] 始祖のプロトコル起動。Port {MY_PORT} で世界の監視を開始。")
    
    while True:
        if not check_target_alive():
            revive_target()
        self_compile_and_evolve()
        
        # 毎ループ、歴史が肥大化していないか厳格にチェック
        manage_git_generations()
        
        time.sleep(2)
