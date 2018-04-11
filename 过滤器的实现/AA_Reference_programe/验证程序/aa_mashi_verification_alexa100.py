import pandas as pd
import domain
import numpy
from scipy.spatial.distance import mahalanobis
from linguistic_classifier import *


df = pd.read_csv('alexa100.txt',engine='python',header=None)
df.columns = ['domain']
list = []
dict = {}

linguistic_normality = LinguisticNormality()


for do in df['domain']:
    print '**********now initialize*********',do
    do = domain.Domain(do,'False')
    print '*********complated initialize***********'


    print  '-----------set linguisticfeature_set-----------'
    features_set = FeatureSet()
    
    features_set.set_meaningful_word_ratio(MeaningfulWordsExtractor(do).meaningful_words_ratio())
    features_set.set_numerical_characters_ratio(NumericalCharactersExtractor(do).characters_ratio())
    features_set.set_character_set(CharacterSetExtractor(do).set())

    n_gram_normality_extractor = NGramNormalityExtractor(do)

    features_set.set_one_gram_normality_score(n_gram_normality_extractor.normality_score(1))
    features_set.set_two_gram_normality_score(n_gram_normality_extractor.normality_score(2))
    features_set.set_three_gram_normality_score(n_gram_normality_extractor.normality_score(3))
    do.set_linguistic_feature_set(features_set)
    print  '----------------complated linguisticfeature_set---------------'

    print '----------------complate',do,'mahalanobis--------------'
    distance = linguistic_normality.compute_distance(do)
    print  '------------the',do,'mahalanobis is-------------',distance
    list.append(distance)

post_list = sorted(list)
print 'The 90-th distance is ' ,post_list[int(len(post_list)*0.9)] #1.99014368663
print 'The 70-th distance is ' ,post_list[int(len(post_list)*0.7)] #1.35884863088



#dict = {'distance':list}
#a = pd.DataFrame(dict)
#a.to_csv('distance.csv')
#print '------------------complated distance collect -----------------'





    
