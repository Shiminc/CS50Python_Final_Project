# Visualizing 2x2 Contigency Table
#### Video Demo:  https://youtu.be/UHfOp6vwhS0
#### Description:
This program calculates the **chi-square** statistics of the data submitted by users. It also determines if the data supports the hypothesis by telling the users if the statistic is significant at *p*-value<0.05. At its current stage, it only accepts data for **2x2** contingency table, that is 2 *categorical variables* each with 2 *levels. 

It also produces a **stacked bar chart** summarizing the data and showing how it differs from *null-hypothesis.

#### Input:
Users need to provide a csv file in the following format:
- Each row refers to data of one participant
- 1st column should be the index number or participant ID
- 1st row, i.e., header row, should indicate variable names/labels of each column
- 2nd column and 3rd column will be the data for each of the two variables 

###### Example:
````
Participant,Gender,Habit
1,Female,Smoker
2,Female,Smoker
3,Female,Nonsmoker
4,Male,Smoker
5,Male,Nonsmoker
````
#### Output:
The program will print out the frequency in each cell in the 2x2 contigency table, and a chart

###### Example:
```commandline
data {'Male Nonsmoker': 13, 'Male Smoker': 9, 'Female Nonsmoker': 7, 'Female Smoker': 6}
('0.091783', 'Not significant')

```


#### Significant features:
1. The program automatically detects the variables and their levels and calculates the frequencies in each cell.
2. The program not only produces charts summarizing the data, but also supplements it with null-hypothesis visualising to facilitate interpretation. 

#### Future development:
It is hoped to scale up the calculation and visualization of contigency table with dimension higher than 2x2. 