from datetime import date
d = 0b1111
m = 0b1100
y = 0b11111101001
start = date(y, m, d)
print(start.strftime('%d/%m/%y'))