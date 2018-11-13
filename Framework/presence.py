__author__ = 'root'
import os

if os.path.isfile('test.txt'):
    print "test.txt file is there"
else:
    print "it doesnt exist"