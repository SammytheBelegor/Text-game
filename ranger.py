#A ranger's path
#a text game written on python
#There might be some references to the Lord of the Rings universe
import random
import time, os, sys
inventory = ['steel sword', 'journal book', 'health portion', 'torch']
health=random.randint(45,70)
def restart_game():
	time.sleep(2)
	restart=input("Do you wanna play again and explore more? (yes/no) ").lower().strip()
	if restart=="yes":
		time.sleep(2)
		print("All righty than!")
		time.sleep(2)
		os.execl(sys.executable, os.path.abspath('ranger.py'), *sys.argv)
	elif restart=="no":
		print("Such a pity but anyways thanks for playing my game!")
		time.sleep(2)
		quit()

def ending():
	time.sleep(2)
	print("Seems like these lads knew you and you decided to ask them to help you to remember.")
	time.sleep(3)
	print('"Well, '+name+'. You are a dunedain strider. Very known among free folk and in enemies rows as well.\nAs far as I remember you were on a mission given to you by Gandalf the Gray. \nHe said that we may meet you cause our missions are located pretty close."')
	time.sleep(3)
	print('You start remembering now. You set on the quest given by your good friend Gandalf to scout a band of \norc spies on the western slope of Misty Mountains.')
	time.sleep(3)
	print('"By the way, cap. Gandalf asked us to tell you to rush to Imladris if we meet you here. Seems like\nthere are more important things to take care of!')
	time.sleep(3)
	if act=="cave":
		print('You discussed something a bit longer with the dwarves (with Dwalin mainly) and than rushed to Rivendel\ncause you knew that Gandalf would not call without a vital reason!')
	elif act=="forest":
		print('You discussed something a bit longer with the elves (with Haldir mainly) and than rushed to Rivendel\ncause you knew that Gandalf would not call without a vital reason!')
	time.sleep(3)
	print("This is how your adventure goes on.\n    TO BE CONTINUED")
	restart_game()

def deadoralive():
	if health<=0:
		print("Unfortunately, this is the end of your story. You got too much damage.\n         GAME OVER!!!")
		restart_game()
	elif health>0 and health<30:
		print("Fortunately, you are alive after that battle but you are very wounded. \nAvoid fighting and... probably eating yellow snow")
	else:
		print("You have fought bravely. Well done!")
		time.sleep(3)
		return 
def introMon(): #The game starts with this function 
	print('You wake up in a very dark forest with your head hurting...')
	time.sleep(2)
	print('It seems like you were knocked off or maybe something fell on your head and you just zoned out!')
	time.sleep(2)
	print("You don't have time for thinking cause you feel dizzy and should find some help!")
	time.sleep(2)
	return

def battle(): #battle function with random stats
	global health
	enemy_health=random.randint(15,39)
	time.sleep(1)
	print("Your battle begins. \nYour health is "+str(health)+". Your enemy's health is "+str(enemy_health)+".")
	time.sleep(2)
	print("First move is yours. You can attack or defend yourself if health is low.")
	while  health>=0:
		act4=input("(a to attack/d to defend) ").lower().strip()
		time.sleep(1)
		if act4=="a":
			time.sleep(1)
			hero_damage=random.randint(8,16)
			enemy_health-=hero_damage
			print("You attack. You swang your sword and made "+str(hero_damage)+" points of danage. "+str(enemy_health)+" points of enemy's health remains!")
			if enemy_health<=0:
				break
		elif act4=="d":
			time.sleep(1)
			health+=5
			print("You thought defending is a better option. You get prepared for a strike and get plus 5 for health")
		time.sleep(2)
		enemy_damage=random.randint(3,14)
		health-=enemy_damage
		print("Your enemy strikes and makes "+str(enemy_damage)+" of damage. "+str(health)+" points of your health remains")
		time.sleep(3)
	deadoralive()
	time.sleep(2)
	return health

introMon()

name=input('You find a journal book and seems like your name is: ') #entering the name so that programm could speak to a player
time.sleep(2)
print("So "+name+" it is. You are remembering something. But memories\n are too blury. You need to look further!")
time.sleep(2)

def invent():
	print('You decide to look in your inventory cause there might be something useful.\nIt is all you have got:')
	print("Youe health is "+str(health)+" out of 100.")
	print(inventory)
	time.sleep(2)
	act = input('Do you need any of these? (yes or no) ').lower().strip()
	time.sleep(1)
	if act=='yes':
		item1=""
		while item1 != "quit":
			item1=input('Choose the item (sword, book, portion, torch and quit to quit) ').lower().strip()
			time.sleep(3)
			if item1=="sword":
				print("That is a long, steel sword. You can see some runes\n but you can't read them... yet.")
			elif item1=="book":
				print("Seems like it is your journal book. It says the book \nbelongs to "+name+". Seems legit don't you think. Also, it sais\n you belong to some kind of Dunedain folk and that swords\n name is Narsil in elvish.")
			elif item1=="portion":
				print("You may need a health portion when your life will be on the edge of the knife.")
			elif item1=="torch":
				print("Come on, dude. What can i say about a torch.")
			elif item1=="quit":
				print('Okie, '+ name)
			else:
				print('try again, smartass')
	else:
		print('Fine, '+name)
		print()
		time.sleep(2)
		return

