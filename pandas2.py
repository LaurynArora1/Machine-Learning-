import pandas as pd

food1 = {'name': ["apple", "pizza", "burger", "mango"], 'color': ["red","yellow","orange","green"]}
food2 = {'size': [3, 10, 15, 11], 'price': [10, 20, 30, 40]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion=table1.join(table2)

print(fusion)