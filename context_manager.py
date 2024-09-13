'''Context managers allow you to manage resources safely using the with statement.
They are implemented using __enter__ and __exit__ methods.
Example:'''

class File:
    def __init__(self, filename, mode) -> None:
        self.filename=filename
        self.mode=mode

        pass    
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    def __exit__(self,exc_type,exc_value, tracback):
        self.file.close()
with File('example.txt','w') as f:
    f.write ('Hello- world!')
