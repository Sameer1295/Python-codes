import pandas as pd


a = [1,'sam','show']
print(a)
#create a series
myVar = pd.Series(a)
print(myVar)
#create a series with userdefined index
print('----------- series with userdefined index--------')
myVar2 = pd.Series(a,index = ["x","y","z"])
print(myVar2)
#create series using dictonary
print('----------- series using dictionary--------')
dicVar = {'name':'Sameer','age':26,'City':'Mumbai'}
mydicVar = pd.Series(dicVar)
print(mydicVar)

#create series selected key/values object
mydicVar2 = pd.Series(dicVar,index=['name','age'])
print('----------- series with selected keys--------')
print(mydicVar2)