input_file= "./results_novels.txt"
output_file="./results_novelsCleaned.txt"
#--------------------61825 Words
# Using readlines()
dirtyFile = open(input_file, 'r')
Lines = dirtyFile.readlines()
 
lbmCleanerFile = open(output_file, "w")
# Strips the newline character
for line in Lines:
    linesSplitted = line.split(',')
    linesSplittedScdn = linesSplitted[1]
   
    canBePrinted = True
    if "_" not in line and len(linesSplittedScdn)>3 :
        for character in linesSplittedScdn:
            if  character.isdigit():
                canBePrinted = False
                break
        if  canBePrinted:
            line.replace(',',';')
            lbmCleanerFile.write(line)             


