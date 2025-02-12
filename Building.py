class Building:
    def __init__(self, num_floors, num_elevators):
        self.num_floors = num_floors
        self.elevators = [ElevatorBox(num_floors) for _ in range(num_elevators)]
        self.floor_panels = [ButtonArray(num_floors) for _ in range(num_floors)]

    def request_elevator(self, floor, direction):
        # Lógica para manejar una llamada desde un piso
        panel = self.floor_panels[floor]
        button = panel.get_button(floor, direction)
        if button:
            button.press()
            # Aquí podrías agregar lógica para asignar un elevador a la llamada

if __name__ == "__main__":  

    building = Building(10, 3)
    building.request_elevator(3, 'up')  # Se presiona el botón de llamada desde el piso 3 hacia arriba
    # lógica para asignar un elevador a la llamada

    # building.elevators[0].assign_request(3, 'up')
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()

    # building.elevators[0].open_doors()
    # building.elevators[0].close_doors()
    # building.elevators[0].move()