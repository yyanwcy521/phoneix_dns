import pandas as pd
df = pd.read_csv('dga1.txt',sep = r'\t',engine='python',header=None)
df.columns = ['a','b','c','d']

label = ['gameover', 'locky', 'nymaim', 'symmi', 'conficker','pykspa_v2_real', 'pykspa_v2_fake', 'bamital', 'madmax', 'qadars','necurs', 'cryptolocker', 'proslikefan', 'ranbyus', 'murofet','suppobox', 'mirai', 'vidro', 'tofsee', 'dyre', 'chinad', 'virut','emotet', 'matsnu', 'blackhole', 'padcrypt', 'xshellghost','ccleaner', 'fobber_v1', 'dircrypt', 'tinba', 'ramnit', 'banjori','simda', 'fobber_v2', 'tempedreve', 'vawtrak', 'rovnix', 'gspy','pykspa_v1', 'shifu']

dic1 = {}
counter = 0
for i in range(df.shape[0]):
    counter += 1

    if df.ix[i]['a'] in label:
        dic1[df.ix[i]['a']] = df.ix[i]['c']
        label.remove(df.ix[i]['a'])
    else:
        continue
    
    print '--------------------',counter
print dic1
