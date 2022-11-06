import csv
import matplotlib.pyplot as plt

def main():
    #filename = input("What is the datafile:" )
    filename = "data1.csv"
    variable1 = "Gender"
    level1 = ["Female", "Male"]
    variable2 = "Habit"
    level2 = ["Smoker","Nonsmoker"]
    
    data = readdata(filename)

    #female smoker
    category11 = calculate(data,variable1,variable2,level1[0],level2[0]) 
    category11_label = level1[0] + " " + level2[0]
    print(category11)
    print(category11_label)

    #female nonsmoker
    category12 = calculate(data,variable1,variable2,level1[0],level2[1]) 
    category12_label = level1[0] + " " + level2[1]
    print(category12)
    print(category12_label)

    #male smoker
    category21 = calculate(data,variable1,variable2,level1[1],level2[0]) 
    category21_label = level1[1] + " " + level2[0]
    print(category21)
    print(category21_label)

    #male nonsmoker
    category22 = calculate(data,variable1,variable2,level1[1],level2[1]) 
    category22_label = level1[1] + " " + level2[1]
    print(category22)
    print(category22_label)

    numbers=get_chisquare(category11,category12,category21,category22)
    draw_graph(numbers,variable1,level1,level2)


def readdata(filename):
    data=[] 
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
           
    return data

def calculate(data,variable1,variable2,level_x,level_y):
    
    category = [
         row[variable1] for row in data if row[variable1]==level_x and row[variable2]==level_y
    ]
    return len(category)

def get_chisquare(category11,category12,category21,category22):
    row_total1 = category11 + category12
    row_total2 = category21 + category22
    column_total1 = category11 + category21
    column_total2 = category21 + category22
    
    total = category11 + category12 + category21 + category22

    expected_category11 = get_expected_frequency(row_total1,column_total1,total)
    expected_category12 = get_expected_frequency(row_total1,column_total2,total)
    expected_category21 = get_expected_frequency(row_total2,column_total1,total)
    expected_category22 = get_expected_frequency(row_total2,column_total2,total)

    single_term11=get_single_term(category11,expected_category11,total)
    single_term12=get_single_term(category12,expected_category12,total)
    single_term21=get_single_term(category21,expected_category21,total)
    single_term22=get_single_term(category22,expected_category22,total)

    results=compare_chisquare(single_term11 , single_term12 , single_term21 , single_term22)
    print(f"Chi Square is {results[0]:.2f}, {results[1]}")
    
    Observedbar1=[category11,category21]
    Observedbar2=[category21,category22]

    Expectedbar1=[expected_category11,expected_category21]
    Expectedbar2=[expected_category21,expected_category22]

    return(Observedbar1,Observedbar2,Expectedbar1,Expectedbar2)

def draw_graph(numbers,variable1,level1,level2):
    Observedbar1=numbers[0]
    Observedbar2=numbers[1]
    Expectedbar1=numbers[2]
    Expectedbar2=numbers[3]
    
    legend=level2 + [f"Expected {level2[0]}",f"Expected {level2[1]}"]
    _, axs = plt.subplots(1, 1)


    # Plot bar chart
    bar_width = 0.4
    Observedposition = [idx - bar_width/2 for idx in range(2)]
    Expectedposition = [idx + bar_width/2 for idx in range(2)]
    axs.bar(Observedposition, Observedbar1, width=bar_width, color='#00BFFF')
    axs.bar(Observedposition, Observedbar2, bottom=Observedbar1, width=bar_width, color='#1E90FF')
    axs.bar(Expectedposition, Expectedbar1, width=bar_width, color='#CDAA7D')
    axs.bar(Expectedposition, Expectedbar2, bottom=Expectedbar1, width=bar_width, color='#8B7355')
    axs.set_title("Visualizing contingency table")
    axs.set_xlabel(variable1)
    axs.set_xticks(range(2))
    axs.set_xticklabels(level1)
    axs.set_ylabel("Count")
    axs.grid(False)
    axs.legend(legend, bbox_to_anchor=(1.0, 1.0))
    plt.tight_layout()

    plt.show()


def get_expected_frequency(row_total,column_total,total):
    return row_total*column_total/total

def get_single_term(observed,expected,total):
    return (observed-expected)*(observed-expected)/total

def compare_chisquare(a,b,c,d):
    chisquare =(a + b + c + d)
    if chisquare >3.84:
        findings = "Significant"
    else:
        findings = "Not significant"
    return (chisquare,findings)
    
if __name__ == "__main__":
    main()