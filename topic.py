import sys
from ngram import NGram

class TopicDetector: 
	def __init__(self,text):
		self.ng=[]
		self.topic=[]
		file = open(text,"r")

		for linea in file.readlines():
			words = linea.split(" ")
			self.topic += [words[0]]
			nng = NGram(words[2].split(","))
			self.ng += [nng]
		file.close()

    	'''
    	file = open(text,"r")
		linea = file.readline()
		while linea != '':
			words = linea.split(" ")
			self.topic += [words[0]]
			nng = NGram(words[2].split(","))
			self.ng += [nng]
			linea = file.readline()
		file.close()
		'''

	def verify(self,text_compare):
		results = []
		texto = []
		'''
		file2 = open(text_compare,"r")
		for linea2 in file2.readlines():
			texto+=linea2.split(" ")
		tng=NGram(texto)
		file2.close()
		'''
		file2 = open(text_compare,"r")
		linea2 = file2.readline()
		while linea2 != '':
			texto+=linea2.split(" ")
			linea2 = file2.readline()
		tng=NGram(texto)
		file2.close()

		for ngs in self.ng:
			count=0
			for word in list(ngs):
				for porc in tng.search(word):
					if porc[1]>0.3:
						count+=1
			results+=[count]

		#print list(results)

		pos=0
		count=0
		i=0
		for res in results:
			if count<res:
				count=res
				pos=i
			i+=1

		if results[pos]>2:
			print("Tema mas preciso del texto: "+repr(self.topic[pos]))
		else:
			print("No se ha podido precisar de que trata")
				

			


if __name__ == '__main__':
	Detector=TopicDetector("topicos.txt")
	Detector.verify("texto1.txt")
	Detector.verify("texto2.txt")
	Detector.verify("texto3.txt")