
'''
The objective of this assignment is to print the dataframe showed in the instruction.
Only one test will be done.
You can write you code after this comment :
'''
#Your code here:
import pandas as pd
arr1 = ["Brad","Angelina","Tom"]
arr2 = ["Pitt", "Jolie", "Cruise"]
arr3 = [58,47,60]
data = {
    "Name" : arr1,
    "Surname" : arr2,
    "Age" : arr3
}
df = pd.DataFrame(data)
print(df)
