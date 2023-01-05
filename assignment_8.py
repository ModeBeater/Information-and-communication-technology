'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    input3 = sys.argv[3]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""
    input3 = ""


'''
The objective of this assignment is to print the expected output.
You can find it in the instruction folder.
List of installed and authorized packages :
    - numpy
    - scikit-learn (import sklearn)
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
input1 = [int(i) for i in input1.split(',')]
input2 = [int(i) for i in input2.split(',')]
input3 = [int(i) for i in input3.split(',')]
x = np.array(input1)
x = x.reshape((-1,1))
y = np.array(input2)
y = y.reshape((-1,1))
z = np.array(input3)
z = z.reshape((-1,1))
arr = np.hstack((x,y,z))
# print(arr)
scaler = preprocessing.StandardScaler().fit(arr)
data_x = scaler.transform(arr)
train,test = train_test_split(data_x, test_size = 0.25, shuffle = False)
# print(data_x)
#use this printing (where "data_x" is your features scaled and standardized)
print("{}".format(np.round(train,2)))