#! python3

# The player must choose the options. 
# They may try to guest the animal will be present and reach the score more than 10 during encounter the animals. 

import time, math, random, sys, textwrap
import textgame, constants


class Game(object):
    def __init__(self):
        self.done = False
        self.score = 5          # 10 score is the goal to win
        self.energy = 5         # 5 is the starting energy
        self.full = 10          # 10 is the maximum energy 
        self.turns = 0          # the number of game you takes

    def intro(self):
        for char in textwrap.dedent(constants.INTRO):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

        time.sleep(0.1)

    def random_object(self,value):
        if value == 1:
            return "route"

        elif value == 2:
            return "wolf"
        
        elif value == 3:
            return "bear"
        
        else:
            return "tiger"

    def status(self):
        # Alert User with energy
        print(f"Your energy is {self.energy}")
        
        # Alert user with score 
        print(f"Your score is {self.score}")

    def random_event(self, choice):
        if choice != "s":
            i = random.randint(1,4)
            return i
        else:
            return 0

    def increase_energy(self):
        if self.energy < self.full:
            self.energy += 1
        
        else:
            print("\nYour energy reach the maximum.")

    def apply_choice(self, choice, randvalue):
        if choice.lower().strip(".,! ") == "q":
            self.done = True

        elif choice.lower().strip("!,. ") == "s":
            print(f"""
            ---Status Check---
    energy: {self.energy}
    score: {self.score}
    for sucess {10 - self.score} socre behind you.   
    lost {self.score} score will failed.
    
""")

        elif choice.lower().strip(",.! ") == "r":
            self.increase_energy()
            if randvalue == 1:
                print("\n A new path appears. You increased energy and your score remains the same.")
            
            else:
                self.score -= 1
                print(f"\nWhile you are resting you encounter {self.random_object(randvalue)}. lose 1 point.")


        elif choice.lower().strip("!,. ") == "d":
            if self.energy > 1:
                if randvalue == 4:
                    self.energy -= 1
                    self.score -= 1
                    print("\n You encounter Tiger! Tiger is fast, and you are caught. lost 1 score.")
                
                elif randvalue == 1:
                    self.energy -= 1
                    self.score -= 1
                    print("\n You have missed a easier route to home. You lose 1 point!")

                else:
                    self.score += 1
                    print("\n You detour correctly, gets 1 score.")
                self.energy -= 2

            else:
                self.score -= 1
                print("\n Your energy is used up, you cannot detour! lost 1 points.")

        elif choice.lower().strip("!,. ") == "e":
            if randvalue == 1:
                self.score += 1
                print("\n You explore a new route, gets 1 point.")

            else:
                self.score -= 1
                print("\nYou did not explore anything, lose 1 point.")

        elif choice.lower().strip("!,. ") == "f":    
            if randvalue == 4:
                self.energy -= 1
                self.score -=1 
                print("\nTiger's speed is really fast and comes to attack you. Fortunately it is not hungry and it walks away.")
              
            elif randvalue == 1:
                self.energy -= 1
                self.score -=1 
                print("\nYou have missed a easier route to home. You lose 1 point!")

            else:
                print(f"\nGood job {self.random_object(randvalue)} cannot reach you! Your score keeps the same.")

        elif choice.lower().strip("!,. ") == "h": 
            if randvalue == 1:
                self.score -= 1
                print("\nThere is a route appears to your sight, but unfortunately you choose to hide, so your score minus 1.")

            else:
                self.score += 1   
                print(f"\nA {self.random_object(randvalue)} pass by you, but since you are hide at a great spot it did not see you. Score plus 1!")

    def end_game(self):
        ending = None

        # The Win Condition
        if self.score > 9 or self.turns > 9:
            time.sleep(2)
            ending = f"""\
            ------------------------ 
            ...Lucky for you! A helicopter is patrol nearby, it saw you and arrived to help you!
            Without losing anything you are safely back home.
            It takes you {self.turns} turns.
            The Helicopter will bring you home.

            -------- Game Over -------- 
            """
            self.done = True        

        # end game for agents catching up
        elif self.score < 0:
            ending = f"""\
                
                ---------------------
                ...... Failed! ......
                You now is trapped in the forest without any food or water left in your backpack.
                
                After two days of hunger you 
                You failed in {self.turns} turns.
                If continue you may have less chance to success.
                More risk will be present to you if continue.
                You should change your strategy or pick options way.
                
                -------- Game Over --------
                """

            self.done = True

        if self.done == True:
            if ending != None:
                for char in textwrap.dedent(ending):
                    time.sleep(0.05)
                    sys.stdout.write(char)
                    sys.stdout.flush()

                print(f"\nYou finished the game in {self.turns} turns.\n")
            else:
                print("Thanks for playing!")

    def update(self):
        # Main Instructions
        print(constants.CHOICES)

        self.status()

        choice = input("What do you want to do? ")
        self.turns += 1
        r = self.random_event(choice.lower())
        self.apply_choice(choice.lower(),r)

        self.end_game()
        time.sleep(1)
