
class Figure:
    sides_count = 0
    __color = [255, 255, 255]
    def __init__(self, sides):
        self.sides = sides
        #self.filled = False
        if (self.sides_count == 12 and len(sides) != self.sides_count and
            all(x == sides[0] for x in sides) == False):
            print(f'У куба 12 сторон, а не {len(sides)}')
            print('Задайте верное кол-во одинаковых сторон')

        elif (self.sides_count == 12 and len(sides) == self.sides_count and
            all(x == sides[0] for x in sides) == False):
            print('Вы ввели правильное число сторон, но стороны не равны')
            print('Попробуйте снова')

        else:
            print(sides)
            print('Ура, вы справились!')


    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
            else:
                return False
        else:
            return False
    def set_color(self, r, g, b):
            if self.__is_valid_color(r, g, b):
                self.__color = [r, g, b]
                print(self.__color)
            else:
                print('Ошибка цвета')

    def __is_valid_sides(self,*sides):
        if len(sides) == self.sides_count or int(self.sides) > 0:
            return True
        else:
            return False
    def get_sides(self, *sides):
        if self.__is_valid_sides(*sides):
           print (self.sides)

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if self.sides_count == 1 and len(new_sides) != self.sides_count:
            print(self.sides)
        elif self.sides_count == 3 and len(new_sides) != self.sides_count:
            print(self.sides)
        elif (self.sides_count == 12 and len(new_sides) != self.sides_count and
              all(x == new_sides[0] for x in new_sides) == False):
            self.sides = 1
            print([self.sides] * 12)


        elif (self.sides_count == 12 and len(new_sides) == self.sides_count and
              all(x == new_sides[0]for x in new_sides) == False):
               print('Введены некорректные данные, введите одинаковое кол-во сторон')

        elif (self.sides_count == 12 and len(new_sides) != self.sides_count and
              all(x == new_sides[0]for x in new_sides) == True):
                print(self.sides)

        else:
            print([*new_sides])

class Circle(Figure):
    sides_count = 1
    def __init__(self, __color, sides):
        super().__init__(sides)

    def get_square(self):
        __radius = self.sides / 2
        print (round(3.14 * (__radius ** 2)))

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *sides):
       super().__init__([*sides])

    def get_square(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, *sides):
        super().__init__([*sides])
        if len(self.sides) < self.sides_count and all(x == self.sides[0]for x in self.sides) == True:
            print('Вы задали неверное кол-во параметров')


    def get_volume(self):
        print (self.sides[0]**3)


circle1 = Circle((200, 200, 200), 17)
#cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
circle1.set_color(55, 666, 77)
circle1.set_sides(4)
circle1.get_square()

triangle1 = Triangle((255, 34, 134), 66, 55, 77)
triangle1.set_color(54, 55, 57)
triangle1.set_color(545, 55, 57)
#triangle1.set_sides(22)
if len(triangle1.sides) != triangle1.sides_count:
    print(f'У треугольника три стороны, а не {len(triangle1.sides)}')
    print('Задайте верное кол-во сторон')
else:
    print(triangle1.sides)
triangle1.set_sides(22, 66, 88, 88)
triangle1.set_sides(22, 33, 44)

print()
cube1 = Cube((22, 55, 135), 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22)
print()
cube1.set_color(65, 55, 11)
cube1.set_color(665, 55, 11)

cube1.set_sides(23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23)
cube1.get_volume()













