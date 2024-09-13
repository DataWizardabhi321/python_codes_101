#import  required  modules   first 
from abc import ABC , abstractclassmethod , abstractmethod

#create  a  base  class
class car(ABC):
    #constructor  to  initialize using the __init__
    def __init__(self, brand, model, year) -> None:
        self.brand= brand
        self.model=model
        self.year=year
        #create  a  abstract  method
    @abstractmethod  #this is  a  decorator 
    def printdetails(self):
        pass
    #concrete  method  for accelarating
    def accelarate(self):
        print('speeding  up')

    #conccreate method  for applying break
    def brake_applied(self):
        print('car stopped')
#create  a child class for   the hatch back cars 
class hahtchback(car):
    #implementing  the abstract method to print details
    def  printdetails(self):
        print("Brand", self.brand);
        print("model",self.model);
        print("year",self.year);
   #specific  method  for hatchback cars 
    def sunroof(self):
      print('not having  this  feature')

    #create a  child  class  for   suv's
    class Suv(car):
        #implementing the abstract method  to print detials
        def printdetails(self):
            print('Brand:',self.brand);
            print('model:',self.model);
            print('year:',self.year);
#specific method  for  suv's
def sunroof(self):
    print('available')
#institianate  a  hatchback object 
car1 = hahtchback('maruti','Alto','2022');

#call  the printdetails method of the, car1  to print   the details
car1.printdetails()

#call  the car   to accelarate  with  the accelarate  method 
car1.accelarate()

        