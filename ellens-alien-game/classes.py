class Alien:

    total_aliens_created = 0

    def __init__(self, x_coodridane, y_coordinate) -> None:
        self.x_coordinate = x_coodridane
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return False if self.health <= 0 else True

    def teleport(self, x_coodridane, y_coodridane):
        self.x_coordinate = x_coodridane
        self.y_coordinate = y_coodridane

    def collision_detection(self, object):
        pass


def new_aliens_collection(positions):
    """Function taking a list of position tuples, creating one Alien instance per position.

    :param positions: list - A list of tuples of (x, y) coordinates.
    :return: list - A list of Alien objects.
    """
    return [Alien(position[0], position[1]) for position in positions]
