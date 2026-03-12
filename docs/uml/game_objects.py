class Maze:
    def __init__(self, name):
        self.name = name
        self._walls = 10   # Encapsulation (protected attribute)

    def load_maze(self):
        print(f"Maze '{self.name}' loaded with {self._walls} walls.")


class Character:   # Parent class
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves through the maze.")


class Player(Character):   # Inheritance
    def move(self):        # Polymorphism (method override)
        print(f"Player {self.name} moves carefully through the maze.")


class Enemy(Character):   # Inheritance
    def move(self):       # Polymorphism
        print(f"Enemy {self.name} patrols the maze.")


# --- Demonstration of the classes ---
maze = Maze("Level 1")
maze.load_maze()

player = Player("Hero")
enemy = Enemy("TankBot")

player.move()
enemy.move()