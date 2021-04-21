class Pets:
    def __init__ (self, nickname, gender, age):
        self.nickname = nickname
        self.gender = gender
        self.age = age

    def get_nickname(self):
        return self.nickname

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age   

    def get_cats(self):
        print(f'Nickname: {self.nickname}')
        print(f'Gender: {self.gender}')
        print(f'Age: {self.age}')     
