class CreateUserDto:
    email: str
    sub: str
    name: str
    given_name: str
    family_name: str

    def __init__(self, sub, name, given_name, family_name, email):
        self.email = email
        self.name = name
        self.sub = sub
        self.given_name = given_name
        self.family_name = family_name
