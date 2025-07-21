import networkx as nx


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
    
class PathPlanner:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_prerequisites(self, course_pairs):
        self.graph.add_edges_from(course_pairs)

    def get_available_courses(self, completed):
        available = []
        for course in self.graph.nodes:
            if course not in completed:
                prereqs = set(self.graph.predecessors(course))
                if prereqs.issubset(set(completed)):
                    available.append(course)
        return available

    def find_path(self, start_courses, end_course):
        if end_course not in self.graph.nodes:
            return {"error": f"{end_course} is not found in the course graph."}

        paths = []
        for start in start_courses:
            if start in self.graph.nodes and nx.has_path(self.graph, start, end_course):
                try:
                    path = nx.shortest_path(self.graph, start, end_course)
                    paths.append(path)
                except nx.NetworkXNoPath:
                    continue

        if not paths:
            return {"error": f"No path found from {start_courses} to {end_course}."}
        return paths