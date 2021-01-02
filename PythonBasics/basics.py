from dataclasses import dataclass

@dataclass
class Player:
        name = str
        age = int
        gender = str

        def data(self):
            name = input("Enter you name: ")
            age = int(input("Enter Your Age: "))
            gender = input("Enter Your Gender: ")
            print("Your name is:",name)
            print("Your age is:",age)
            print("Your Gender is:",gender)

class Game(Player):

    def play(self,game):
        age = 67
        print("Game we are playing called:", game)
        power = 50
        print("You have 10 power.Which you can use later on to save yourself.")
        print(age)
        if age >= 18:
            print("You are old enough...")
            wants_to_play = input("Do you want to play an amazing game with us? ").lower()
            if wants_to_play == "yes":
                print("Let's play....")
                left_or_right = input("First choice... Left or Right (left/right)?")
                if left_or_right == "left":
                    ans = input(
                        "Nice, you followed the right path and reach a lake.Do you want to swim across or go around (across/around).").lower()
                    if ans == "around":
                        print("You went around and reached the other side of lake.")
                    elif ans == "across":
                        print("You bit by a fish and lost 5 power.")
                        power -= 5
                        print("you left with ", power, "power")
                        ans = input("You notice a house and a river .Which one you choose? (River/house)").lower()
                        if ans == "house":
                            print(
                                "You entered house and greeted by the owner.He doesn't like you.And you lose 5 power.")
                            power -= 5
                            if power <= 0:
                                print("You left with 0 power and lose the game.")
                            else:
                                print("You have survived..")
                        else:
                            print("You fell in the river and lost.")

                    else:
                        print("You lost....")
                else:
                    print("You fell down and lose...")

            else:
                print("See youuuuuuuuu Again ")
        elif age >= 14:
            print("You can go and play with toys.Not here.")
        else:
            print("You are not old enough.....")

    def exitFromGame(self):
        exit()

game1 = Game()
list_mine = [game1.data,game1.play,game1.exitFromGame]
print("1. Yes \n  2.Let's Play\n 3.Exit")
ch = int(input("Enter your choice: "))
output = list_mine[ch -1]()
print(output)

