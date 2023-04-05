class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
    def get_x_coordinate():
        return self.__x_coordinate
    def shift():
        pass

    

def main():
    point_A = Point()
    point_B = Point()
    if point_A == point_B:
        print("I due punti coincidono")

    if point_B == Point():
        print("Il punto si trova nell'origine degli assi")

    point_C = point_B - point_A
    print(point_C.get_x_coordinate(), point_C.get_y_coordinate)
if __name__ == '__main__':
    main()