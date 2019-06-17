class dataAnalyser:
    def calculate_min_difference(self,data,column_1,column_2):
        for i in range(len(data)):
            x=abs(float(data[i][column_1].strip('*'))-float(data[i][column_2].strip('*')))
            try:
                if x < min_diff:
                    min_diff=x
                    min_diff_index=i
            except:
                min_diff=x
                min_diff_index=i
        return list(data[min_diff_index].values())[0]