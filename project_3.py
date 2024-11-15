"""
Week 3: Lists and Sets
"""

import sys
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import requests
import secrets

MAIN_MENU_QUESTION = "null"
STATES_LIST = []
STATES_LIST.append ( ['Alabama', 'Montgomery', 4903185, 'Camellia','https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/camellia-flower.jpg?itok=K1xKDUI5'] )
STATES_LIST.append ( ['Alaska', 'Juneau', 731545, 'Forget-Me-Not', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Oak_leaf_hydrangea380.jpg?itok=oKb8UNHC' ] )
STATES_LIST.append ( ['Arizona', 'Phoenix', 7278717, 'Suguaro Catus Blossom','https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/large/public/saguaroflowersFlickr.jpg?itok=QpFj3Opl'] )
STATES_LIST.append ( ['Arkansas', 'Little Rock', 3017825, 'Apple Blossom', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/large/public/primary-images/AppletreeblossomArkansasflower.JPG?itok=Z-Q3rp1D'] )
STATES_LIST.append ( ['California', 'Sacremento ', 39512223, 'Golden Poppy', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/large/public/primary-images/CAflowerCaliforniaPoppy.jpg?itok=Q5Q8X3LE'] )
STATES_LIST.append ( ['Colorado', 'Denver', 5758736, 'Mountain Columbine', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Colorado_columbine2.jpg?itok=3bfYnk5Y'] )
STATES_LIST.append ( ['Connecticut', 'Hatford', 3565287, 'Mountain Laurel', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Mountain-Laural-flowers2.jpg?itok=b7tlfk4G'] )
STATES_LIST.append ( ['Delaware', 'Dover', 973764, 'Peach Blossom', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/peachblossomspeachflowers.jpg?itok=Lx-fzlgl'] )
STATES_LIST.append ( ['Florida', 'Tallahassee', 21477737, 'Orange Blossom', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/OrangeBlossomsFloridaFlower.jpg?itok=SK-Tp-rH'] )
STATES_LIST.append ( ['Georgia', 'Atlanta', 10617423, 'Cherokee Rose', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CherokeeRoseFlower.jpg?itok=TKWxpzcw'] )
STATES_LIST.append ( ['Hawaii', 'Honolulu', 415872, 'Red Hibiscus', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/yellowhibiscusPuaAloalo.jpg?itok=Y2aYqLKY'] )
STATES_LIST.append ( ['Idaho', 'Boise', 1787065, 'Syringa', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/syringaPhiladelphuslewisiiflower.jpg?itok=BKOaOXs0'] )
STATES_LIST.append ( ['Illinois', 'Springfield', 12671821, 'Violet', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/singlebluevioletflower.jpg?itok=8i1uQHwg'] )
STATES_LIST.append ( ['Indiana', 'Indianaplois', 6732219, 'Peony', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/PeonyPaeoniaflowers.jpg?itok=IrFIQ9ZF'] )
STATES_LIST.append ( ['Iowa', 'Des Moines', 3155070, 'Wild Rose', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/WildPrairieRose.jpg?itok=zyo0qIMG'] )
STATES_LIST.append ( ['Kansas', 'Topeka', 2913314, 'Sunflower', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/native-sunflowers.jpg?itok=PB8Qq-IC'] )
STATES_LIST.append ( ['Kentucky', 'Frankfort', 4467673, 'Goldenrod', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/stateflowergoldenrod-bloom.jpg?itok=CCLZ4eiV'] )
STATES_LIST.append ( ['Louisiana', 'Baton Rouge', 4648794, 'Magnolia', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/LouisianaIrisWildflower-0.jpg?itok=lOKBHACo'] )
STATES_LIST.append ( ['Maine', 'Augusta', 1344212, 'Pine Cone &amp; Tassel','https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/whitepinemalecones.jpg?itok=cscy757F'] )
STATES_LIST.append ( ['Tennessee', 'Nashville', 6833174, 'Iris', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/passionflowerwildflower2.jpg?itok=c5CmwPJt'] )
STATES_LIST.append ( ['Maryland', 'Annapolis', 6045680, 'Black-eyed Susan', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/FlowerMDBlack-eyedSusan.jpg?itok=I8jYSvFl'] )
STATES_LIST.append ( ['Deleware', 'Dover', 973764, 'Peach Blossom', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/peachblossomspeachflowers.jpg?itok=Lx-fzlgl'] )
STATES_LIST.append ( ['Massachusettes', 'Boston', 6949503, 'Mayflower', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/MayflowerTrailingArbutus.jpg?itok=uIQd8O6F'] )
STATES_LIST.append ( ['Rhode Island', 'Providence', 1059361, 'Violet', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/violetsflowers.jpg?itok=KNMrrLfu'] )
STATES_LIST.append ( ['Minniesota', 'St.Paul', 5639632, 'Lady-Slipper', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/pinkwhiteladysslipperflower1.jpg?itok=LGYZFl26'] )
STATES_LIST.append ( ['Mississippi', 'Jackson', 2976149, 'Magnolia', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CoreopsisWildflower1-01.jpg?itok=HPK2l6yQ'] )
STATES_LIST.append ( ['Missouri', 'Jefferson City', 6137428, 'Hawthorne', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/hawthornflowersblossoms1.jpg?itok=LOrlsJ3L'] )
STATES_LIST.append ( ['Michigan', 'Lansing', 9986857, 'Apple Blossom', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/appleblossombeauty.jpg?itok=HxWn6VHl'] )
STATES_LIST.append ( ['Montana', 'Helena', 1068778, 'Bitterroot', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/bitterrootfloweremblem.jpg?itok=SnCwy78x'] )
STATES_LIST.append ( ['Nebraska', 'Lincoln', 1934408, 'Goldenrod', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/goldenrodflowersyellow4.jpg?itok=6X5qpm4c'] )
STATES_LIST.append ( ['Nevada', 'Carson City', 3080156, 'Sagebrush', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Nevada-Sagebrush-Artemisia-tridentata.jpg?itok=ij6RMnom'] )
STATES_LIST.append ( ['New Hampshire', 'Concord', 1359711, 'Purple Lilac', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/NH-pinkLadysSlipperFlower.jpg?itok=tppHBWs8'] )
STATES_LIST.append ( ['Vermont', 'Montpelier', 623989, 'Red Clover', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redcloverstateflowerWV.jpg?itok=wvnkPA4C'] )
STATES_LIST.append ( ['New Jersey', 'Trenton', 8882190, 'Violet', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/wood-violet.jpg?itok=IJ0ft_8r'] )
STATES_LIST.append ( ['New Mexico', 'Santa Fe', 2096829, 'Yucca', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/YuccaFlowersclose.jpg?itok=jCUN8toc'] )
STATES_LIST.append ( ['New York', 'Albany', 19453561, 'Rose', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redrosebeautystateflowerNY.jpg?itok=LDcB_Vc_'] )
STATES_LIST.append ( ['North Carolina', 'Raleigh', 10488084, 'Flowering Dogwood', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/floweringdogwoodflowers2.jpg?itok=p_1PGcNk'] )
STATES_LIST.append ( ['Wyoming', 'Cheyenne', 78759, 'Indian Paintbrush', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/indianpaintbrushWYflower.jpg?itok=ClQHPA55'] )
STATES_LIST.append ( ['North Dakota', 'Bismark', 762062, 'Prairie Rose', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/flowerwildprairierose.jpg?itok=j5Retaxz'] )
STATES_LIST.append ( ['Ohio', 'Columbus', 11689100, 'Scalet Carnation', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redcarnationOhioflower.jpg?itok=oCdw9u6V'] )
STATES_LIST.append ( ['Oklahoma', 'Oklahoma City', 3956971, 'Mistletoe', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Indian-blanket-Gaillardia-pulchella.jpg?itok=_7eai2t7'] )
STATES_LIST.append ( ['Oregon', 'Salem', 4217737, 'Oregon Grape', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Oregongrapeflowers2.jpg?itok=lVSJoqCE'] )
STATES_LIST.append ( ['Pennsylvania', 'Harrisburg', 12801989, 'Mountain Laurel', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Mt_Laurel_Kalmia_Latifolia.jpg?itok=8VhW2Sms'] )
STATES_LIST.append ( ['South Carolina', 'Columbia', 5148714, 'Yellow Jessamine','https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CarolinaYellowJessamine101.jpg?itok=1tgcX6mj'] )
STATES_LIST.append ( ['South Dakota', 'Pierre', 88465, 'Pasque flower', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Pasqueflower-03.jpg?itok=vMlGt_qW'] )
STATES_LIST.append ( ['Texas', 'Austin', 28995881, 'Bluebonnet', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Texas-dawn-waterlily-Nymphaea.jpg?itok=RuViBaR-'] )
STATES_LIST.append ( ['Utah', 'Salt Lake City', 3202985, 'Sego Lily', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/SegoLily.jpg?itok=Hxt3DOTq'] )
STATES_LIST.append ( ['Virginia', 'Richmond', 8535519, 'Dogwood', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/floweringDogwoodSpring.jpg?itok=DFuNFYgS'] )
STATES_LIST.append ( ['Washington', 'Olympia', 7614893, 'Coast Rhododendron', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/flower_rhododendronWeb.jpg?itok=0Xl911Zf'] )
STATES_LIST.append ( ['West Virginia', 'Charleston', 1792147, 'Rhododendron', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/rhododendronWVstateflower.jpg?itok=7lJaeqWT'] )
STATES_LIST.append ( ['Wisconsin', 'Madison', 5822434, 'Wood Violet', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/wood-violet.jpg?itok=IJ0ft_8r'] )

def validator(x_x):
    """Prompts user to validate their input"""
    valid_input = False
    while valid_input is not True:
        print("Is the following input correct:" , x_x , "\tYes or No?")
        validator_correctness = upper_input()
        if validator_correctness == "YES":
            print("Thank you for confirming")
            return True
        if validator_correctness == "NO":
            print("Understood, reprompting...")
            return False
        if validator_correctness == "QUIT":
            print("Are you sure you'd like to Quit?")
            quit_check = upper_input()
            if quit_check == "YES":
                print("Goodbye")
                sys.exit()
            elif quit_check == "NO":
                print("Returning Back")
                break
            else:
                print("Please Enter 'Yes' or 'No'")
        if not validator_correctness.isalpha:
            print("Please Enter 'Yes' or 'No'")

def upper_input():
    """Converts input to uppercase"""
    x_x = input()
    return x_x.upper().strip()

def get_state_index(state):
    """Gets the Index of A State"""
    for index, item in enumerate(STATES_LIST):
        if item[0].upper() == state.upper().strip():
            return index
    return None

def continue_check():
    """Checking if the user wishes to continue"""
    menu_question = "null"
    valid_input = False
    while valid_input is not True:
        print("Would you like to continue?")
        menu_question = upper_input()
        if menu_question == "QUIT":
            sys.exit()
        if menu_question == "NO":
            print("Returning to main menu")
            break
        if validator(menu_question):
            valid_input = True
        else:
            print(
                "Invalid Input: Please enter 'Yes' , 'No' , or 'Quit'")
    return valid_input

def all_states():
    """Display, sort and update, as needed a List of U.S states containing the state capital, overall state population, and state flower"""
    print("This Application will Display the State Capital, Overall State Population, and State Flower for All States")
    if continue_check():
        for x_x in range(len(STATES_LIST)):
            print("For" , STATES_LIST[x_x][0], "... The State Capitol is" , STATES_LIST[x_x][1] , "... The State Population is" , STATES_LIST[x_x][2] , "... And the State Flower is the" , STATES_LIST[x_x][3])

def specific_states():
    """Search for a specific state and display the appropriate Capital name,
    State Population, and an image of the associated State Flower"""
    print("This will Display the State Capital, Overall State Population, and State Flower")
    menu_question = "null"
    if continue_check():
        valid_input = False
        while valid_input is not True:
            print("Enter a Specific State to View Information or 'Quit'")
            menu_question = upper_input()
            validator(menu_question)
            if menu_question == "QUIT":
                break
            index = get_state_index(menu_question)
            response = requests.get(STATES_LIST[index][4])
            img = Image.open(BytesIO(response.content))
            if index is not None:
                print("You have selected:" , STATES_LIST[index][0] , "Their Capitol is:" ,
                STATES_LIST[index][1] , "... The State Population is" ,
                STATES_LIST[index][2] , "... And the State Flower is")
                img.show()
            else:
                print(menu_question , "is not a US State")

def graph_states():
    """Provide a Bar graph of the top 5 populated States showing their overall population"""
    print("This Application will Provide a Bar Graph for the Top 5 Populated States")
    if continue_check():
        sorted_states_by_pop = sorted(STATES_LIST, key= lambda x : x[2], reverse=True)
        names = [sorted_states_by_pop[0][0], sorted_states_by_pop[1][0], sorted_states_by_pop[2][0], sorted_states_by_pop[3][0], sorted_states_by_pop[4][0]]
        populations = [sorted_states_by_pop[0][2], sorted_states_by_pop[1][2], sorted_states_by_pop[2][2], sorted_states_by_pop[3][2], sorted_states_by_pop[4][2]]
        fig = plt.figure(figsize = (10, 5))
        plt.bar(names, populations, color='blue', width = 0.4)
        plt.xlabel("State")
        plt.ylabel("Population")
        plt.title("Sorted State Populations")
        plt.show()

def update_states():
    """Update the overall state population for a specific state"""
    print("This Application will Update the Overall State Population for a Specific State")
    menu_question = "null"
    if continue_check():
        valid_input = False
        while valid_input is not True:
            print("Enter a Specific State to Modify or 'Quit'")
            menu_question = upper_input()
            validator(menu_question)
            if menu_question == "QUIT":
                break
            index = get_state_index(menu_question)
            if index is not None:
                print("You have selected:" , STATES_LIST[index][0] , "Their current population is:" , STATES_LIST[index][2])
                print("Please Set a new population for:" , STATES_LIST[index][0])
                menu_question = upper_input()
                if menu_question.isnumeric:
                    STATES_LIST[index][2] = int(menu_question)
                else:
                    print("Please Enter a Valid Number")
                print("The new Population for:" , STATES_LIST[index][0] , "is:" , STATES_LIST[index][2])
            else:
                print(menu_question , "is not a US State")

print("******************************")
print("Welcome to the State Facts application!")

while MAIN_MENU_QUESTION != "QUIT":
    print("Please select the specific application you'd like to utilize OR Quit: ")
    print("1. Display All U.S. States Information")
    print("2. Display Specific U.S. State Information")
    print("3. Display Bar Graph of Top States' Population")
    print("4. Update State's Population")
    MAIN_MENU_QUESTION = upper_input()
    if MAIN_MENU_QUESTION in ('1', 'ALL'):
        validator(MAIN_MENU_QUESTION)
        all_states()
    elif MAIN_MENU_QUESTION in ('2', 'SPECIFIC'):
        validator(MAIN_MENU_QUESTION)
        specific_states()
    elif MAIN_MENU_QUESTION in ('3', 'GRAPH'):
        validator(MAIN_MENU_QUESTION)
        graph_states()
    elif MAIN_MENU_QUESTION in ('4', 'UPDATE'):
        validator(MAIN_MENU_QUESTION)
        update_states()
    elif MAIN_MENU_QUESTION == "QUIT":
        validator(MAIN_MENU_QUESTION)
        print("Thank you for utilizing the State Facts application!")
        sys.exit()
    else:
        print("***Invalid Input***")
        print("Please Enter 'All', 'Specific', 'Graph', 'Update', or 'Quit'\t")
