class Display:
    def __init__(self):
        self.current_floor = 0
        self.direction = None  # 'up', 'down', o None (si está parado)

    def update(self, current_floor, direction):
        self.current_floor = current_floor
        self.direction = direction

    def show(self):
        print(f"Piso actual: {self.current_floor}, Dirección: {self.direction}")
        
if __name__ == "__main__":

    display = Display()
    display.show()  # Piso actual: 0, Dirección: None

    display.update(3, 'up')
    display.show()  # Piso actual: 3, Dirección: up

    display.update(1, 'down')
    display.show()  # Piso actual: 1, Dirección: down