import datetime as dt

class Member:
    """Create a new member"""
    free_days = 365

    def __init__(self, username, fullname):
        #Define attributes and give them values
        self.date_joined = dt.date.today()
        #Set an expiration date
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)

    #Class methods follow @classmethod decorator and refer to cls rather than to self
    @classmethod
    def setfreedays(cls,days):
        cls.free_days = days
