import csv
import sys
import re
import matplotlib.pyplot as plt

class CustomError(Exception):
    pass

def main():

    filename = input("What is the datafile: " )

    #filename = "data1.csv"
    data = readdata(filename)
    try:
        variables = get_variables(data)
    except CustomError as exception:
        sys.exit("There are more/fewer than 2 variables in the data files")

    try:
        levels = get_levels(data,variables)
    except CustomError as exception:
        sys.exit("There are more/fewer than 2 levels in one of the variables")
    #print(variables)
    #print(levels)


    observed_frequencies = calculate_frequencies(data,variables,levels)
    print("data", observed_frequencies)

    margin_total=calculate_margin(observed_frequencies,levels)
    #print('margin_total',margin_total)
    expected_frequencies = calculate_expected(observed_frequencies,margin_total)
    #print("expected",expected_frequencies)

    results = calculate_chisquare(observed_frequencies,expected_frequencies)
    print(results)

    observedbar1 = extract(observed_frequencies,variables[1],levels,0)
    #print(observedbar1)
    observedbar2 = extract(observed_frequencies, variables[1], levels, 1)
    expectedbar1 = extract(expected_frequencies, variables[1], levels, 0)
    expectedbar2 = extract(expected_frequencies, variables[1], levels, 1)
    try:
        draw_graph(observedbar1,observedbar2,expectedbar1,expectedbar2,variables,levels)
    except ValueError:
        sys.exit("graph could not be drawn due to value error")
        
def extract(numbers: dict, variable: str, levels: dict , n:int):
    bar = []
    level = levels[variable]
    for key in numbers:
        my_regex = (r'\b' + re.escape(level[n]) + r'\b')
        if re.search(my_regex, key):
            bar.append(float(numbers[key]))
    return bar

def calculate_frequencies(data:dict,variables: list,levels: dict):
    observed = {}
    for lvl1 in levels[f"{variables[0]}"]:
        for lvl2 in levels[f"{variables[1]}"]:
            key = (f"{lvl1} {lvl2}")
            observed[key]=calculate(data,variables,lvl1,lvl2)
    return(observed)

def calculate_margin(observed: dict, levels:dict):
    
    margin= {}

    for variable_key in levels:
        for level in levels[variable_key]:
            margin_total=[]
            for key in observed:
                my_regex = (r'\b' + re.escape(level) + r'\b')
                if re.search(my_regex, key):
                    margin_total.append(observed[key])
            margin[f"{level}"]=sum_list(margin_total)        
            #print(margin_total)
    return(margin)
        
def calculate_expected(observed,margin):
    expected = {}
    expected = observed.copy()
    grand_total = sum_list(observed.values())
    #print(grand_total)
    #print(expected)

    for key in expected:
        expected_denominator = []
        for margin_key in margin:
            my_regex = (r'\b' + re.escape(margin_key) + r'\b')
            if re.search(my_regex, key):
                expected_denominator.append(margin[margin_key])
        expected[key] = multiply_list(expected_denominator)/grand_total
    
    return(expected)

def calculate_chisquare(observed: dict,expected:dict):
    denominator=0
    chisquare=0

    for key in observed:
        chisquare += ((float(observed[key])-float(expected[key]))**2)/float(expected[key])

    if chisquare >3.84:
        findings = "Significant"
    else:
        findings = "Not significant"

    return f"{chisquare:.5}", findings
def sum_list(values: list):
    n=0
    for x in values:
        n += int(x)
    return n

def multiply_list(values:list):
    n=1
    for x in values:
        n *= int(x)
    return n 

def calculate(data,variables,level_x,level_y):
    
    category = [
         row[variables[0]] for row in data if row[variables[0]]==level_x and row[variables[1]]==level_y
    ]
    return len(category)


def get_variables(data):

    variables = []
    for variable in data[1].keys():
        variables.append(variable)
    
    if len(variables[1:])!=2:
        raise CustomError
    else:
        return variables[1:]

def get_levels(data,variables):
    levels = {}
    for variable in variables:
        level = set(
            row[variable] for row in data 
        )
        level = list(level)    
        if len(level)!=2:
            raise CustomError
        else:
            levels[f"{variable}"]=level
    return levels

def readdata(filename):
    data=[]
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
    return data


def draw_graph(Observedbar1,Observedbar2,Expectedbar1,Expectedbar2,variables,levels):
    _, axs = plt.subplots(1, 1)

    bar_width = 0.4
    Observedposition = [idx - bar_width / 2 for idx in range(2)]
    Expectedposition = [idx + bar_width / 2 for idx in range(2)]

    axs.bar(Observedposition, Observedbar1, width=bar_width, color='#00BFFF')
    axs.bar(Observedposition, Observedbar2, bottom=Observedbar1, width=bar_width, color='#1E90FF')
    axs.bar(Expectedposition, Expectedbar1, width=bar_width, color='#CDAA7D')
    axs.bar(Expectedposition, Expectedbar2, bottom=Expectedbar1, width=bar_width, color='#8B7355')
    axs.set_title("Visualizing contingency table")
    axs.set_xlabel(variables[0])
    axs.set_xticks(range(2))
    axs.set_xticklabels(levels[variables[0]])
    axs.set_ylabel("Count")
    axs.grid(False)
    legend = levels[variables[1]] + [f"Expected {levels[variables[1]][0]}", f"Expected {levels[variables[1]][1]}"]
    axs.legend(legend, bbox_to_anchor=(1.0, 1.0))
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()
