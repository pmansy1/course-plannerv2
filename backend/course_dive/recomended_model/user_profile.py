
class User_student():
    def __init__(self, user_id, name, age, major, minor, year, exp_grad_year, credits_completed, completed_courses):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.major = major
        self.minor = minor
        self.year = year
        self.exp_grad_year = exp_grad_year
        self.credits_completed = credits_completed
        self.completed_courses = completed_courses
        self.courses_rec = []
        self.interests = []
    
    def add_interest(self, interest: list):
        for i in interest:
            if i not in self.interests:
                self.interests.append(i)
        print(f"Interest '{interest}' added to user {self.name}.")
    

    def remove_interest(self, interest):
        if interest in self.interests:
            self.interests.remove(interest)
            print(f"Interest '{interest}' removed from user {self.name}.")
        else:
            print(f"Interest '{interest}' not found in user {self.name}'s interests.")
    
    def update_courses(self, courses):
        for i in courses:
            if i not in self.courses_rec:
                self.courses_rec.append(i)
        print(f"Courses updated for user {self.name}.")


    def get_user_profile(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "minor": self.minor,
            "year": self.year,
            "exp_grad_year": self.exp_grad_year,
            "credits_completed": self.credits_completed,
            "completed_courses": self.completed_courses,
            "courses_rec": self.courses_rec,
            "interests": self.interests
        }
    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Major: {self.major}, Year: {self.year}, Completed Courses: {self.completed_courses}"
    
