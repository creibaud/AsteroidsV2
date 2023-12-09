import sys
import core.settings.memory as memorySettings
import core.settings.screen as screenSettings
import core.settings.SpaceShip as spaceShipSettings
import core.settings.bullet as bulletSettings
import core.settings.asteroid as asteroidSettings
import core.settings.game as gameSettings
import core.screen as screenSetUp
import core.SpaceShip as spaceShipSetUp
import core.game as gameSetUp
import core.asteroid as asteroidSetUp
import core.bullet as bulletSetUp

def memory(key: object, value: object = None) -> object:
    if " " in key:
        sys.stderr.write("ERREUR : Espace interdit dans les noms de variable : " + key + "\n")
        sys.exit()
    
    if value is not None:
        memorySettings.MEMORY_STORAGE[key] = value
    else:
        try:
            return memorySettings.MEMORY_STORAGE[key]
        except:
            sys.stderr.write("ERREUR : Nom de variable inconnue : " + key)
            sys.exit()

def printMemory():
    print("--------------MEMORY:-------------------")
    for k, v in memorySettings.MEMORY_STORAGE.items():
        print("Nom : ", k, " Valeur :", v, " Type : ", type(v))
    print("----------------------------------------")
    print("\n")