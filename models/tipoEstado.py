from enum import Enum 

class TipoEstado(Enum):
    BUENO = 'Bueno'
    AL_CADUCAR = 'Al_caducar'
    CADUCADO = 'Caducado'
    NO_DISPONIBLE = 'No_disponible'
    
    @staticmethod
    def choices():
        return [(estado.name, estado.value) for estado in TipoEstado]