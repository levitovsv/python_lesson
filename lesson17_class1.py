from hero import Hero
# -------------- MAIN -----------------

myhero1 = Hero("Vurdalak", 5, "ork")
myhero2 = Hero("Alexandr", 4, "Human")
myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
#myhero1.health=70
myhero1.set_health(60)
myhero1.show_hero()

