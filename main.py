from src.Init.init import choice 
from src.Init.init import initialisation 
import os

def main():
    user_choice = choice()
    initialisation(user_choice)


if __name__ == '__main__':
    main()