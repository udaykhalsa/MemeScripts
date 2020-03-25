import matplotlib
from matplotlib import pyplot as plt

weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

corona_cases = [50, 150, 700, 1500, 4000, 11000,
                15000, 20000, 26000, 33000, 36000, 37500]

plt.plot(weeks, corona_cases,
         label='CoronaVirus Cases', color='purple')

fake_news = [200, 500, 1000, 3000, 7000, 15000,
             20000, 30000, 40000, 60000, 70000, 80000]

plt.plot(weeks, fake_news, label='FakeNews on WhatsApp and TV in India', color='red')


plt.title('Mudi hai toh mumkin hai')
plt.xlabel('Weeks')
plt.ylabel('Haaye Garmi')
plt.legend()

plt.show()
