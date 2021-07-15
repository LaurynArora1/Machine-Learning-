# converting a csv file to an html file using pandas
import pandas as pd
fruit = pd.read_csv('D:\\ML\\Book1.csv')
fruit.to_html("FRUIT")