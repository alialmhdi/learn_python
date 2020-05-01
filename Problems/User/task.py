class User:
    # create the class here
    n_active = 0
    users = []
    def __init__(self, active, user_name):
        self.active = active
        self.user_name = user_name
        if self.active:
            self.users.append(self.user_name)
        self.n_active = len(self.users)