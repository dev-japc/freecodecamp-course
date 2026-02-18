class Planet():
    '''
    Docstring for Planet
    A class to represent a planet.
    Attributes:
    ----------
    name : str
        
    planet_type : str
        The type of the planet (e.g., terrestrial, gas giant).
    star : str
        The star that the planet orbits around.
    Methods:
    -------
    __init__(self, name, planet_type, star):
        Initializes the Planet with a name, planet type, and star.
    __str__(self):
        Returns a string representation of the Planet.
    orbit(self):
        Returns a string indicating that the planet is orbiting its star.
    '''

    # defining __init__ method
    def __init__(self, name, planet_type, star):
        '''
        Docstring for __init__
        self: The instance of the class.
        name: The name of the planet.
        planet_type: The type of the planet (e.g., terrestrial, gas giant).
        star: The star that the planet orbits around.
        '''
        # Assigning the values passed in to the instance attributes name,
        # planet_type, and star.
        self.name = name
        self.planet_type = planet_type
        self.star = star

        #  listing attributes to validate their values
        attributes = [name, planet_type, star]

        for attr in attributes:
            if not isinstance(attr, str):
                raise TypeError('name, planet type, and star must be strings')

            if attr == '':
                raise ValueError('name, planet_type, and star must be non-empty strings')

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    '''try:
        for var in variables:
            if not isinstance(var, str):
                raise TypeError('name, planet type, and star must be strings')

            if var == '':
                # Nota: Cambié el 'elif' por 'if' por limpieza, ya que si es str, 
                # de todas formas queremos validar que no esté vacío.
                raise ValueError('name, planet_type, and star must be non-empty strings')
                
        except TypeError as e:
            print(f"Error de tipo: {e}")
            # Aquí puedes decidir si el programa se detiene o hace otra cosa
        except ValueError as e:
            print(f"Error de valor: {e}")
    '''

planet_1 = Planet('venus',' rocky','sun')
planet_2 = Planet('balard','gasy','bettlejuice')
planet_3 = Planet('cotton','cotton','candy')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())