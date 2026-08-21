#!/usr/bin/python3
str1 = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
string = str1[39:66] + chr(32) + str1[107:111] + chr(32) + str1[0:6]
print(string)
