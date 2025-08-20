'''This is DOC string of task 2'''
class Human:
    '''This is DOC string of class Human'''
    def __init__(self, name):
        self.name = name

    def welcome(self):
        '''This is DOC string of method'''
        print(f'Welcome {self.name}!')

    @classmethod
    def species(cls):
        '''This is DOC string of class method'''
        print('Homosapiens')

    @staticmethod
    def arbitray_msg():
        '''This is DOC string of static method'''
        print('Arbitray message')

leo = Human('Leonid')
leo.welcome()
leo.species()
leo.arbitray_msg()
