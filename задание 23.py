n=int(input())
if 1<=n<=86400:
	hour=n//3600
	min=(n%3600)//60
	sec=n%60
	print(hour,'часов',min,'минут',sec,'секунд')