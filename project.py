import random
import pdfkit
import csv
import sys
from tabulate import tabulate



def main():
    try:
        chosen_recipe = ask_for_input()
        print("Loading please wait...")
        match chosen_recipe:
            case 1:
                gen_rand_african_dish()
            case 2:
                gen_rand_european_dish()
            case 3:
                gen_rand_latin_dish()
            case 4:
                gen_rand_asian_dish()
            case _:
                sys.exit("That is not an available option!")
        print("Done! Please check the \"generated_recipe\" pdf for your recipe!\nEnjoy! 😄")
    except ValueError:
        sys.exit("Please make sure to provide a numerical input only!")



def ask_for_input():
    options = [
                ["Nationality", "Number"],
                ["African", 1],
                ["European", 2],
                ["Latin", 3],
                ["Asian",4]
    ]
    table = tabulate(options, headers="firstrow", tablefmt="fancy_grid")
    return int(input(f"What type of recipe would you like?\n {table}\n"))


def gen_pdf(s):
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    pdfkit.from_url(s, 'generated_recipe.pdf', configuration=config)

def read_csv(c):
    list = []
    with open(c, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for recipe in reader:
            list.append(recipe)
    return list

def gen_rand_african_dish():
    african = read_csv("african.csv")
    randint: int = random.randint(0, len(african))
    recipe: str = african[randint]
    return gen_pdf(recipe)

def gen_rand_european_dish():
    european = read_csv("european.csv")
    randint: int = random.randint(0, len(european))
    recipe: str = european[randint]
    return gen_pdf(recipe)

def gen_rand_latin_dish():
    latin = read_csv("latin.csv")
    randint: int = random.randint(0, len(latin))
    recipe: str = latin[randint]
    return gen_pdf(recipe)

def gen_rand_asian_dish():
    asian = read_csv("asian.csv")
    randint: int = random.randint(0, len(asian))
    recipe: str = asian[randint]
    return gen_pdf(recipe)



if __name__ == "__main__":
    main()


