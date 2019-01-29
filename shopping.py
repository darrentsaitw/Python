nyear = 2019

powlist = ["滑鼠",'主機','螢幕','筆記型電腦',"鍵盤"]
foodlist = ["麵包","餅乾","蛋糕","牛肉","魚肉","蔬菜"]
uselist = ["衛生紙","馬克杯","牙膏","雨傘","牙刷"]
drinklist = ["啤酒","白酒","伏特加","紅酒","威士忌"]

print("此為購物車程式，如須購買，請按照指示進行，購物產品有：\n\n1.電子",powlist,"\n2.食品",foodlist
												,"\n3.日用品",uselist,"\n4.酒類",drinklist)

print()

def date(agree):
	while True:	
		year = int(input("請輸入西元年份(yyyy必塡)：") or "0")
		if year == 0:
			print("請重新輸入")				
			continue
		if agree == True:
			if 1911>year :
				print("請輸入正確年份",year)
				continue
		else:
			if 1911>year or year>nyear:
				print("請輸入正確年份",year)
				continue
		month = int(input("請輸入月份(mm必塡):") or "0")
		if month ==0:
			print("請重新輸入")
			continue
		
		if 12 < month or month< 0:
			print("月份不得小於0，且不得大於12")
			continue

		day = int(input("請輸入日期(dd必塡):") or "0")
		if day ==0:
			print("請重新輸入")
			continue

		if year%400 == 0 or year%100 != 0 or year%4 == 0:
			if month == 2:
			 	if 0>day or day> 29:
			 		print("該年為閏年，二月最多29天，最少1天，請確認。",day)
			 		continue
		if month in [1,3,5,7,8,10,12]:
			if 0>day or day>31:
				print("請確認輸入之日期正確,該月%d月最多有31天" % month)
				continue
		elif month in [2,4,6,9,11]:
			if 0>day or day>30:
				print("請確認輸入之日期正確,該月%d月最多有30天" % month)
				continue
		daylist = [year,month,day]
		break
	return(daylist)

#主邏輯始
agree = False
date1 = date(agree)
print("結算日期為：%s/%s/%s" % (date1[0],date1[1],date1[2]))
discountlist = []

while True:
	discount = float(input("請輸入折扣優惠(不再輸入請直接按Enter)：") or "0")			
	if discount == 0:
		break				
	kind = int(input("請選取商品種類:電子產品請輸入1，食品請輸入2，日用品請輸入3，酒類請輸入4："))
	
	if kind == 1:
		kind = "電子"
	elif kind == 2:
		kind = "食品"
	elif kind == 3:
		kind = "日用品" 
	elif kind == 4:
		kind = "酒類"
	else:
		continue

	if kind in discountlist:
		check = input("該種類折扣已有，請確認是否做變更？%s %1.3f(y/n)"
			%(discountlist[discountlist.index(kind)],discountlist[discountlist.index(kind)-1]))
		if check == "y" or check == "Y":
			discountlist[discountlist.index(kind)],discountlist[discountlist.index(kind)-1] = [kind,discount]
		else:
			continue
	else:
		discountlist += [discount,kind]

print("所輸入的折扣優惠為：",discountlist)
print()   #為了空行

tprice = 0
something = [] 

while True:
	number = int(input("請輸入該商品購買數量(不再輸入請直接按Enter)：") or "0")
	if number == 0:	
		break
	articles = input("請輸入該商品名稱：")

	discountf = lambda x :discountlist[discountlist.index(x)-1]  #創建函數
	
	if articles in powlist and "電子" in discountlist:
		discount = discountf("電子")
	
	elif articles in foodlist and "食品" in discountlist:
		discount = discountf("食品")
	
	elif articles in uselist and "日用品" in discountlist:
		discount = discountf("日用品")
	
	elif articles in drinklist and "酒類" in discountlist:
		discount = discountf("酒類")
	
	else:
		discount = 1

	price = float(input("請輸入該商品單價："))

	something += [number,articles,price]   #最後列印出購買所有的產品

	print("您輸入的商品為：",number,"*",articles,"*",price)
	
	tprice += number * price * discount

for x in range(0,len(something)-1,3):
	print(something[x],something[x+1],something[x+2],"\n")	

check2 = input("請問是否有一千送三百的優惠卷？（y/n）") or "n"
while True:	
	if check2 == "y" or check2 == "Y":
		print("請按順序輸入優惠卷的日期")
		agree = True
		date2 = date(agree)
		if date2 <= date1:
			print("該優惠卷已過期")
			check3 = input("是否繼續輸入另一張優惠卷(y/n)?")
			if check3 == "y" or check3 == "Y":
				continue
			else:
				check2 = "n" or check2 == "N"
				continue
		print("\n輸入之優惠卷日期:%s/%s/%s" % (date2[0],date2[1],date2[2]),"優惠卷為滿一千折三百\n" )
		if tprice >= 1000:
			print("總共要付的金額:%10.2f" %(tprice-300))
			break
		else:
			print("總共要付的金額:%10.2f" %tprice)
			break
	else:
		print("總共要付的金額:%10.2f" %tprice)
		break

			