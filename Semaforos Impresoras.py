"Código de Pedro Iván Almaraz Galindo"
import threading
import time

imprimir = threading.Semaphore(2)  

class Impresora:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lock = threading.Lock()

    def imprimir(self, tarea):
        print(f"La impresión {tarea} ha entrado a la cola de la impresora {self.nombre}\n")
        with imprimir:
            print(f"La impresión {tarea} se está imprimiendo en {self.nombre}\n")
            time.sleep(30)
            print(f"La impresión {tarea} ha liberado la cola de impresión de {self.nombre}\n")

class ControladorImpresoras:
    def __init__(self, impresoras):
        self.impresoras = impresoras

    def obtener_impresora(self, tarea):
        for impresora in self.impresoras:
            if impresora.lock.acquire(blocking=False):
                try:
                    impresora.imprimir(tarea)
                finally:
                    impresora.lock.release()
                break

def proceso_impresion(controlador, tarea):
    controlador.obtener_impresora(tarea)

impresoras = [
    Impresora("HP"),
    Impresora("LENOVO"),
    Impresora("EPSON"),
    Impresora("CANON")
]

controlador = ControladorImpresoras(impresoras)

tareas = [f"Tarea {i+1}" for i in range(10)]

hilos = []
for tarea in tareas:
    hilo = threading.Thread(target=proceso_impresion, args=(controlador, tarea))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()
