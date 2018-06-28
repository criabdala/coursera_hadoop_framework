#!/usr/bin/env python
import sys


# --------------------------------------------------------------------------
#This mapper code will input a <date word, value> input file, and move date into 
#  the value field for output
#  
#  Note, this program is written in a simple style and does not full advantage of Python 
#     data structures,but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------

#input 1 is like:
# Almos_news,25
# Hourly_show 30
# Hot_Cooking 7
#...

#input 2 is like:
# Almos_news,ABC
# Hourly_show COM
# Hot_Cooking FNT
#...

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key, value  = line.split(",",1)   #split line, into key and value, returns a 2 values

    if (value == "ABC"):    
        #print key_in
	print( '%s\t%s' % (key, value) )  #print a string, tab, and string
    elif (value.isdigit()):
	print( '%s\t%s' % (key, value) )  #print a string, tab, and string 
#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value
