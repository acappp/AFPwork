str1 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

sec1 = str1[0:63]  #Creates section 1
print("Exon one", sec1)
lsec1 = len(sec1) #Counts the letters in the first section

sec2 = str1[63:91] #Creates section 1
print("Exon two", sec2)
lsec2 = len(sec2) #Counts the letters in the second section

sec3 = str1[91:]

total = len(str1) #Works out the percentage 
perc = ((lsec1 + lsec2) / total*100)
print(perc)