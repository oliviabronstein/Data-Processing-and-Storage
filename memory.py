class Memory:
	def __init__(self):
		self.dictionary = {}
		self.in_progress_dictionary = {}
		self.in_progress = False

	def begin_transaction(self):
		if not self.in_progress:
			self.in_progress = True
		else:
			raise Exception("Error: Transaction already in progress")

	def put(self, key, value):
		if self.in_progress:
			if (isinstance(key, str) and isinstance(value, int)):
				self.in_progress_dictionary[key] = value
			else:
				raise Exception("Error: Key, value must be str, int respectively")
		else:
			raise Exception("Error: Cannot call put while transaction not in progress")


	def get(self, key):
		if (isinstance(key, str)):
			if key in self.dictionary:
				return self.dictionary[key]
			else:
				return None

	def commit(self):
		if self.in_progress:
			self.dictionary.update(self.in_progress_dictionary)
			self.in_progress_dictionary = {}
			self.in_progress = False
		else:
			raise Exception("Error: Cannot call commit if transaction not in progress")

	def rollback(self):
		if self.in_progress:
			self.in_progress_dictionary = {}
			self.in_progress = False
		else:
			raise Exception("Error: Cannot call rollback if transaction not in progress")

def main():
	m = Memory()
	m.begin_transaction()
	m.put("olivia", 2)
	print(m.get("olivia"))
	m.commit()
	print(m.get("olivia"))
	print(m.dictionary)
	m.begin_transaction()
	m.put("hi", 3)
	m.rollback()
	print(m.get("hi"))
	print(m.dictionary)


main()