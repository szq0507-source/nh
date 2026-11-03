# ==========================================
# Python 猜拳遊戲：裝備技能強化版
# ==========================================

import random  # 召喚處理「隨機」的魔法模組

# 1. 冒險者登入
name = input("請輸入你的冒險者名字：")

# 裝備選單設定
equipments = {
    "1": {"name": "黃金鍵盤", "skill": "雙倍傷害", "desc": "勝利時獲得 2 勝 (每局限用 1 次)"},
    "2": {"name": "魔法魔杖", "skill": "護盾護體", "desc": "輸掉時不計電腦得分 (每局限用 1 次)"},
    "3": {"name": "幸運草護身符", "skill": "平手算贏", "desc": "平手時直接算你獲勝 (每局限用 1 次)"}
}

print("\n=== 🎒 請選擇你的初始裝備 ===")
for key, eq in equipments.items():
    print(f"【{key}】{eq['name']} - 技能：[{eq['skill']}] {eq['desc']}")

eq_choice = input("\n請輸入裝備編號 (1 / 2 / 3)：").strip()
while eq_choice not in equipments:
    eq_choice = input("⚠️ 無效選擇，請重新輸入裝備編號 (1 / 2 / 3)：").strip()

selected_eq = equipments[eq_choice]

# 印出前置劇情
print("\n=== 系統廣播 ===")
print(f"歡迎勇敢的冒險者【{name}】！")
print(f"你已經裝備了【{selected_eq['name']}】（技能：{selected_eq['skill']}），準備好迎接【猜拳】挑戰！")

options = ["剪刀", "石頭", "布"]

# 主遊戲迴圈
while True:
    print("\n\n=== ✊✋✌️️ 剪刀石頭布 終極大對決 ===")
    print("規則：先獲得 5 勝的一方就是最終贏家！\n")

    player_wins = 0
    computer_wins = 0
    round_num = 1
    skill_used = False  # 記錄該局遊戲技能是否已使用

    # 單局遊戲迴圈
    while player_wins < 5 and computer_wins < 5:
        print(f"--- 第 {round_num} 回合 ---")
        print(f"🏆 目前戰況 - 你：{player_wins} 勝 | 電腦：{computer_wins} 勝")
        
        # 顯示技能狀態
        if not skill_used:
            print(f"✨ 裝備技能【{selected_eq['skill']}】：可以使用 (輸入「技能」觸發)")
        else:
            print(f"❌ 裝備技能【{selected_eq['skill']}】：本局已使用過")

        # 玩家出拳
        player_choice = input("請出拳 (輸入 剪刀、石頭、布，或輸入「技能」發動技能)：").strip()

        # 判斷是否使用技能
        use_skill_this_round = False
        if player_choice == "技能":
            if skill_used:
                print("⚠️ 本局技能已經使用過了！請重新選擇出拳。\n")
                continue
            else:
                use_skill_this_round = True
                skill_used = True
                print(f"🔥 發動裝備技能【{selected_eq['skill']}】！")
                player_choice = input("請出拳 (輸入 剪刀、石頭 或 布)：").strip()

        # 檢查玩家是否輸入錯誤
        if player_choice not in options:
            print("⚠️️ 哎呀！指令錯誤，請輸入 剪刀、石頭 或 布。\n")
            if use_skill_this_round:
                skill_used = False  # 如果輸入錯誤，返還技能次數
            continue

        # 電腦隨機出拳
        computer_choice = random.choice(options)
        print(f"🤖 電腦出了：{computer_choice}")

        # 勝負判斷
        if player_choice == computer_choice:
            # 技能：幸運草護身符 (平手算贏)
            if use_skill_this_round and selected_eq['name'] == "幸運草護身符":
                print("🍀 幸運草生效！平手局直接算你獲勝！🎉\n")
                player_wins += 1
            else:
                print("平手！沒有人得分。\n")

        elif (player_choice == "剪刀" and computer_choice == "布") or \
             (player_choice == "石頭" and computer_choice == "剪刀") or \
             (player_choice == "布" and computer_choice == "石頭"):
            
            # 技能：黃金鍵盤 (雙倍傷害)
            if use_skill_this_round and selected_eq['name'] == "黃金鍵盤":
                print("⌨️ 黃金鍵盤爆擊！獲得 2 勝！🎉🎉\n")
                player_wins += 2
            else:
                print("🎉 這回合你贏了！\n")
                player_wins += 1

        else:
            # 技能：魔法魔杖 (護盾護體)
            if use_skill_this_round and selected_eq['name'] == "魔法魔杖":
                print("🪄 魔法護盾阻擋了攻擊！電腦本回合無法得分！🛡️\n")
            else:
                print("💥 這回合電腦贏了！\n")
                computer_wins += 1

        round_num += 1

    # 最終結算
    print("=== 🌟 最終結果 🌟 ===")
    if player_wins >= 5:
        print(f"🏆 恭喜你以 {player_wins} : {computer_wins} 擊敗了電腦，成為剪刀石頭布大師！")
    else:
        print(f"💻 很可惜，電腦以 {computer_wins} : {player_wins} 獲得了最終勝利，下次再來挑戰吧！")

    # 詢問是否再玩一次
    play_again = input("\n想要再玩一次嗎？(輸入 y 重新開始，其他鍵結束)：").strip().lower()
    if play_again != "y":
        print("感謝遊玩，下次見！")
        break

# ==========================================