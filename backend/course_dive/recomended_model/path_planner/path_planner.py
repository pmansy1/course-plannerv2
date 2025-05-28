import networkx as nx
from ..user_profile import User_student
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