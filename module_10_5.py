import multiprocessing
import time


print('------\nЗадача "Многопроцессное считывание"\n------')

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1,5)]


# Линейный вызов
start1 = time.time()

read_info(filenames[0])
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])

fin1 = time.time()
print(f'Время выполнения программы: {fin1 - start1} (линейный вызов)')

'''
# Многопроцессорный вызов
start2 = time.time()

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        result = pool.map(read_info, filenames)

fin2 = time.time()
print(f'Время выполнения программы: {fin2 - start2} (многопроцессорный вызов)')
'''

print('------')