class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
        

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = int(age)

    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

#Test code
Thomas = Student("Prester", 20, ["ENG","BIO"], 39.40)
Thomas.change_name("Thomas")
print(Thomas.name)
Thomas.change_age("16")
Thomas.add_track("Physiology")
print(Thomas.get_score())


#@George Akor
#theStormGod



