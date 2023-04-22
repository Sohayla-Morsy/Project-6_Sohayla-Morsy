#!/usr/bin/env python3

"""
Script for removing the duplicates
Created by Sohayla Morsy
Date 22 April 2023
"""

#The parsing of command line arguments/interfaces to remove duplicates
import argparse
parser = argparse.ArgumentParser(
    prog = 'RemoveDuplicates', 
    description = 'It removes duplicates from fasta-file')

#Adding arguments for the input and output files attributes for the programm
parser.add_argument('-i', '--inputfile', required=True)            #The input file Azolla_filiculoides.genome.txt
parser.add_argument('-o', '--outputfile', required=True)           #The output file new.txt
args = parser.parse_args()                                        #"args" variable to return an object with two attributes, integers and accumulate

fasta_in=open(args.inputfile,"r")   #Write new file which will be read only argument and name it "fasta_in"
count_arrow=0                       #Create Variable which has integer zero



#Create loop for each line in fasta_in
for line in fasta_in:
    if line.startswith(">"):              #Whenever the line starts with ">", it means it is a gene ID then add 1 to the count_arrow each time 
        count_arrow=count_arrow+1
    else:                                #Otherwise continue as they would be only sequences 
        continue 
fasta_in.close()                        #Close the file

#Convert count_arrow variable which is integer to  a string
a=str(count_arrow)                     

#Print the counted arrows number ("a" variable as string) to know how many sequences are in the inputfile                         
print("*In the inputfile there are "+a+ " sequences") 

#Creating a dictionary with key: value 
fasta_in=open(args.inputfile,"r")   
dictio={}                                 

#Loop for variable in the range of the counted arrows before
for seq in range(count_arrow):
    identifier=fasta_in.readline().strip()           #Returns one line from the file and removing the end line character
    sequence=fasta_in.readline().upper().strip()     #Same as above command and all sequences are stored in capital letters
    dictio[identifier]=sequence                      #Create dictionary with key: value as identifier: sequence 
    
#Remove duplicates
dictioRemove={}  #contains every sequence only once; identifier:sequence
dictioCount={}   #contains key "identifier" (from dictio):count of how many times duplicated as value

#Loop for variable in dictio while retrieving all of the keys from the dictionary
for identifier in dictio.keys():
    sequence = dictio[identifier]         #Create variable that has the values (Sequences) of the dictio dictionary
    count=0                              #Create Variable which has integer zero
    
#Loop for variable in dictioRemove while retrieving all of the keys from the dictionary
    for identifier2 in dictioRemove.keys():
        if (sequence == dictioRemove[identifier2]):  #Whenever the sequnece from dictio equals to the value (sequences) in dictioRemove dictionary (with the key "identifier2") then add 1 to the count variable
            count=count+1  
            dictioCount[identifier2]=dictioCount[identifier2]+1  #dictioCount with identifier2 keys will be added by 1 each time the above condition applies to be having the number of duplicated sequences (Indication of duplication)
            
 #Whenever the count equals zero then dictioRemove will be same as dictio and dictioCount keys will be only 1 (unduplicated)       
    if count==0:    
        dictioRemove[identifier]=dictio[identifier]
        dictioCount[identifier]=1
       
    
#Storage and adding the number of duplicates to each gene ID header

#Write a new file with the output file (new.txt) used with the argument write
New_protein_sequences=open(args.outputfile, 'w') 

#Loop for variable in dictioRemove while retrieving all of the keys from the dictionary
for headers in dictioRemove.keys():
    
 #Add in the new file the headers variable (unduplicated Keys>> which are gene ID) from dictioRemove and also converting the values (count of duplicated headers) of dictioCount keys "headers" from integer to a string with end line character
    New_protein_sequences.write(headers+"_"+str(dictioCount[headers])+"x \n")
    
    #Add in the file the sequences for each key of dictioRemove with end line character
    New_protein_sequences.write(dictioRemove[headers]+'\n')          
    
#Close the file    
New_protein_sequences.close() 

#Print the summary showing the number of non-duplicated sequences (content of dictioRemove) in the new output file after removing the duplicates from the original inputfile as string
print("*In the outputfile there are "+str(len(dictioRemove))+ " sequences")                                                                                                                                                                                    
        

