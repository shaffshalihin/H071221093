from praktikum9_pp_H071221093_no_1 import Warrior, Assasin, Support
warrior = Warrior("bambang", pos_x=10)
assassin = Assasin("joko", pos_x=25)
support = Support("udin",pos_x=30)
# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print()

# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())
print()

# sebelum
print("assasin (health)", assassin.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(assassin)
# sesudah
print("assassin (health)", assassin.getHealth())
print("Support (speed): ",support.getSpeed())