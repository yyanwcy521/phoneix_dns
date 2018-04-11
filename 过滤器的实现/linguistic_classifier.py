from linguistic_features_extractors import MeaningfulWordsExtractor
from linguistic_features_extractors import NumericalCharactersExtractor
from linguistic_features_extractors import CharacterSetExtractor
from linguistic_features_extractors import NGramNormalityExtractor
from cluster import DomainClusterFileFactory
from scipy.spatial.distance import mahalanobis
import scipy
import numpy


########################################
## Feature set
########################################

class FeatureSet:
	def __init__(self):
		self._meaningful_word_ratio = None
		self._numerical_characters_ratio = None
		self._character_set = None
		self._one_gram_normality_score = None
		self._two_gram_normality_score = None
		self._three_gram_normality_score = None
		self._DGA_label = None

	def export_header(self):
		return 'meaningful_word_ratio, numerical_characters_ratio, one_gram_normality_score, two_gram_normality_score, three_gram_normality_score, DGA_label'

	def __str__(self):
		string = ''
		string += str(self.get_meaningful_word_ratio())
		string += ', '
		string += str(self.get_one_gram_normality_score())
		string += ', '
		string += str(self.get_two_gram_normality_score())
		string += ', '
		string += str(self.get_three_gram_normality_score())
		string += ', '
		string += str(self.get_DGA_label())

		return string

	def set_meaningful_word_ratio(self, feature):
		self._meaningful_word_ratio = feature

	def get_meaningful_word_ratio(self):
		if self._meaningful_word_ratio == None:
			raise Exception('The feature meaningful_word_ratio was not set.')

		return self._meaningful_word_ratio

	def set_numerical_characters_ratio(self, feature):
		self._numerical_characters_ratio = feature

	def get_numerical_characters_ratio(self):
		if (self._numerical_characters_ratio == None):
			raise Exception('The feature numerical_characters_ratio was not set.')

		return self._numerical_characters_ratio

	def set_character_set(self, feature):
		self._character_set = feature

	def get_character_set(self):
		if (self._character_set == None):
			raise Exception('The feature character_set was not set.')

		return self._character_set

	def set_one_gram_normality_score(self, feature):
		self._one_gram_normality_score = feature

	def get_one_gram_normality_score(self):
		if self._one_gram_normality_score == None:
			raise Exception('The feature one_gram_normality_score was not set.')

		return self._one_gram_normality_score

	def set_two_gram_normality_score(self, feature):
		self._two_gram_normality_score = feature

	def get_two_gram_normality_score(self):
		if self._two_gram_normality_score == None:
			raise Exception('The feature two_gram_normality_score was not set.')

		return self._two_gram_normality_score

	def set_three_gram_normality_score(self, feature):
		self._three_gram_normality_score = feature

	def get_three_gram_normality_score(self):
		if self._three_gram_normality_score == None:
			raise Exception('The feature three_gram_normality_score was not set.')

		return self._three_gram_normality_score

	def set_DGA_label(self, label):
		self._DGA_label = label

	def get_DGA_label(self):
		if self._DGA_label == None:
			return 'unknown'

		return self._DGA_label;

        def set_mahalanobis(self,distance):
                self._mahalanobis_distance = distance

        def get_mahalanobis(self):
                if self._mahalanobis_distance == None:
			raise Exception('The mahalanobis_distance was not set.')
         
                return self._mahalanobis_distance


########################################
## Features extractor
########################################

class FeaturesExtractor:
	def __init__(self, domain):
		self._domain = domain

	def compute_feature_set(self, dictionary=None):
		features_set = FeatureSet()

		features_set.set_meaningful_word_ratio(MeaningfulWordsExtractor(self._domain).meaningful_words_ratio())
		features_set.set_numerical_characters_ratio(NumericalCharactersExtractor(self._domain).characters_ratio())
		features_set.set_character_set(CharacterSetExtractor(self._domain).set())

		n_gram_normality_extractor = NGramNormalityExtractor(self._domain)

		features_set.set_one_gram_normality_score(n_gram_normality_extractor.normality_score(1))
		features_set.set_two_gram_normality_score(n_gram_normality_extractor.normality_score(2))
		features_set.set_three_gram_normality_score(n_gram_normality_extractor.normality_score(3))

		return features_set


