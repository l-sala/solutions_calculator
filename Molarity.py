#############################################################################################
#
# 2017-09-24 - Leiden (NL) 
#
# Luca Sala, PhD
#
# This scripts helps to perform some basic lab operations when preparingis one solutions.
#
# Code is simple and it my first attempt with programming and Python :)
#
# Hope it might help some BSc or MSc students preparing solutions
#
# This script works with Python 3.6
#
#############################################################################################

import math

def Mass_in_solution():
	mw = input("Insert the molecular weight of the reagentin in g/mol \n")
	vol = input("Insert the volume in L\n")
	M = input("Insert the molarity in mol/L\n")
	Result = float(mw)*float(M)*float(vol)
	print ("You have to add", float(Result), "grams to your solution")

def Molarity():
	g = input("Insert the grams of reagent\n")
	mw = input("Insert the molecular weight in g/mol\n")
	vol = input("Insert the volume in liters\n")
	Result = float(g)/(float(mw)*float(vol))
	print ("Your compound in solution is", float(Result), "M")

def Volume():
	g = input("Insert the grams of reagent\n")
	mw = input("Insert the molecular weight in g/mol\n")
	M = input("Insert the molarity in mol/L\n")
	Result = float(g)/(mw*M)
	print ("Add"+str(Result)+ "liters to obtain a solution with the desidered molarity")


Action  =  input("Do you want to compute the 'weight' (grams of reagent), the 'molarity' or the 'volume' (liters to create a solution with a known molarity)?\n") 

if Action=="weight":
	Mass_in_solution()
elif Action=="molarity":
	Molarity()
elif Action=="volume":
	Volume()
else:
	print ("ATTENTION!! Insert only 'weight', 'molarity' or 'volume'.")
