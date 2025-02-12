class ButtonArray:
    def __init__(self, num_floors, is_elevator_panel=False):
        self.buttons = []
        if is_elevator_panel:
            # Para el panel dentro del elevador, solo necesitamos botones para cada piso
            for floor in range(num_floors):
                self.buttons.append(Button(floor=floor))
        else:
            # Para los paneles de piso, necesitamos botones de subida y bajada
            for floor in range(num_floors):
                self.buttons.append(Button(floor=floor, direction='up'))
                self.buttons.append(Button(floor=floor, direction='down'))

    def get_button(self, floor, direction=None):
        for button in self.buttons:
            if button.floor == floor and (direction is None or button.direction == direction):
                return button
        return None

if __name__ == "__main__":

    button_array = ButtonArray(5)
    button = button_array.get_button(3, 'up')
    print(button.is_pressed)  # False

    button.press()
    print(button.is_pressed)  # True

    button.reset()
    print(button.is_pressed)  # False

    button = button_array.get_button(3, 'down')
    print(button.is_pressed)  # False

    button.press()
    print(button.is_pressed)  # True

    button.reset()
    print(button.is_pressed)  # False    