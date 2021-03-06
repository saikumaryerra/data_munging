import dataExtractor as dE
import dataAnalyser as dA
class weather:

    def __init__(self,file_path):
        self.file_path=file_path
        self.extractor=dE.dataExtractor(file_path)
        self.analyzer=dA.dataAnalyser()
    
    def calculate_min_difference(self,column_1,column_2):
        result=self.extractor.data()
        result.pop()
        print(self.analyzer.calculate_min_difference(result,column_1,column_2))
if __name__=='__main__':
    file_path='weather.dat'
    k=weather(file_path)
    k.calculate_min_difference('MxT','MnT')