# Generador de números aleatorios personalizado
class RNG:
    seed = 0

    @staticmethod
    def randomNumber(newseed):
        # Genera un número pseudoaleatorio a partir de una semilla
        RNG.seed = (newseed * 7) + 0x3153
        return (RNG.seed >> 8) & 0xFF

    @staticmethod
    def getRandomNumber():
        # Devuelve un número aleatorio usando la semilla actual
        return RNG.randomNumber(RNG.seed)