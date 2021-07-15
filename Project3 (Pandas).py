import pandas as pd

Employee1 = {'number': [1, 2, 3, 4, 5], 'name': ["abby", "jenny", "marc", "nina", "tom"], 'hourly salary': [3,12,14,15,11]}
table1 = pd.DataFrame(Employee1)
Employee2 = {'number': [1, 2, 3, 4, 5], 'name': ["abby", "joana", "marc", "nina", "tom"], 'hourly salary': [3,15,14,15,11]}
table2 = pd.DataFrame(Employee2)
print(Employee1)
print(table1)
print(table1.head(3))
print(table1.tail(2))

fusion = pd.merge(table1, table2,on='name') #it will merge everything that is common in two tables
print(fusion)

food1={'number':[1, 2,3,4,5],'name':['pizza','apple','fries','chips','burger']}