invent()
print('All righty than the situation is not that bad. You have got some stuff in your bag.')
time.sleep(1)
print("But still you need to find out what to do next. You can see a decent\n pass through the forest. And also a cave that looked like an \nabandoned entrance because of it's square shape.")
time.sleep(4)
act=input("Which way to go? (forest or cave) ").lower().strip()
if act=="forest":
	time.sleep(2)
	print("You decide to go explore the forest path and went stride along the path.")
	time.sleep(2)
	print("Almost 2 hours passed and finally some signs of live. You found \nsome traces of feet that go further.")
	time.sleep(2)
	act2=input("Do you want to find to whom these footprints belong. (yes/no)").lower().strip()
	if act2=="yes":
		time.sleep(2)
		print("You decide to follow the footprints and finally you come across to a couple of orcs")
		time.sleep(2)
		print("Well, they haven't noticed you yet.")
		time.sleep(2)
		print("You noticed that you are very keen and stealthy. You kinda \ninstinctively knew what to do.")
		time.sleep(2)
		act3=input("You think you can use the advantage and attack them from behind\n or flee while they can't see you. (attack/flee) ").lower().strip()
		time.sleep(3)
		if act3=="attack":
			time.sleep(1)
			print("You decided that you cannot let those evil creatures live so you attack.\n You took one down but another one was cautios got prepared for the battle.")
			time.sleep(2)
			battle()
			print('A piece of a cake, huh?')
		elif act3=="flee":
			time.sleep(1)
			print("You decide that attacking is not the best idea. So you flee and continue your journey.")
			time.sleep(2)
			print("But when you were about to leave you accidently stepped on the branch and thus you were noticed.\n And also could not use the advantage of stealth.")
			time.sleep(2)
			battle()
			print("Good, 1 enemy left. You decide to take a health portion.")
			battle()
			print("That was a close one. You did well!")

	elif act2=="no":
		print("For good or bad you decide to avoid going there cause the footprints\n definitely belonged to bad creatures cause you could see blood spits.")
		time.sleep(3)
		print("GOD DAMMIT!!! When you were going to take another route an enemy scout \nattacked you from behind and made 20 points of damage")
		health-=20
		time.sleep(2)
		battle()
		print("Phew... that was a close one.")
	else:
		print("You have been thinking too long and could not decide where to go so you died because you got too bored")
		restart_game()

elif act=="cave":
	time.sleep(3)
	print("You decide to go explore the cave .Fortunately, you have a torch so darkness is not a problem.")
	time.sleep(3)
	print("It turns out it is not a cave at all. You went along greenish, polished halls. ")
	time.sleep(3)
	print("It is probably a dwarven craft. You thought it was abandoned but you found some traces.")
	time.sleep(3)
	print("...")
	time.sleep(3)
	print("After an hour of following them you heard some noises.")
	time.sleep(3)
	print("You sneaked up and found out it was a band of 7 goblins.")
	time.sleep(3)
	act5=input("Do you wanna attack or wait up until they leave. (yes/no) ").lower().strip()
	if act5=="yes":
		time.sleep(1)
		print("Wow, what an insane you are. Anyways, if you decide to do this let it be.")
		time.sleep(2)
		print("You could take one out because of stealth skill.")
		time.sleep(2)
		battle()
		print("3 of them are archeres and one of them could get you and made 15 point of damage.")
		health-=15
		time.sleep(2)
		print("Your health is low so you took a health portion! Watch out another one approaches! ")
		health+=40
		battle()
		print("You already defeated 3 of them but arches were a real danger. You cought another arrow (-10 health)")
		time.sleep(2)
		health-=10
		print("At the time archers were aiming you and you were on the edge of a knife you heard some crowds noise approaching!")
		time.sleep(3)
		print("You thought it was the end but it turns out enemies were not welcome for new comers.")
		time.sleep(2)
		print('These are dwarves! A gang of 10 dwarves rushed and killed the orc archers and an arbalet bolt killed another melee orc!')
		time.sleep(2)
		print('"Hey,'+name+'"-said one of the dwarves. "Surprised and glad to see you here.\nDid almost half of our job, hah?"-said the dwarve with a smile on his face.')
		ending()
	elif act5=="no":
		time.sleep(1)
		print("You decide to wait up and not risk. A few minutes later you heard some feet noises aapproaching. More enemies???")
		time.sleep(3)
		print("No... these are dwarves!! Allies they were to the Dunedain folk as it is said in your book. They already killed 3 of them cause they were greater in numbers.")
		time.sleep(4)
		print('You decide to help them anyways and make one orc fighter to face you.')
		battle()
		print("These dwarves were great at fighting and did not loose any dwarf in their 10-person group.")
		time.sleep(3)
		print("One of the dwarves appocahes to you and cries out:")
		time.sleep(3)
		print('"'+name+'??? Didnt expect to see you here. Thanks for the help thoguh we did not needed it"-said one of the dwarves as if ke knew you.')
		time.sleep(3)
		ending()

else:
	print("You have been thinking too long and could not decide where to go so you died because you got too bored")
	restart_game()

time.sleep(3)
print('You continued your path along the forest. And suddenly "'+name+'"-someones pleasant voice cried out.')
time.sleep(3)
print('A few elves went out of woods. They seemed friendly. "Mae gowannen, mellon"- was pronounced the same voice.')
time.sleep(4)
print('It seemed like an unknown speach but turns out you can understand it.')
time.sleep(3)
print('"You seem strange today, mellon. As if you have forgotten who we are."')
time.sleep(3)
print('"Sorry, but seems like i have lost my mind. I woke up in the forest a few hours ago."-you said.')
time.sleep(3)

if act2=="yes":
	print('"Later i found some traces and followed them. Turned out they belonged to a couple of orcs.')
	time.sleep(3)
	print('I defeated them and continued going along the path and now i am here".')
	ending()
elif act2=="no":
	print('"Later i decided to go along a forest path. About an hour later i was attacked by an orc spy.')
	time.sleep(2)
	print('He made a good cut but fortunately i defeated him. Than i continued going through the forest and thus I am here".')
	time.sleep(2)
	ending()