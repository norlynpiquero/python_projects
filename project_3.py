from datetime import date
Year = input("What is your year of birth? [ex. 1988]")
Month = input("What is your birth month in number")
Day = input("What is your day of birth")
print('Your date of birth is ', (Day + "/" + Month + "/" + Year))

date_today = date.today().year

your_age = date_today - int(Year)
print(your_age)

if ((int(Month)==12 and int(Day)>=22) or (int(Month)==1 and int(Day)<=19)):
    sign = ("\n Capricorn")
elif ((int(Month)==1 and int(Day) >= 20)or(int(Month)==2 and int(Day)<= 18)):
    sign = ("\n aquarius")
elif ((int(Month)==2 and int(Day) >= 19)or(int(Month)==3 and int(Day)<= 20)):
    sign = ("\n Pisces")
elif ((int(Month)==3 and int(Day) >= 21)or(int(Month)==4 and int(Day)<= 19)):
    sign = ("\n Aries")
elif ((int(Month)==4 and int(Day) >= 20)or(int(Month)==5 and int(Day)<= 20)):
    sign = ("\n Taurus")
elif ((int(Month)==5 and int(Day) >= 21)or(int(Month)==6 and int(Day)<= 20)):
    sign = ("\n Gemini")
elif ((int(Month)==6 and int(Day) >= 21)or(int(Month)==7 and int(Day)<= 22)):
    sign = ("\n Cancer")
elif ((int(Month)==7 and int(Day) >= 23)or(int(Month)==8 and int(Day)<= 22)):
    sign = ("\n Leo")
elif ((int(Month)==8 and int(Day) >= 23)or(int(Month)==9 and int(Day)<= 22)):
    sign = ("\n Virgo")
elif ((int(Month)==9 and int(Day) >= 23)or(int(Month)==10 and int(Day)<= 22)):
    sign = ("\n Libra")
elif ((int(Month)==10 and int(Day) >= 23)or(int(Month)==11 and int(Day)<= 21)):
    sign = ("\n Scorpio")
elif ((int(Month)==11 and int(Day) >= 22)or(int(Month)==12 and int(Day)<= 21)):
    sign = ("\n Sagittarius")

print("Your zodiac sign is",sign)