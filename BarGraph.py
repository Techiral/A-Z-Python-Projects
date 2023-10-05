import matplotlib.pyplot as plt
companies = ['Google', 'Amazon', 'Microsoft', 'FB']
revenues = [100, 110, 80, 145]
profits = [15, 20, 10, 30]
xpos = [0, 1, 2, 3]
firstx = []
secondx = []
for i in range(len(xpos)):
    firstx.append(xpos[i]-0.2)
    secondx.append(xpos[i]+0.2)
plt.bar(xpos, revenues, label='Revenue')
plt.ylabel('Revenue')
plt.xticks(xpos, companies)
plt.legend()
plt.show()

import matplotlib.pyplot as plt
companies = ['Google', 'Amazon', 'Microsoft', 'FB']
revenues = [100, 110, 80, 145]
profits = [15, 20, 10, 30]
xpos = [0, 1, 2, 3]
firstx = []
secondx = []
for i in range(len(xpos)):
    firstx.append(xpos[i]-0.2)
    secondx.append(xpos[i]+0.2)
plt.bar(firstx, revenues, width=0.4, label='Revenue')
plt.bar(secondx, profits, width=0.4, label='Profits')
plt.title('Revenues & Profits')
plt.xticks(xpos, companies)
plt.legend()
plt.show()
