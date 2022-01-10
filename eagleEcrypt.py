import string

class EcryptionEagel:

	__chars = string.ascii_letters

	def __Mapping(self):

		__data = EcryptionEagel.__chars

		__Map = {'52': " ", '53': '\n'}

		for i in range(len(__data)):

			__Map[str(i)] = __data[i]

		return __Map


	def __SliceString(self, data):

		__data = data.split()

		return __data


	def Encrypt(self, data):

		__Encryption = ''

		for eachChar in range(len(data)):

			for key, value in EcryptionEagel.__Mapping(self).items():

				if value == data[eachChar]:

					__Encryption = __Encryption + key + " "

		return __Encryption


	def Decrypt(self, data):

		__decrypt = ''
		__newList = EcryptionEagel.__SliceString(self,data)

		for i in range(len(__newList)):

			for key, value in EcryptionEagel.__Mapping(self).items():

				if key == __newList[i]:

					__decrypt = __decrypt + value

		return __decrypt

E = EcryptionEagel()
x = E.Encrypt("This is the name")
print(x)