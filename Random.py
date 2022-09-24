# random generator
import random
def random_inp(inp):
    random_input = inp.split()
    #random_input = [element.replace(",", "") for element in random_input]
    #print(random.choice(random_input))
    result = random.choice(random_input).replace(",", "")
    return result