########################################
## Classifier
########################################

class DGAClassifier:
	def __init__(self, domain):
		self._domain = domain

	def classify(self, strict = True):
		features_extractor = FeaturesExtractor(self._domain)
		feature_set = features_extractor.compute_feature_set()

		meaningful_words_ratio = feature_set.get_meaningful_word_ratio()  #0-1
		one_gram_normality_score = feature_set.get_one_gram_normality_score() #>>1
		two_gram_normality_score = feature_set.get_two_gram_normality_score() #>>1
		three_gram_normality_score = feature_set.get_three_gram_normality_score() #>>1

		self._domain.set_linguistic_feature_set(feature_set) ###

		try:
			linguistic_normality = LinguisticNormality()
		except LinguisticNormality as linguistic_normality_instance:
			linguistic_normality = linguistic_normality_instance

                distance = linguistic_normality.compute_distance(self._domain)

		if distance < linguistic_normality.get_threshold(strict):

			label = 'non-DGA'
		else:
			label = 'DGA'

		feature_set.set_DGA_label(label)


                
                return distance

        


########################################
## Linguistic normality
########################################

class LinguisticNormality:
	__instance = None

	def __init__(self):
		if LinguisticNormality.__instance:
			raise LinguisticNormality.__instance

		LinguisticNormality.__instance = self
#alexa100.txt
		cluster_factory = DomainClusterFileFactory('alexa100.txt', False)
		normal_cluster = cluster_factory.get('cluster_0')

		meaningful_word_ratio_list = list()
		one_gram_normality_score_list = list()
		two_gram_normality_score_list = list()
		three_gram_normality_score_list = list()

		for domain in normal_cluster:
			features_extractor = FeaturesExtractor(domain)
			feature_set = features_extractor.compute_feature_set()

			meaningful_word_ratio_list.append(feature_set.get_meaningful_word_ratio())
			one_gram_normality_score_list.append(feature_set.get_one_gram_normality_score())
			two_gram_normality_score_list.append(feature_set.get_two_gram_normality_score())
			three_gram_normality_score_list.append(feature_set.get_three_gram_normality_score())
                        
		samples = numpy.array([meaningful_word_ratio_list, one_gram_normality_score_list, two_gram_normality_score_list, three_gram_normality_score_list])
                print samples
		cov_matrix = numpy.cov(samples)#4*4
                print cov_matrix
		self._cov_inv = numpy.linalg.inv(cov_matrix) #4*4
                print self._cov_inv
		self._centroid = numpy.array([numpy.average(meaningful_word_ratio_list), numpy.average(one_gram_normality_score_list), numpy.average(two_gram_normality_score_list), numpy.average(three_gram_normality_score_list)])
                print self._centroid#1*4

	def compute_distance(self, domain):
		meaningful_word_ratio = domain.get_linguistic_feature_set().get_meaningful_word_ratio()
		one_gram_normality_score = domain.get_linguistic_feature_set().get_one_gram_normality_score()
		two_gram_normality_score = domain.get_linguistic_feature_set().get_two_gram_normality_score()
		three_gram_normality_score = domain.get_linguistic_feature_set().get_three_gram_normality_score()

		current_sample = numpy.array([meaningful_word_ratio, one_gram_normality_score, two_gram_normality_score, three_gram_normality_score])

		for i in range(len(current_sample)):
			if self._centroid[i] < current_sample[i]:
				current_sample[i] = self._centroid[i] ###if current_sample[i]  is bigger than centroid[i],then it must be no_dga.

		distance = mahalanobis(current_sample, self._centroid, self._cov_inv)

		return distance

	def get_threshold(self, strict = True):
		if strict:
			return 1.99  #997380   0.9 is 1.99751292059257    0.7 is 1.3126509550449008
		else:                  #10W alexa: 0.9 is 1.99014368663 0.7 is 1.35884863088
			return 1.3588


