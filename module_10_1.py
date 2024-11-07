import threading
import time

print('------\nЗадача "Потоковая запись в файлы"\n------')

def write_words(word_count, file_name):
    with open(file_name, 'a+', encoding='utf-8') as file:
        i = 1
        while i <= word_count:
            file.write(f'Какое-то слово № {i}\n')
            i += 1
            time.sleep(0.01)
    print(f'Завершилась запись в файл {file_name}')

start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

fin = time.time()
print(f'Работа потоков {fin - start}')

start_2 = time.time()

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

fin_2 = time.time()
print(f'Работа потоков {fin_2 - start_2}')

print('------')