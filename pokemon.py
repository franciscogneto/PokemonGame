class Pokemon:

    def __init__(self,specie,name=None, level=1):
        self.specie = specie
        self.name = name if name else specie
        self.level = level
        pass

    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.level)
    
    def atack(self, pokemon:Pokemon):
        pass


class EletricPokemon(Pokemon):
    type = "Eletric"

    def atack(self, pokemon:Pokemon):
        pass


class FirePokemon(Pokemon):
    type = "Fire"
    
    def atack(self, pokemon:Pokemon):
        pass

class WaterPokemon(Pokemon):
    type = "Water"
    
    def atack(self, pokemon:Pokemon):
        pass
