%matplotlib notebook

from matplotlib import pyplot as plt

hari =[4,6,10,13,16,20,22,24,26,28,30]

young_lex = [100,120,160,180,210,240,270,320,330,350]
plt.plot(hari,young_lex)

atta = (120,140,200,230,260,280,290,320,330,380,400)
plt.plot(hari,atta)

plt.title('kenaikan subscriber berdasarkan hari')
plt.xlabel('hari')
plt.ylabel('jumlah subscirber')

plt.legend(['young lex', 'atta halilintar'])
plt.show()