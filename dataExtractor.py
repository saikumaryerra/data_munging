class dataExtractor:
    def __init__(self,file_path):
        self.file_path=file_path
    
    def data(self):
        file_path=self.file_path
        with open(file_path,'r') as file:
            file_reader=file.readline()
            column_name=file_reader.strip('\n').split()
            column_index=[]
            search_index=0
            for i in column_name:
                search_index=file_reader.index(i,search_index)
                column_index.append(search_index)
                
            rows=file.readlines()
        data=[]
        for row in rows:
            row_data={}
            for i in range(len(column_index)):
                column_index_start=column_index[i]
                if i==len(column_index)-1:
                    column_index_end=0
                else:
                    column_index_end=column_index[i+1]
                column_value=row[column_index_start:column_index_end].strip('-')
                if column_value!='':
                    row_data[column_name[i]]=column_value.strip(' -\n')
            data.append(row_data)
        try:
            data.remove({})
        except:
            pass
        return data
            