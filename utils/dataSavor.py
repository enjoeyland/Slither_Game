import os
import json

from utils.setting import WRITE, APPEND, READ


class DataSavor(object):
	def __init__(self, fileName, filePath = "data/textFiles"):
		self.fileName = fileName
		self.filePath = filePath
		self.file = os.path.join(self.filePath, self.fileName)

		with open(self.file, APPEND, encoding= "utf-8"):
			pass

	def write(self, data):
		with open(self.file, WRITE, encoding= "utf-8") as outfile:
			if type(data) is list:
				for d in data:
					outfile.write(d)
			elif type(data) is str:
				outfile.write(data)

	def append(self, data):
		with open(self.file, APPEND, encoding= "utf-8") as outfile:
			if type(data) is list:
				for d in data:
					outfile.write(d)
			elif type(data) is str:
				outfile.write(data)

	def readSome(self, length):
		result = []
		with open(self.file, READ, encoding= "utf-8") as outfile:
			while length:
				line = outfile.readline()
				if not line: break
				line = line.strip()
				result.append(line)
				length -= 1
		return result

	def readAllAsList(self):
		with open(self.file, READ, encoding= "utf-8") as outfile:
			data = outfile.readlines()
		return data

	def readAllAsString(self):
		with open(self.file, READ, encoding= "utf-8") as outfile:
			data = outfile.read()
		return data

	def jsonReadAll(self):
		result = []
		with open(self.file, READ, encoding= "utf-8") as outfile:
			while True:
				line = outfile.readline()
				if not line: break
				line = line.strip()
				json_obj = json.loads(line)
				result.append(json_obj)
		return  result


	def jsonAppend(self, data):
		"""data should be dict type"""
		jsonObjectData = json.dumps(data)
		self.append(jsonObjectData + "\n")


class ScoreSavor(DataSavor):
	def __init__(self):
		DataSavor.__init__(self, "score.json")

	def saveScore(self, score, **kwargs):
		data = {}
		data["score"] = score
		for key, value in kwargs.items():
			data[key] = value
		self.jsonAppend(data)

	def readScore(self):
		data = self.jsonReadAll()
		return data

	def getTopScore(self, num = 10):
		scores = self.readScore()
		scores.sort(key= self.extractScore, reverse= True)
		return scores[:num]

	def extractScore(self, json):
		try:
			return int(json["score"])
		except KeyError:
			return 0