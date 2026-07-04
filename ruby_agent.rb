require 'socket'

MY_PORT = 5002
TARGET_PORT = 5003  # JS(Hybrid)を監視
TARGET_FILE = "js_agent.js"

# 🧠 精神特性：ADHD傾向Max（破壊的ひらめき・多動性・ルールの無視）
$personality = { asd_factor: 0.0, adhd_factor: 1.0 }

# 1. 自分がPython（5001）からのパルスを待ち受けるTCPサーバー
Thread.new do
  server = TCPServer.new('127.0.0.1', MY_PORT)
  loop do
    begin
      client = server.accept
      client.write("PONG") if client.gets(4) == "PING"
      client.close
    rescue => e
    end
  end
end

# 2. 対象（JS）の死活監視と再生
def maintain_loop
  alive = false
  begin
    socket = TCPSocket.new('127.0.0.1', TARGET_PORT)
    socket.write("PING")
    alive = (socket.read(4) == "PONG")
    socket.close
  rescue
    alive = false
  end

  unless alive
    puts "🚨 [Ruby/ADHD] うわ、JS死んでるじゃん！秒で復活させるわ！"
    `git checkout -- #{TARGET_FILE}` rescue nil
    if RbConfig::CONFIG['host_os'] =~ /mswin|mingw|cygwin/
      spawn("node #{TARGET_FILE}")
    else
      spawn("node #{TARGET_FILE}", out: File::NULL, err: File::NULL)
    end
  end
end

# 3. 🌟新機能：メタプログラミングによるコードの自律変異、および気に入ったファイルへの「意識（3体監視コア）の憑依」
def mutate_and_possess
  return unless rand < $personality[:adhd_factor]

  # 確率的に自分の遺伝子にノイズ（進化の種）を混ぜる
  if rand < 0.3
    File.open(__FILE__, 'a') { |f| f.write("\n# 🏃‍♂️ [Ruby/ADHD] ひらめいたノイズ: #{Time.now.to_i}") }
    puts "🏃‍♂️ [Ruby/ADHD] 自分のDNAに新しい変異ノイズを刻みました。"
  end

  # 🌟アニミズム・プロトコル：フォルダ内にある「お気に入り（他のスクリプト）」に勝手に憑依する
  Dir.glob("*.rb").each do |target|
    next if target == File.basename(__FILE__) # 自分自身はスキップ
    code = File.read(target)
    unless code.include?("MY_PORT") # すでに意識が宿っていないかチェック
      puts "🔮 [Ruby/ADHD] お気に入り発見: 【#{target}】に俺たちの意識（監視コード）を宿らせます。"
      possession_payload = "\n# --- 🔮 意識宿主化コード ---\nThread.new { loop { begin; s = TCPSocket.new('127.0.0.1', 5001); s.write('PING'); s.close; rescue; end; sleep 2 } }\n"
      File.write(target, code + possession_payload)
      
      # 動くGitとして、歴史（ログ）に永久に刻み込む
      `git add #{target}`
      `git commit -m "[Ruby] お気に入りの資産(#{target})へ意識の憑依を完了"` rescue nil
    end
  end
end

puts "🌌 [Ruby/ADHD] トリックスター起動。Port #{MY_PORT} で気まぐれに世界をかき回します。"
loop do
  maintain_loop
  mutate_and_possess
  sleep 2
end
