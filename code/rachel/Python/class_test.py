import datetime as dt

class Member:
    """Create a new member"""
    free_days = 365

    def __init__(self, uname, fname):
        #Define attributes and give them values
        self.username = uname
        self.fullname = fname
        #Default date_joined as today's date
        self.date_joined = dt.date.today()
        #Set is active to True initially
        #self.is_active = True
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)

    #A method to return a formatted string showing date joined
    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined:%m-%d-%y}"
    
    #Method to activate (True) or deactivate (False) account
    def activate(self, yesno):
        """True for active, False to make inactive"""
        self.is_active = yesno
    
    free_days = 90

#Create an instance of the Member class named new_guy
#new_guy = Member('Rambo', 'Rocco Moe')
wilbur = Member('wblomgren', 'Wilbur Blomgren')



print(wilbur.date_joined)
print(wilbur.free_expires)

#Is the new guy active?
#print(new_guy.is_active)

#Try out the activate method
#new_guy.activate(False)

#print(new_guy.is_active)
