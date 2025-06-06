class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None
   
    def set_occupant(self, name):
        
        if self.free==1:
            self.occupant = name
            self.free = False
            print(f"{self.occupant} is assigned to this seat")
        else:
            print(f"{self.occupant} is occupying the seat")
    

    def remove_occupant(self):
       
        if self.free==0:
            removed_name = self.occupant
            self.free==1
            print(f"{self.occupant} is removed from seat")
        