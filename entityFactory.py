from Const import WIN_WIDTH
from background import Background
from barrel import Barrel
from oil import Oil

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Pista0': # Ajustado para aceitar nomes específicos de pista
                return Background(entity_name, position)
            case 'Level1Pista1':
                return Background(entity_name, position)
            case 'Level1Pista2':
                return Background(entity_name, position)
            case 'Barrel01': # Nome do barril ajustado
                return Barrel(position)
            case 'Oil':
                return Oil(position)
            case _:
                return None