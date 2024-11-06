import threading
from time import sleep
from random import randint
from queue import Queue

print('------\nЗадача "Потоки гостей в кафе"\n------')

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3,10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        flag = False
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    flag = True
                    break
                else:
                    flag = False
            if flag == False:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
        print()

    def discuss_guests(self):
        count = len(self.tables)
        while not self.queue.empty() or count:
            for table in self.tables:
                if not table.guest is None:
                    if table.guest.is_alive():
                        continue
                    else:
                        print(f'{table.guest.name} покушал(-а) и ушел(ушла)\n Стол номер {table.number} свободен\n')
                        table.guest = None
                        count -= 1
                else:
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        count += 1
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}\n')
                        table.guest.start()


tables = [Table(number) for number in range(1,6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Anatolii', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()

print('------')