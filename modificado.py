import threading
import time

semaphore = threading.Semaphore(1)

def tarea(id):
    print(f"Tarea {id} intentando acceder al recurso")
    with semaphore:
        print(f"Tarea {id} ha adquirido el semáforo")
        time.sleep(2)
        print(f"Tarea {id} ha liberado el semáforo")

threads = []
for i in range(5):
    thread = threading.Thread(target=tarea, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()