from mrjob.job import MRJob
from mrjob.step import MRStep

class MRLabelSummary(MRJob):

    def mapper(self,_,line):
        label,value=line.split()
        label=int(label)
        value=float(value)
        sqvalue = float(value*value)
        yield (label, (1,value,sqvalue))

    def reducer(self,label,packedvalues):
        cumVal=0.0; cumSumSq=0.0; cumN=0.0
        for val in packedvalues:
            cumN += float(val[0])
            cumVal += float(val[1])
            cumSumSq += float(val[2])
        mean=cumVal/cumN
        var=(cumSumSq - 2*mean*cumVal + cumN*mean*mean)/(cumN-1)  
        yield (label,(cumN,mean,var))

if __name__=='__main__':
    MRLabelSummary.run()
