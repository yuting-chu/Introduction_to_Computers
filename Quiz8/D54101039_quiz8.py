import csv
import chardet

# 偵測檔案(因為有ERROR:'utf-8' codec can't decode byte 0xa4 in position 125: invalid start byte)
with open("nba_standings.csv", "rb") as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

# 勝率的公式
def win_percentage(record):
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses)

# 讀資料
with open("nba_standings.csv", newline='', encoding=encoding) as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# Question 1 先找出屬於"Eastern"的球隊，再比較他們主場跟客場的勝率
eastern_teams = [row for row in data if row['Conference'] == 'Eastern']
q1_teams = [team['Team'] for team in eastern_teams if win_percentage(team['HOME']) < win_percentage(team['AWAY'])]

# Question 2 先得出兩邊隊伍的得分減失分，再算出平均，最後比較兩邊的平均
eastern_pf_minus_pa = [float(team['PF']) - float(team['PA']) for team in data if team['Conference'] == 'Eastern']
western_pf_minus_pa = [float(team['PF']) - float(team['PA']) for team in data if team['Conference'] == 'Western']

avg_pf_minus_pa_eastern = sum(eastern_pf_minus_pa) / len(eastern_pf_minus_pa)
avg_pf_minus_pa_western = sum(western_pf_minus_pa) / len(western_pf_minus_pa)

q2_conference = 'Eastern' if avg_pf_minus_pa_eastern > avg_pf_minus_pa_western else 'Western'

# Question 3 用對戰另一區的勝率排出隊伍的順序
data_sorted_by_inter_conf_wins = sorted(data, key=lambda team: win_percentage(team['CONF']), reverse=True)
ranked_teams = [team['Team'] for team in data_sorted_by_inter_conf_wins]

# 印出答案
print("Question 1:",q1_teams)

print("\nQuestion 2:",q2_conference)

print("\nQuestion 3:",ranked_teams)

