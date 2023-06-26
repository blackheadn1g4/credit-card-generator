import random
from colorama import Fore
from pystyle import *

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

print(f'''{Fore.LIGHTGREEN_EX}
░█████╗░██████╗░███████╗██████╗░██╗████████╗  ░█████╗░░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝██████╔╝█████╗░░██║░░██║██║░░░██║░░░  ██║░░╚═╝███████║██████╔╝██║░░██║
██║░░██╗██╔══██╗██╔══╝░░██║░░██║██║░░░██║░░░  ██║░░██╗██╔══██║██╔══██╗██║░░██║
╚█████╔╝██║░░██║███████╗██████╔╝██║░░░██║░░░  ╚█████╔╝██║░░██║██║░░██║██████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
''')


def generate_credit_card():
    card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
    expiration_month = random.randint(1, 12)
    current_year = 2023
    expiration_year = random.randint(current_year + 1, current_year + 5)
    cvv = ''.join(str(random.randint(0, 9)) for _ in range(3))
    return card_number, expiration_month, expiration_year, cvv


def generate_credit_card_file(file_name1, num_codes1):
    credit_cards = [generate_credit_card() for _ in range(num_codes1)]
    with open(file_name1, 'w') as file:
        for card_number, expiration_month, expiration_year, cvv in credit_cards:
            file.write("Card Number: {}\n".format(card_number))
            file.write("Expiration Date: {}/{}\n".format(expiration_month, expiration_year))
            file.write("CVV: {}\n".format(cvv))
            file.write('\n')


num_codes = int(input("Enter the number of credit card codes to generate: "))
file_name = input("Enter the file Name to save the generated credit card codes: ")
file_name = file_name + ".txt"

print("Generating Credit Card Codes...")
generate_credit_card_file(file_name, num_codes)
print("Credit Card Codes have been generated and saved to", file_name)
