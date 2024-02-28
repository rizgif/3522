class Engine:
    def __init__(self, temp):
        # self._name = name #directly setting name
        self.temperature = temp  # using property to set name

    def set_temperature(self, temp):
        print(f"setting temperature to {temp}")
        self._temp = temp

    def get_temperature(self):
        print(f"getting temperature {self._temp}")
        return self._temp

    temperature = property(get_temperature, set_temperature)


engine = Engine(100)
print(engine.temperature)

engine.temperature = 70
print(engine.temperature)
