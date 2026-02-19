class GameCharacter:
    """
    Docstring for GameCharacter\n
    This class represents a game character with attributes such as name, health, mana, and level.
    It includes methods to level up the character and to display the character's stats.\n
    Attributes
    - name (str): The name of the character.
    - health (int): The health points of the character, ranging from 0 to 100.
    - mana (int): The mana points of the character, ranging from 0 to 50.
    - level (int): The level of the character, starting at 1
    """
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self._health = 0        
        elif new_health > 100:
            self._health = 100
        else:
            self._health = new_health
        
    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        
        print(f"{self.name} leveled up to {self.level}!")
    
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

hero = GameCharacter('Kratos')
hero.health -= 80
hero.mana -= 20
print(hero)
hero.level_up()
print(hero)
hero.level_up()
print(hero)
