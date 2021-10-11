input_file = "./results_novelsCleaned.txt"
output_file="./freqresults_novelsCleaned.csv"
fileCleaned = open(input_file,"r")


Lines = fileCleaned.readlines()
fileSlashed = open(output_file, "w")
# Strips the newline character
#previousValue = 0
i = 56653
for line in Lines:
    linesSplitted = line.split(',')
    freq = linesSplitted[0]
    fileSlashed.write(freq+';'+str(i)+'\n')
    i=i-1
fileSlashed.close()