#!/usr/bin/env python
import sys

line_count     = 0       #count the number of lines
old_key        = "  "    #initialize previous word  to blank string
viewer_count   = 0       #count the number of viewers of the same channel
abc_found      = False   #whether we have found channel ABC or not

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list    
    key        = key_value[0]       #key is first item in list, indexed by 0
    value      = key_value[1]       #value is 2nd item

    line_count = line_count + 1

    if key == old_key or line_count == 1:
        if value == "ABC":
            abc_found = True
        else:
            viewer_count = viewer_count + int(value)

    if key != old_key and line_count:
        if abc_found == True:
            print( '%s %s' % (old_key, viewer_count) )
        old_key      = key  #reset variables
        if value.isdigit():
            viewer_count = int(value)
        abc_found    = False

print( '%s %s' % (key, viewer_count) )
