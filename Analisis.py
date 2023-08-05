import threading
import time

# Definición de interfaz para los vehículos
class IVehiculo:
    def iniciar(self):
        pass
    
    def detener(self):
        pass

# Implementación de la clase Automovil que cumple con la interfaz IVehiculo
class Automovil(IVehiculo):
    def __init__(self):
        self.iniciado = False
        self.lock = threading.Lock()  # Bloqueo para manejar concurrencia
    
    def iniciar(self):
        with self.lock:
            if not self.iniciado:
                self.iniciado = True
                print("\nIniciando automóvil...")
                # Simulando tiempo de inicio
                time.sleep(2)
            else:
                print("\nEl automóvil ya está iniciado.")
    
    def detener(self):
        with self.lock:
            if self.iniciado:
                self.iniciado = False
                print("Deteniendo automóvil...")
                # Simulando tiempo de detención
                time.sleep(2)
            else:
                print("El automóvil ya está detenido.")

# Implementación de la clase Bicicleta que cumple con la interfaz IVehiculo
class Bicicleta(IVehiculo):
    def __init__(self):
        self.iniciado = False
        self.lock = threading.Lock()  # Bloqueo para manejar concurrencia
    
    def iniciar(self):
        with self.lock:
            if not self.iniciado:
                self.iniciado = True
                print("\nIniciando bicicleta...")
                # Simulando tiempo de inicio
                time.sleep(1)
            else:
                print("\nLa bicicleta ya está iniciada.")
    
    def detener(self):
        with self.lock:
            if self.iniciado:
                self.iniciado = False
                print("Deteniendo bicicleta...")
                # Simulando tiempo de detención
                time.sleep(1)
            else:
                print("La bicicleta ya está detenida.")

# Función para mostrar el menú y gestionar vehículos
def gestionar_vehiculos():
    vehiculos = [Automovil(), Bicicleta()]

    while True:
        print("\nSeleccione un vehículo:")
        print("1. Automóvil")
        print("2. Bicicleta")
        print("3. Ver vehículos iniciados")
        print("4. Salir")

        try:
            opcion = int(input("Ingrese el número de opción: "))

            if opcion == 1 or opcion == 2:
                vehiculo = vehiculos[opcion - 1]

                print("\n¿Qué desea hacer?")
                print("1. Iniciar")
                print("2. Detener")

                accion = int(input("Ingrese el número de acción: "))

                if accion == 1:
                    num_vehiculos = int(input("Ingrese el número de vehículos a iniciar: "))
                    hilos = []

                    for _ in range(num_vehiculos):
                        hilo = threading.Thread(target=vehiculo.iniciar)
                        hilos.append(hilo)
                        hilo.start()

                    for hilo in hilos:
                        hilo.join()
                elif accion == 2:
                    vehiculo.detener()
                else:
                    print("Acción inválida. Por favor, seleccione una acción válida.")
            elif opcion == 3:
                vehiculos_iniciados = [v for v in vehiculos if v.iniciado]
                if vehiculos_iniciados:
                    print("\nVehículos iniciados:")
                    for v in vehiculos_iniciados:
                        print("- ", type(v).__name__)
                else:
                    print("No hay vehículos iniciados.")
            elif opcion == 4:
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

if __name__ == "__main__":
    gestionar_vehiculos()
