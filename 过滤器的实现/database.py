import datetime
from pymongo import MongoClient#Connection
from timeseries import Timeseries


########################################
## Database interface
########################################

class DatabaseInterface:
	__instance = None

	def __init__(self):
		if DatabaseInterface.__instance:
			raise DatabaseInterface.__instance

		DatabaseInterface.__instance = self
		self._db = MongoClient().botime#Connection

	def was_domain_seen_in_training(self, domain):
		result = self._db.exposure_domain_timeline.find_one({'domain' : str(domain.get_domain_name())})

		if result == None:
			return False
		else:
			return True

	def get_all_domain_names(self, experiment = False):
		result = list()

		if experiment == False:
			col = self._db.exposure_domain_timeline
		elif experiment == True:
			col = self._db.exposure_domain_timeline_experiment
		else:
			raise Exception('The query is not supported by the database')


		for entry in col.find():
			result.append(entry['domain'])

		return result

	def get_ip_addr_associated_with_domain(self, domain, experiment = False):
		domain_name = str(domain.get_domain_name())

		if experiment == False:
			col = self._db.exposure_domain_ip
		elif experiment == True:
			col = self._db.exposure_domain_ip_experiment
		else:
			raise Exception('The query is not supported by the database')

		results =  col.find({'domain' : domain_name}, {'ip' : 1})

		ips = list()

		for result in results:
			ips.append(result['ip'])
		
		return ips

	def get_timeseries_associated_with_domain(self, domain, experiment = False):
		domain_name = str(domain.get_domain_name())
		timeseries = Timeseries()

		if experiment == False:
			col = self._db.exposure_domain_timeline
		elif experiment == True:
			col = self._db.exposure_domain_timeline_experiment
		else:
			raise Exception('The query is not supported by the database')

		for entry in col.find({'domain' : domain_name}):
			for point in entry['entries']:
				date = point['date'].date()
				count = point['count']
				timeseries.add_value(date, count)

		return timeseries
