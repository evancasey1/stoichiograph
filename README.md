# Stoichiograph

This program takes a word (or list of words) as input and quickly returns
a list (if such a list exists) of the ways that those words can be made from
the names of the elements in the periodic table.<br>
Runs in O(n) time <br><br>

# Usage
python stoichiograph.py -i \<inputfile> -o \<options> <br><br>

# Options:

p: print list (file input only)<br>
l: find longest words that can be made<br>
c: find the word with the most possible combinations<br><br>

# Recommended Example
python stoichiograph.py -i dictionary2.txt -o plc
