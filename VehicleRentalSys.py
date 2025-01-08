from json import load, dump
from datetime import datetime


print("project: Vehicle Rental System Using OOPS")
d1=datetime(2024,9,19)
d2=datetime(2024,9,20)
print("DATE: ",d1.strftime("%d"),'-',d2.strftime("%d %b %Y at %p")) # Printing Date of Creation

#class of vehicle
class VehicleRent:

 # class of specific vehicle i.e. Bike
 class Bike: 

   with open("VehicleRentalSys.json") as r:  #reading Json of containing Vehicles Info
       Vi=load(r)#Vi = Vehicle Info

   for Vd in Vi['VehiclePriceQntity']: #Assigning Vehicle info to variables by direct passing in loop if Vehicle is Bike
    if Vd['Vehicle']=='Bike':
      BikeQntity= Vd['VehicleQntity']    
      BikeRentalprice= Vd['VehiclePrice']  
   
   def ShowBQntity(self): #Method to print Vehicle Info I.e. Qntity and Price
      print("Total Bike Quantity: ",self.BikeQntity)
      print("Bike rental Price: ",self.BikeRentalprice," Per Bike per Day")

   def Ask4rent(self, Q4Rent): #Manipulating vehicle info and Rental sys
      if Q4Rent>self.BikeQntity:# if asked quantity is greater than availabole stocks
         print("Enter Quantity within Available Stocks Only!")
      elif 1<Q4Rent<self.BikeQntity: #if asked stocks is within avialable stocks
         print("Total Stocks asked: ",Q4Rent)
         print("Total Price 4 Rental: ",Q4Rent,' * ',self.BikeRentalprice,' = ', Q4Rent * self.BikeRentalprice)
         
         self.BikeQntity=self.BikeQntity-Q4Rent
         print("total Stock Left After rental: ",self.BikeQntity)
      elif Q4Rent<1: #if asked stocks is a -ve int
         print("Error - Enter Positive Qntity only!")
   
   
 class Car: #same logics as for class Bike just replace Car with bike

   with open("VehicleRentalSys.json") as r: 
       Vi=load(r) #Vi = Vehicle Info

   for Vd in Vi['VehiclePriceQntity']:
    if Vd['Vehicle']=='Car':
      CarQntity= Vd['VehicleQntity']    
      CarRentalprice= Vd['VehiclePrice']
   
   def ShowCQntity(self):
      print("Total Car Quantity: ", self.CarQntity)
      print("Car rental Price: ", self.CarRentalprice, " Per Car Per Day")

   def Ask4rent(self, Q4Rent):
      if Q4Rent>self.CarQntity:
         print("Enter Quantity within Available Stocks Only!")
      elif 1<Q4Rent<self.CarQntity:
         print("Total Stocks asked: ",Q4Rent)
         print("Total Price 4 Rental: ", Q4Rent,' * ',self.CarRentalprice,' = ',Q4Rent * self.CarRentalprice)

         self.CarQntity=self.CarQntity-Q4Rent
         print("total Stock Left After rental: ",self.CarQntity)
      elif Q4Rent<1:
         print("Error - Enter Positive Qntity only!")
  

 class Cycle: #same logics as for class Bike and Car

   with open("VehicleRentalSys.json") as r:
       Vi=load(r) #Vi = Vehicle Info

   for Vd in Vi['VehiclePriceQntity']:
    if Vd['Vehicle']=='Cycle':
      CycleQntity= Vd['VehicleQntity']    
      CycleRentalprice= Vd['VehiclePrice']
   
   
   def ShowcQntity(self):
      print("Total Cycle Quantity: ", self.CycleQntity)
      print("Cycle rental Price: ", self.CycleRentalprice, " Per Cycle Per Day")

   def Ask4rent(self, Q4Rent):
      if Q4Rent>self.CycleQntity:
         print("Enter Quantity within Available Stocks Only!")
      elif 1<Q4Rent<self.CycleQntity:
         print("Total Stocks asked: ",Q4Rent)
         print("Total Price for Rental: ",Q4Rent,' * ',self.CycleRentalprice,' = ',Q4Rent * self.CycleRentalprice)

         self.CycleQntity=self.CycleQntity-Q4Rent
         print("total Stock Left After rental: ",self.CycleQntity)
      elif Q4Rent<1:
         print("Error - Enter Positive Qntity only!")

