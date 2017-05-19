"""
Evan Casey
stoichiograph.py

This program takes a word (or list of words) as input and quickly returns
a list (if such a list exists) of the ways that those words can be made from
the names of the elements in the periodic table.

Runs in O(n) time

OPTIONS:
      p: print list (file input only)
      l: find longest words that can be made
      c: find the word with the most possible combinations
"""

import sys, getopt

elements = ["Ac", "Al", "Am", "Sb", "Ar",
            "As", "At", "Ba", "Bk", "Be",
            "Bi", "Bh", "B", "Br", "Cd",
            "Ca", "Cf", "C", "Ce", "Cs",
            "Cl", "Cr", "Co", "Cu", "Cm",
            "Ds", "Db", "Dy", "Es", "Er",
            "Eu", "Fm", "F", "Fr", "Gd",
            "Ga", "Ge", "Au", "Hf", "Hs",
            "He", "Ho", "H", "In", "I",
            "Ir", "Fe", "Kr", "La", "Lr",
            "Pb", "Li", "Lu", "Mg", "Mn",
            "Mt", "Md", "Hg", "Mo", "Nd",
            "Ne", "Np", "Ni", "Nb", "N",
            "No", "Os", "O", "Pd", "P",
            "Pt", "Pu", "Po", "K", "Pr",
            "Pm", "Pa", "Ra", "Rn", "Re",
            "Rh", "Rg", "Rb", "Ru", "Rf",
            "Sm", "Sc", "Sg", "Se", "Si",
            "Ag", "Na", "Sr", "S", "Ta",
            "Tc", "Te", "Tb", "Tl", "Th",
            "Tm", "Sn", "Ti", "W", "U",
            "V", "Xe", "Yb", "Y", "Zn",
            "Zr"]

elements_lower = []
computed = []
allWords = []

#Main recursive driver function. Creates words, if valid
def computeVars(word, current):
      if word == "" and current not in computed:
            computed.append(current)
      elif word != "":
            if word[0:2] in elements_lower:
                  computeVars(word[2:], current + elements[elements_lower.index(word[0:2])])
            if word[0] in elements_lower:
                  computeVars(word[1:], current + elements[elements_lower.index(word[0])])

#Find word from a list with the most permutations available
def findMostPermutations(words):
      lengths = [len(x) for x in words]
      maxlen = max(lengths)
      word = words[lengths.index(maxlen)]
      print "The word with the most valid combinations is: " + word[0].lower()
      print "With " + str(maxlen) + " combinations\n"

#Find the longest word(s) that can be made from a given list
def findLongestWord(words):
      print "Longest valid word(s) are:"
      maxlen = -1
      for wordl in words:
            for w in wordl:
                  if len(w) > maxlen:
                        maxlen = len(w)
                  break
      for wordl in words:
	    for w in wordl:
		  if len(w) == maxlen:
			print w.lower()
			break

def main(argv):
      variations = []
      for e in elements:
            elements_lower.append(e.lower())
      infileName = ''
      options = ''

      #Get command line arguments
      try:
            opts, args = getopt.getopt(argv, "hi:o:", ["infile=", "options="])
      except getopt.GetoptError:
            print "stoichiograph.py -i <inputfile> -o <options>"
            sys.exit(2)
      for opt, arg in opts:
            if opt == '-h':
                  print "stoichiograph.py -i <inputfile> -o <options>"
                  sys.exit()
            elif opt in ("-i", "--infile"):
                  infileName = arg
            elif opt in ("-o", "--options"):
                  options = arg

      #If command line file is set
      if infileName != "":
            infile = open(infileName, "r")
            for line in infile:
                  computeVars(line[0:-1].lower(), "")
                  if len(computed) > 0:
                        allWords.append(computed[:])
                        computed[:] = []
      
      else:
            word = raw_input("Enter word: ")
            computeVars(word, "")
            if len(computed) > 0:
                  print computed
            else: 
                  print "No valid combinations"

      print
      if 'p' in options.lower():
            for li in allWords:
                  print li
      if 'l' in options.lower():
            findLongestWord(allWords)
            print
      if 'c' in options.lower():
            findMostPermutations(allWords)
            print


if __name__ == "__main__":
      main(sys.argv[1:])
