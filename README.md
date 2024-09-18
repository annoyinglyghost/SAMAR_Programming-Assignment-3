# :notebook: PA3 - Python Data Analysis 
## Problem 1:

Using knowledge obtained from the experiment and demonstrations:
- a. Load the corresponding .csv file into a data frame named cars using pandas
  
🌱 Input: 
```python
import pandas as pd

#Read the csv file into the data fram
file = pd.read_csv('C:/Users/Iszz/Documents/Python Codes/PA3/cars.csv')
#Print file
file
```
🌳 Output: 

![image](https://github.com/annoyinglyghost/Images-2-/blob/main/prob%201.png)

---

- b. Display the first five and last five rows of the resulting cars.

🌱 Input (1.b):
```python
#Displaying the first five rows of the resulting cars
file.head(5)
```
🌳 Ouput (1.b):

![image](https://github.com/annoyinglyghost/Images-2-/blob/main/prob1b.png)

🌱 Input (2.b):
```python
#Displaying the last five rows of the resulting cars
file.tail(5)
```
🌳 Output (2.b):

![image](https://github.com/annoyinglyghost/Images-2-/blob/main/prob2b.png)

> [!NOTE]
> Save your file as Surname_Pandas-P1.py

## Problem 2:

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
indexing operations.

- a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
🌱 Input:
```python
#Showing only the first five rows with odd-numbered columns
file[1::2].head(5)
```
🌳 Ouput:

![image](https://github.com/annoyinglyghost/Images-2-/blob/main/prob2%20a.png)

---

- b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
  
🌱 Input:
```python
#Displaying the row that contains the 'Model' of 'Mazda RX4'
file.loc[file['Model'] == 'Mazda RX4']
```
🌳 Ouput:

![image](https://github.com/annoyinglyghost/Images-2-/blob/main/prob2%20b.png)

---

- c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
  
🌱 Input:
```python
#Filter for finding how many cylinders the 'Camaro Z28' have
camaro = file[file['Model'] == 'Camaro Z28']['cyl'].values[0]

#Printing the result
print(f"The Camaro Z28 has {camaro} cylinders.")
```
🌳 Ouput:

![image](https://github.com/annoyinglyghost/Images-2-/blob/main/prob2%20c.png)

---

- d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
  
🌱 Input:
```python
#List of the car models to be filtered
str = ['Mazda RX4', 'Ford Pantera L', 'Honda Civic']
#Filter the data frame with the specific car models and select only the cyl and gear columns
file[file['Model'].isin(str)][['Model', 'cyl', 'gear']] 
```
🌳 Ouput:

![image](https://github.com/annoyinglyghost/Images-2-/blob/main/prob2%20d.png)

> [!NOTE]
> Save your file as Surname_Pandas-P2.py

## Author
:red_haired_woman: Mariane Iszley V. Samar
- @annoyingltghost—https://github.com/annoyinglyghost
