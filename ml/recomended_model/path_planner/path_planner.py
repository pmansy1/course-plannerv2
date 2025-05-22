import networkx as nx
from recomended_model.user_profile import User_student
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
                if prereqs.issubset(completed):
                    available.append(course)
        return available

    def find_path(self, start_courses, end_course):
        paths = []
        for start in start_courses:
            if nx.has_path(self.graph, start, end_course):
                paths.append(nx.shortest_path(self.graph, start, end_course))
        return paths