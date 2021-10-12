import random
#from main import player

items = ["HP Potion", "Big HP Potion", "Full restore", "Sword", "Long Sword", "B.F. Sword", "Cloth Armor", "Leather Armor", "Iron Suit", "Boots", "Swiftness Boots", "Mach Boots", "Rejuv. Bead", "Rejuv Totem", "Rejuv Armguard"]

item_value = [50,80,999,3,7,12,2,2,2,2,2,2,3,6,12]

fightinventory = [3,1,4]

enemy = random.randint(0,4)
if enemy == 0:
  enemyfile = open("Enemies/Fighter")
  enemycontent = enemyfile.readlines()
  e_name = enemycontent[1]
  e_hp = int(enemycontent[3])
  e_atk = int(enemycontent[5])
  e_def = int(enemycontent[7])
  e_spd = int(enemycontent[9])
  e_mat = enemycontent[11]
  e_check = enemycontent[13]
  e_xp = enemycontent[15]

elif enemy == 1:
  enemyfile = open("Enemies/Tank")
  enemycontent = enemyfile.readlines()
  e_name = enemycontent[1]
  e_hp = int(enemycontent[3])
  e_atk = int(enemycontent[5])
  e_def = int(enemycontent[7])
  e_spd = int(enemycontent[9])
  e_mat = int(enemycontent[11])
  e_check = enemycontent[13]
  e_xp = enemycontent[15]

elif enemy == 2:
  enemyfile = open("Enemies/Assassin")
  enemycontent = enemyfile.readlines()
  e_name = enemycontent[1]
  e_hp = int(enemycontent[3])
  e_atk = int(enemycontent[5])
  e_def = int(enemycontent[7])
  e_spd = int(enemycontent[9])
  e_mat = int(enemycontent[11])
  e_check = enemycontent[13]
  e_xp = enemycontent[15]

elif enemy == 3:
  enemyfile = open("Enemies/Goblin")
  enemycontent = enemyfile.readlines()
  e_name = enemycontent[1]
  e_hp = int(enemycontent[3])
  e_atk = int(enemycontent[5])
  e_def = int(enemycontent[7])
  e_spd = int(enemycontent[9])
  e_mat = int(enemycontent[11])
  e_check = enemycontent[13]
  e_xp = enemycontent[15]

elif enemy == 4:
  enemyfile = open("Enemies/Goblin")
  enemycontent = enemyfile.readlines()
  e_name = enemycontent[1]
  e_hp = int(enemycontent[3])
  e_atk = int(enemycontent[5])
  e_def = int(enemycontent[7])
  e_spd = int(enemycontent[9])
  e_mat = int(enemycontent[11])
  e_check = enemycontent[13]
  e_xp = enemycontent[15]

print("You encountered a", e_name[0:len(e_name)-1] + "!")
while player.Hp and e_hp > 0:
  print("Your HP:", player.Hp)
  print("Enemy HP:", e_hp)
  print("What will you do?")
  print("1) Fight")
  print("2) Check")
  print("3) Item")
  print("4) Flee")
  choice = input("------>")
  while choice not in ("1", "2", "3", "4"):
    choice = input("------>")
  if choice == "1" and e_spd <= player.Spd:
    e_hp -= player.Atk 
    e_hp += e_def
    print("You attack the", e_name[0:len(e_name)-1], "and deal", (player.Atk - e_def), "damage!")
    if e_hp <= 0:
      print("The", e_name[0:len(e_name)-1], "dropped", e_mat, "gold")
      player.Gold += e_mat
    if e_hp > 0:
      print("The", e_name[0:len(e_name)-1],"swings back! You recieve", e_atk - player.Def, "damage!")
      player.Hp -= e_atk
      player.Hp += player.Def
  elif choice == "1" and e_spd > player.Spd:
    print("The", e_name[0:len(e_name)-1], "swings first! You recieve", e_atk - player.Def, "damage!")
    player.Hp -= e_atk
    player.Hp += player.Def
    e_hp -= player.Atk 
    e_hp += e_def
    print("You attack the", e_name[0:len(e_name)-1],"and deal", (player.Atk - e_def), "damage!")
  elif choice == "2":
    print("You glance carefully at the", e_name[0:len(e_name)-1])
    print("HP:", e_hp)
    print("ATK:", e_atk)
    print("DEF:", e_def)
    print("SPD:", e_spd)
    print("Gold Dropped:", e_mat)
    print(e_check)
    print("The", e_name[0:len(e_name)-1],"got mad at your creepy stare and attacked!")
    print("Your recieved", (e_atk - player.Def), "damage!")
    player.Hp -= e_atk
    player.Hp += player.Def
  elif choice == "3":
    print("You have 1:", fightinventory[0], items[0])
    print("You have 2:", fightinventory[1], items[1])
    print("You have 3:", fightinventory[2], items[2])
    itemchoice = input("Select your item")
    while itemchoice not in ("1", "2", "3"):
      itemchoice = input("Select an item number on the list")
    if itemchoice == "1":
      if fightinventory[0] <= 0:
        print("You tried to drink a", items[0], "but you didn't have any!")
        print("You attack the", e_name[0:len(e_name)-1],"and deal", (player.Atk - e_def), "damage!")
        player.Hp -= e_atk
        player.Hp += player.Def
      else:
        print("You drank a", items[0], "and recovered", item_value[0], "health")
        player.Hp += item_value[0]
        fightinventory[0] -= 1
        if player.Hp > player.MaxHP:
          player.Hp = player.MaxHP
          print("Your health won't go any higher")
    elif itemchoice == "2":
      if fightinventory[1] <= 0:
        print("You tried to drink a", items[1], "but you didn't have any!")
        print("You attack the", e_name[0:len(e_name)-1],"and deal", (player.Atk - e_def), "damage!")
        player.Hp -= e_atk
        player.Hp += player.Def
      else:
        print("You drank a", items[1], "and recovered", item_value[1], "health")
        player.Hp += item_value[1]
        fightinventory[1] -= 1
        if player.Hp > player.MaxHP:
          player.Hp = player.MaxHP
          print("Your health won't go any higher")
    elif itemchoice == "3":
      if fightinventory[2] <= 0:
        print("You tried to drink a", items[2], "but you didn't have any!")
        print("You attack the", e_name[0:len(e_name)-1],"and deal", (player.Atk - e_def), "damage!")
        player.Hp -= e_atk
        player.Hp += player.Def
      else:
        print("You drank a", items[2], "and recovered", item_value[2], "health")
        player.Hp += item_value[2]
        fightinventory[2] -= 1
        if player.Hp > player.MaxHP:
          player.Hp = player.MaxHP
          print("Your health won't go any higher")
  elif choice == "4":
    e_hp -= e_hp
    print("You fled the battle.")
print("your gold:",player.Gold)