# Class Project - sprint01 - Base Code Design - 06/17/2021

# Here we put the import files
import random

# Here we declare global variables
program_over = True    # sets the main loop to run

# Here we will define our classes and functions
class MainMenu:  # This is the main menu

    def intro():
        print("Hello, welcome to the math tutor program.")
        print("I am your tutor and I am here to help you learn.")
        print("You may choose from the following options: ")
        print(" 1. Directions")
        print(" 2. Start Program")
        print(" 3. Quit")

        choice = input("\n What do you choose to do? ")

        if choice == "1":
            MainMenu.directions()
        elif choice == "2":
            play = TheBrain
        elif choice == "3":
            print("Goodbye!")
            program_over = False
            quit()
        else:
            print(" Please try again.")
            press = input("\n Please press Enter to continue.")

    def directions():
        print("Greetings! I am your virtual math tutor.")
        print("I am here to help you learn math.")
        print("You can choose to do addition, subtraction, multiplication, or division.")
        print("If you solve the problem correctly you will earn score points.")
        print("If you do not answer correctly, you will not get any score points.")

        press = input("\n Please press Enter to continue.")




class TheBrain:   # This class will be the main intelligence of the program.
    pass


while program_over:
    game = MainMenu.intro()








