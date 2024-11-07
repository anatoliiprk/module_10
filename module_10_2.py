import threading
import time

print('------\nЗадача "За честь и отвагу"\n------')

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        day_count = 0
        while enemies > 0:
            time.sleep(1)
            day_count += 1
            enemies -= self.power
            print(f'{self.name} сражается {day_count} день(дня), осталось {enemies} врагов')
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')

print('------')