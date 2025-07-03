select=(input("Enter the name of the country:"))
class USA():
    def capital(self):
        print("Washington,D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
obj_USA=USA()
obj_India=India()

if select =="India":
    obj_India.capital()
    obj_India.language()
else:
    obj_USA.capital()
    obj_USA.language()
     