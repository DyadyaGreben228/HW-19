import time
import threading

#1
#for i in range(1):
#    time.sleep(1)
#    d = open("file.txt", "w")
#    d.close()
#print("suscs")
f = 0

#2
#for i in range(1, 101):
#    time.sleep(1)
#    with open(f"file_{i}.txt", "w") as file:
#        f += 1
#        print(f+"секунда")



#3
# def create_file(i):
def create_file(i):
    time.sleep(1)
    with open(f"file_{i}.txt", "w") as file:
        print(f"File {i} created after {i} second(s)")

# Замер времени начала выполнения
start_time = time.time()

# Запускаем потоки
threads = []
for i in range(1, 101):
    thread = threading.Thread(target=create_file, args=(i,))
    threads.append(thread)
    thread.start()

# Ожидаем завершения всех потоков
for thread in threads:
    thread.join()

# Замер времени окончания выполнения
end_time = time.time()

# Подсчитываем и выводим общее время выполнения
elapsed_time = end_time - start_time
print(f"All files created in {elapsed_time:.2f} seconds")