class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self. speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, i'm peaceful :)")
        else:
            print(f"Be careful, i'm attacking you 0_0")

class Bird(Animal):
    def __init__(self, species):
        super().__init__(species)
        self.beak = True

    def lay_eggs(self):
        num_eggs = random.randint(1, 4)
        print(f'Here are(is) {num_eggs} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords['z'] -= dz * 0.5


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, name, species):
        super().__init__(name, species)

    def get_degree_of_danger(self):
        return self._DEGREE_OF_DANGER

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):

    def init(self):
        self.sound = "Click-click-click"
        super().__init__(self)

    def speak(self):
        print(str(self.sound))

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()





