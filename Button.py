class Button:
    def __init__(self, floor=None, direction=None):
        self.floor = floor  # Piso al que está asociado el botón (si es un botón de piso)
        self.direction = direction  # Dirección (si es un botón de llamada: 'up' o 'down')
        self.is_pressed = False  # Estado del botón (presionado o no)

    def press(self):
        self.is_pressed = True
        # Aquí podrías agregar lógica para notificar al sistema que el botón ha sido presionado

    def reset(self):
        self.is_pressed = False
        
if __name__ == "__main__":

    button = Button(3, 'up')
    print(button.is_pressed)  # False

    button.press()
    print(button.is_pressed)  # True

    button.reset()
    print(button.is_pressed)  # False
    