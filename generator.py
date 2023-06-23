import random
from pystyle import *
import colorama
from colorama import Fore, Style, Back


intro = '''

░█████╗░██████╗░███████╗██████╗░██╗████████╗  ░█████╗░░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝██████╔╝█████╗░░██║░░██║██║░░░██║░░░  ██║░░╚═╝███████║██████╔╝██║░░██║
██║░░██╗██╔══██╗██╔══╝░░██║░░██║██║░░░██║░░░  ██║░░██╗██╔══██║██╔══██╗██║░░██║
╚█████╔╝██║░░██║███████╗██████╔╝██║░░░██║░░░  ╚█████╔╝██║░░██║██║░░██║██████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
                                                        by Blackheadn1g4
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                              Press Enter >>>
'''

Anime.Fade(
    Center.Center(intro),
    Colors.green_to_red,
    Colorate.Vertical,
    interval=0.035,
    enter=True,
)


print(f'''


{Fore.LIGHTGREEN_EX}░█████╗░██████╗░███████╗██████╗░██╗████████╗  ░█████╗░░█████╗░██████╗░██████╗░
{Fore.LIGHTGREEN_EX}██╔══██╗██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
{Fore.LIGHTGREEN_EX}██║░░╚═╝██████╔╝█████╗░░██║░░██║██║░░░██║░░░  ██║░░╚═╝███████║██████╔╝██║░░██║
{Fore.LIGHTGREEN_EX}██║░░██╗██╔══██╗██╔══╝░░██║░░██║██║░░░██║░░░  ██║░░██╗██╔══██║██╔══██╗██║░░██║
{Fore.LIGHTGREEN_EX}╚█████╔╝██║░░██║███████╗██████╔╝██║░░░██║░░░  ╚█████╔╝██║░░██║██║░░██║██████╔╝
{Fore.LIGHTGREEN_EX}░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

{Fore.LIGHTGREEN_EX}░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
{Fore.LIGHTGREEN_EX}██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
{Fore.LIGHTGREEN_EX}██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
{Fore.LIGHTGREEN_EX}██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
{Fore.LIGHTGREEN_EX}╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
{Fore.LIGHTGREEN_EX}░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

''')


def generate_credit_card():
    card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))

    expiration_month = random.randint(1, 12)


    current_year = 2023
    expiration_year = random.randint(current_year + 1, current_year + 5)


    cvv = ''.join(str(random.randint(0, 9)) for _ in range(3))

    return card_number, expiration_month, expiration_year, cvv


num_codes = int(input("Enter the number of credit card codes to generate: "))
print("Your Credit Card Codes Are Being Generated")


credit_cards = [generate_credit_card() for _ in range(num_codes)]


for card_number, expiration_month, expiration_year, cvv in credit_cards:
    print("Card Number:", card_number)
    print("Expiration Date: {}/{}".format(expiration_month, expiration_year))
    print("CVV:", cvv)
    print()
