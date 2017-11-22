from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE=re.compile(r'\w+')

class MRWordFrequencyCount(MRJob):

    def mapper(self,_,line):
        #yield each word in the line
        for word in WORD_RE.findall(line):
            yield (word.lower(),1)

    def combiner(self,word,counts):
        #in each line, sum words
        yield (word,sum(counts))
        
    def reducer(self,word,counts):
        #acquire number of occurrence
        yield (word,sum(counts))


if __name__=='__main__':
    MRWordFrequencyCount.run()
