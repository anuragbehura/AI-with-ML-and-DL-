from datetime import date

y = date.today().year
m = date.today().month
d = date.today().day

print(date.today())

year = int(input("Enter Your Birth Year: "))
month = int(input("Enter Your Birth Month: "))
day = int(input("Enter Your Birth Day: "))

if day > d and month >= m:
    dd = (d + 30) - day
    mm = ((m -1) + 12 ) -month
    yy = (y - 1) - year
    print(str(yy) + " Years "+ str(mm)+" Months "+str(dd)+" Days")

elif day > d and month < m:
    dd = (d + 30) - day
    mm = m - month
    yy = y - year
    print(str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days")

elif day < d and month > m:
    dd = d- day
    mm = (m + 12) - month
    yy = (y - 1) - year
    print(str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days")

else:
    dd = d - day
    mm = m - month
    yy = y - year
    print(str(yy) + " Years " + str(mm) + " Months " + str(dd) + " Days")

