#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

line_cnt    = 0
prev_word   = None
total       = 0
abc_found   = False

for line in sys.stdin:

    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1

    #note: for simple debugging use print statements, ie:  
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item
   
    if value_in.isdigit() :
        value_out   = int(value_in)
        
   # elif value_in == "ABC" :
   #     abc_found = True
    #-----------------------------------------------------
    # Check if its a new word and not the first line 
    #   (b/c for the first line the previous word is not applicable)
    #   if so then print out list of dates and counts
    #----------------------------------------------------
    if curr_word != prev_word and line_cnt>1:

        # -----------------------     
	#now write out the join result, but not for the first line input
        # -----------------------
        if  abc_found:
            print( '%s\t%s' % (prev_word, total) )  #print a string, tab, and string
            total   = value_out
        abc_found = False
	
    elif curr_word == prev_word or line_cnt == 1 :
	if value_in == "ABC" :
	    abc_found = True
        else :
            total   = total + value_out 
           
    prev_word   = curr_word  #set up previous word for the next set of input lines
