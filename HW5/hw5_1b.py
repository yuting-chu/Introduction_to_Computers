#hw5_1b
#經濟系大三 D54101039朱郁庭

#import random模組
import random

#把撲克牌的花色跟數字建立好
card_num=["ACE",2,3,4,5,6,7,8,9,10,"JACK","QUEEN","KING"]
card_suit=["SPADE", "HEART", "DIAMOND","CLUB"]

#定義抽卡函式
def new_card(card,card_with_hand):
	num=random.choice(card_num)
	suit=random.choice(card_suit)
	name=suit+str(num)
	#card是一個divtionary，key代表第幾張牌，value代表卡牌花色數字
	card[len(card)]=name
	#牌不能重複
	if len(card)>1:
		for j in range(len(card)-1):
			if card[len(card)-1]==card[j]:
				del card[len(card)-1]
				continue
	draw=str(num)+"-"+suit
	if card_with_hand[-1]!=':':
		card_with_hand+=','
	card_with_hand+=" "+draw
	return num,draw,card_with_hand

#定義計算總和函式
def calculate_value(num,value,ace):
	if num=="JACK" or num=="QUEEN" or num=="KING":
		value+=10
	elif num=="ACE":
		value+=11
		ace+=1
	else:
		value+=num
		while ace>0:
			if value>21:
				value-=10
				ace-=1
			else:
				break
	return value,ace

#定義總和狀態
def value_condition(value):
	if value>21:
		condition="Bust! (>21)"
	elif value==21:
		condition="Blackjake! (21)"
	else:
		condition=value
	print(current_value,condition,card_with_hand,"\n")
	return condition

#進入大迴圈，可重複遊戲
while True:
	#建立需要的變數
	card={}
	player="Your"
	hit_stay=0
	you_value=0
	dealer_value=0
	end=0
	dealer_wins=0
	you_win=0
	nobody_wins=0
	#進入小迴圈，開始一局遊戲
	while True:
		#將需要的變數設定好
		value=0
		ace=0
		condition=0
		current_value="\n"+player+" current value is"
		card_with_hand="\nwith the hand:"
		
		#執行兩次的for迴圈代表每個人初始的兩張牌
		for i in range(2):
			num,draw,card_with_hand=new_card(card,card_with_hand)
			#計算總和
			value,ace=calculate_value(num,value,ace)

		#玩家的回合
		if player=="Your":
			while True:
				#根據不同總和要輸出不同的句子
				condition=value_condition(value)
				#一旦總和超過21就輸了
				if condition=="Bust! (>21)":
					end=1
					dealer_wins=1
					break
				#詢問是否要再次抽牌
				hit_stay=int(input("Hit or stay? (Hit = 1, Stay = 0): "))
				#要抽牌的狀況
				if hit_stay==1:
					num,draw,card_with_hand=new_card(card,card_with_hand)
					print("You draw",draw)
					value,ace=calculate_value(num,value,ace)
				#不抽牌的狀況
				elif hit_stay==0:
					#將玩家的數字儲存
					you_value=value
					break
			#如果有結束的狀況就跳出迴圈
			if end==1:
				break
			#換成莊家的回合
			player="Dealer's"
			continue

		#莊家的回合
		elif player=="Dealer's":
			while True:
				#根據不同總和要輸出不同的句子
				condition=value_condition(value)
				#如果總和超過17就不再抽牌
				if value>=17:
					break
				#總和不到17就一直加牌，加到超過17為止
				while value<17:
					num,draw,card_with_hand=new_card(card,card_with_hand)
					print("Dealer draws",draw)
					value,ace=calculate_value(num,value,ace)
			#只要超過21就輸了
			if condition=="Bust! (>21)":
				you_win=1
				break
			else:
				#儲存莊家的總值
				dealer_value=value
				break

	#輸出最後結果
	if dealer_wins==1 or dealer_value>you_value:
		print("*** Dealer wins! ***\n")
	elif you_win==1 or dealer_value<you_value:
		print("*** You beat the dealer! ***\n")
	elif dealer_value==you_value:
		print("*** You tied the dealer, nobody wins. ***\n")

	#詢問是否要在玩一次
	again=input("Want to play again? (y/n): ")
	#要的話輸出分割線並再次進入大迴圈
	if again=='y':
		print("\n---------------------------------")
		continue
	#不要的話跳出迴圈
	elif again=='n':
		breakn