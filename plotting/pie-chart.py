import matplotlib.pyplot as plt

labels = 'R','Python', 'SPSS', 'SAS', 'Excel'
sizes = [22, 14, 18,9,5]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','orange']
explode = (0.1, 0, 0, 0,0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True)

plt.axis('equal')
plt.show()
