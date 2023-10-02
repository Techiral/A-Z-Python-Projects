import time
h = int(input("Enter the Hour:- ")); m = int(input("Enter the Minutes:- ")); s = int(input("Enter the Seconds:- "))
i = 0; j = 2
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = ["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
D = int(input("Enter the Date:- ")); M = int(input("Enter the Month:- ")); Y = int(input("Enter the Year:- "))
indi = dict(zip(month,month_days))

while i < j:
	time.sleep(1)
	s += 1
	if s == 60:
		m += 1
		Y += 1
		s = 0
		if m == 60:
			h += 1
			m = 0
			if h == 24:
				D += 1
				h = 0
				if D == 30:
					M += 1
					D = 0
					if M == 12 and h == 24:
						Y += 1
						m = 0
	print("time:", h, ":", m, ":", s, "|", "Date:", D, "-", M, "-", Y)