import sys
from ngram import NGram

class TopicDetector:
	def __init__(self,text):
		self.ng=[]
		self.topic=[]
		file = open(text,"r")
		
		for linea in file.readlines():
    		words = linea.split("\t")
    		topic+=[words[0]]
    		nng=NGram(words[1].split(" "))
    		ng+=[nng]
    	
    	file.close()

	def verify(self,text_compare):
		results = []
		file = open(text_compare,"r")
		
		texto = []
		for linea in file.readlines():
			texto+=linea.split(" ")
		tng=NGram(texto)

		file.close()

		for ngs in ng:
			count=0
			for word in list(ng):
				count+=len(tng.items_sharing_ngrams(word))
			results+=[count]

		pos=0
		count=0
		i=0
		for res in results:
			if count<res:
				count=res
				pos=i
			i+=1

		print("Tema mas preciso del texto: "+repr(topic[pos]))
				

			


if __name__ == '__main__':
	Detector=TopicDetector("topicos.txt")
	Detector.verify("texto1.txt")