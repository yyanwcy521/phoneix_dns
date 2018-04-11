import domain
from linguistic_classifier import DGAClassifier
import pandas as pd


f_ConfickerA = open('ConfickerA.txt','w+')
f_ConfickerB = open('ConfickerB.txt','w+')
f_ConfickerC = open('ConfickerC.txt','w+')
f_Torpig = open('Torpig.txt','w+')
f_Bamital = open('Bamital.txt','w+')

df_ConfickerA = pd.read_csv('data/conficker.a.txt',engine='python',header=None)
df_ConfickerB = pd.read_csv('data/conficker.b.txt',engine='python',header=None)
df_ConfickerC = pd.read_csv('data/conficker.c.txt',engine='python',header=None)
df_Torpig = pd.read_csv('data/torpig.txt',engine='python',header=None)
df_Bamital = pd.read_csv('data/bamital.txt',engine='python',header=None)



df_ConfickerA.columns = ['domains']
df_ConfickerB.columns = ['domains']
df_ConfickerC.columns = ['domains']
df_Torpig.columns = ['domains']
df_Bamital.columns = ['domains']

####################  ConfickerA  ##########################

count1_A = 0
count1_B = 0
list1_A = []
list1_B = []


for i in range(df_ConfickerA.shape[0]):
    str1 = df_ConfickerA.ix[i]['domains']
    do = domain.Domain(str1,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    print '----------------------distance is ',distance
    if distance < 1.99: #1.99
        count1_A += 1
        list1_A.append(str1) # %10 

    f_ConfickerA.write(str1 + " " + str(distance)  + "\n")
	      

for i in list1_A:
    do = domain.Domain(i,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    
    if distance > 1.3588:  #1.3588
        list1_B.append(i)

f_ConfickerA.write('The no_dga is '+str(float(len(list1_A))/float(df_ConfickerA.shape[0])) + "\n")
f_ConfickerA.write('The recall is '+str(float(len(list1_B))/float(len(list1_A))) + "\n")
f_ConfickerA.close()      
print '********************************************the ConfickerA is complated'
####################  ConfickerB  ##########################
  
count1_A = 0
count1_B = 0
list1_A = []
list1_B = []


for i in range(df_ConfickerB.shape[0]):
    str1 = df_ConfickerB.ix[i]['domains']
    do = domain.Domain(str1,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    print '----------------------distance is ',distance
    if distance < 1.99:
        count1_A += 1
        list1_A.append(str1) # %10 

    f_ConfickerB.write(str1 + " " + str(distance)  + "\n")
	      

for i in list1_A:
    do = domain.Domain(i,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    
    if distance > 1.3588:
        list1_B.append(i)

f_ConfickerB.write('The no_dga is '+str(float(len(list1_A))/float(df_ConfickerB.shape[0])) + "\n")
f_ConfickerB.write('The recall is '+str(float(len(list1_B))/float(len(list1_A))) + "\n")
f_ConfickerB.close() 

print '********************************************the ConfickerB is complated'
####################  ConfickerC  ##########################
  
count1_A = 0
count1_B = 0
list1_A = []
list1_B = []


for i in range(df_ConfickerC.shape[0]):
    str1 = df_ConfickerC.ix[i]['domains']
    do = domain.Domain(str1,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    print '----------------------distance is ',distance
    if distance < 1.99:
        count1_A += 1
        list1_A.append(str1) # %10 

    f_ConfickerC.write(str1 + " " + str(distance)  + "\n")
	      

for i in list1_A:
    do = domain.Domain(i,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    
    if distance > 1.3588:
        list1_B.append(i)

f_ConfickerC.write('The no_dga is '+str(float(len(list1_A))/float(df_ConfickerC.shape[0])) + "\n")
f_ConfickerC.write('The recall is '+str(float(len(list1_B))/float(len(list1_A))) + "\n")
f_ConfickerC.close() 

print '********************************************the ConfickerC is complated'
####################  Torpig  ##########################
  
count1_A = 0
count1_B = 0
list1_A = []
list1_B = []


for i in range(df_Torpig.shape[0]):
    str1 = df_Torpig.ix[i]['domains']
    do = domain.Domain(str1,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    print '----------------------distance is ',distance
    if distance < 1.99:
        count1_A += 1
        list1_A.append(str1) # %10 

    f_Torpig.write(str1 + " " + str(distance)  + "\n")
	      

for i in list1_A:
    do = domain.Domain(i,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    
    if distance > 1.3588:
        list1_B.append(i)

f_Torpig.write('The no_dga is '+str(float(len(list1_A))/float(df_Torpig.shape[0])) + "\n")
f_Torpig.write('The recall is '+str(float(len(list1_B))/float(len(list1_A))) + "\n")
f_Torpig.close() 

print '********************************************the Torpig is complated'
####################  Bamital  ##########################
  
count1_A = 0
count1_B = 0
list1_A = []
list1_B = []


for i in range(df_Bamital.shape[0]):
    str1 = df_Bamital.ix[i]['domains']
    do = domain.Domain(str1,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    print '----------------------distance is ',distance
    if distance < 1.99:
        count1_A += 1
        list1_A.append(str1) # %10 

    f_Bamital.write(str1 + " " + str(distance)  + "\n")
	      

for i in list1_A:
    do = domain.Domain(i,'False')
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()
    
    if distance > 1.3588:
        list1_B.append(i)

f_Bamital.write('The no_dga is '+str(float(len(list1_A))/float(df_Bamital.shape[0])) + "\n")
f_Bamital.write('The recall is '+str(float(len(list1_B))/float(len(list1_A))) + "\n")
f_Bamital.close() 
print '********************************************the Bamital is complated'









