import datetime
import time
# from datetime import datetime, date, time
# now = datetime.datetime.now()
# # d = datetime.date(2012, 12, 14)
# # print(d.year) # 2012
# # print(d.day)  # 14
# # print(d.month)
# # print(datetime.date.today())
# # now = datetime.datetime.now()
# print(now)
# # a = datetime.datetime(2017, 3, 5)
# # print(a)  # datetime.datetime(2017, 3, 5, 0, 0)
# #
# # b = datetime.datetime(2017, 3, 5, 12, 30, 10)
# # print(b)  # datetime.datetime(2017, 3, 5, 12, 30, 10)
# #
# # d = datetime.datetime(2017, 3, 5, 12, 30, 10)
# # print(d.year)  # 2017
# # print(d.second)  # 10
# # print(d.hour)  # 12
# # c = datetime.datetime.today().strftime("%Y%m%d")
# # print(c)
# #
# # then = datetime.datetime(2020, 2, 17)
# # delta = then - now
#
# for x in range(5):
#     time.sleep(2)
#     print("Slept for 2 seconds")
#     print(datetime.datetime.now())
import datetime
import time
class MyOpen:

    def __init__(self, path, method):
        self.path = path
        self.method = method


    def __enter__(self):
        self.file = open(self.path, self.method, encoding='utf-8')
        self.start = datetime.datetime.now()
        # print(self.start)
        self.file.write(f'start: {self.start} \n')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.method == 'w':
            self.finish = datetime.datetime.now()
            # print(now)
            self.file.write(f'finish: {self.finish}\n')
            time_spent = self.finish - self.start
            self.file.write(f'Затраченное время: {time_spent}\n')

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]

with MyOpen('cook_book.txt', 'w') as test_file:
    person = int(input('Введите количество персон для подсчета продуктов: '))
    for dish in cook_book:
        time.sleep(1)
        for ingredient in dish[1]:
            test_file.write(f'{ingredient[0]} {ingredient[1] * person}, {ingredient[2]} \n')
