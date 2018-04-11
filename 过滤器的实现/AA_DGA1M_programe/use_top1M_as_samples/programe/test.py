import pandas as pd


f=open("dga1.txt","r")
dic1 = {}
dic = {}

for line in f:
    str1 = line.split('\t')[0]
    str2 = line.split('\t')[1]

    str3 = str2.partition('.')[0]
    str4 = str2.partition('.')[-1]
    
    
    int1=0
    for x in str3:
        if x.isalpha():
            int1=int1+1
            
    int2=0
    for x in str3:
        if x.isdigit():
            int2=int2+1
            
    rate = float(int2)/float(len(str3))
    
    if str1 in dic1:
        dic1[str1].append(rate)
    else:
        dic1[str1] = []
        dic1[str1].append(rate)


with open ("dga1.txt","r") as f:
for line in f:
    str1 = line.split('\t')[0]
    str2 = line.split('\t')[1]

    str3 = str2.partition('.')[0]
    str4 = str2.partition('.')[-1]
        
    
    
    if  dic.has_key(str1):
        dic[str1]['count'] +=1
        dic[str1]['suff_type'].add(str4)
        dic[str1]['interval'].add(len(str3))
        
    else:
        dic[str1]={}
        
        dic[str1]['count'] = 1
        
        dic[str1]['suff_type']=set()
        dic[str1]['suff_type'].add(str4)
        
        dic[str1]['interval']=set()
        dic[str1]['interval'].add(len(str3))
    
        dic[str1]['num_ratio'] = set()
        dic[str1]['num_ratio'].add(min(tuple(dic1[str1])))
        dic[str1]['num_ratio'].add(max(tuple(dic1[str1])))
print dic

df = pd.DataFrame(dic)
df.to_csv('aaaaaaa.csv')