#creating Objects to call class and modules
Bike=VehicleRent.Bike()  #bike Object to call subclass Bike from class VehicleRent
Car=VehicleRent.Car()  #Car Object to call subclass Car from class VehicleRent
Cycle=VehicleRent.Cycle()  #Cycle Object to call subclass Cycle from class VehicleRent

with open("VehicleRentalSys.json") as r:  #reading info from VehicleREntalSys.json file
       Vi=load(r) #Vi = Vehicle Info

while True: #infinite loop untill not breaked
   c=int(input('''  
     1: Start
     2 or Other: EXit
              '''))#asking to start or Exit Sys
   
   if c==1:
     while True:
      print('''
         Select What u wanna take at Rent:
            1. Bike
            2. Car
            3. Cycle
            Other Num. EXit
           ''')
      choice=int(input("Enter Opr[1.Bike/2.Car/3.Cycle/OtherNum.Exit]: "))#asking 4 specific vehicle 4 Rent or EXit

      if choice==1:
         
         # Showing  available Bike Quantity and Price
         print(Bike.ShowBQntity()) 

         while True:
          rentB=int(input("Enter Bike Quantity to Rent: ")) 
          Bike.Ask4rent(rentB) #calling Ask4rent module

          if Bike.BikeQntity > rentB >= 1 : #if asked stock is in available range
            pc=input("Wanna Make Rental Purchase[Yes/No]: ") #asking 4 confirmation 4 purchase

            if pc.lower()=='yes': 
               print("Make Payment.........")
               print("Thank You For Your Confirmation")

               #updating left vehicles quantity after rent
               for Vd in Vi['VehiclePriceQntity']: 
                 if Vd['Vehicle']=='Bike': 
                  Vd['VehicleQntity']= Bike.BikeQntity
               
               #saving left stocks to Json file
               with open("VehicleRentalSys.json", "w") as j: 
                   dump(Vi, j, indent=4) 
               break


      elif choice==2: # same logic as choice 1
         print(Car.ShowCQntity())

         while True:
          rentC=int(input("Enter Car Quantity to Rent: "))
          Car.Ask4rent(rentC)

          if Car.CarQntity > rentC >= 1:
             pc=input("Wanna Make Rental Purchase[Yes/No]: ")

             if pc.lower()=='yes':
               print("Payment Confirmation.........")
               print("Thank You For Your Confirmation")
               
               for Vd in Vi['VehiclePriceQntity']:
                 if Vd['Vehicle']=='Car': 
                  Vd['VehicleQntity']= Car.CarQntity

               with open("VehicleRentalSys.json", "w") as j:
                   dump(Vi, j, indent=4) 
               break

      elif choice==3: # same logic as choice 1 & 2
         print(Cycle.ShowcQntity())

         while True:
          rentc=int(input("Enter Cycle Quantity to Rent: "))
          Cycle.Ask4rent(rentc)

          if Cycle.CycleQntity > rentc >= 1:
             pc=input("Wanna Make Rental Purchase[Yes/No]: ")

             if pc.lower()=='yes':
               print("Payment Confirmation.........")
               print("Thank You For Your Confirmation")

               for Vd in Vi['VehiclePriceQntity']:
                 if Vd['Vehicle']=='Cycle': 
                  Vd['VehicleQntity']= Cycle.CycleQntity

               with open("VehicleRentalSys.json", "w") as j:
                   dump(Vi, j, indent=4) 
               break #breaking loop after succesfull execution
      
      else:
         break # breaking loop if user asks 4 that @vehicle Selection time

   else:
      print("Exiting....! Thanks for Using our Programme")
      break # breaking loop if user asks 4 that @Starting System
   