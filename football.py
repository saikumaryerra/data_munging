import dataExtractor as dE
import dataAnalyser as dA
class football:

    def __init__(self,file_path):
        self.file_path=file_path
        self.extractor=dE.dataExtractor(file_path)
        self.analyzer=dA.dataAnalyser()
    
    def calculate_min_difference(self,column_1,column_2):
        result=self.extractor.data()
        print(self.analyzer.calculate_min_difference(result,column_1,column_2))
if __name__=='__main__':
    file_path='football.dat'
    k=football(file_path)
    k.calculate_min_difference('F','A')