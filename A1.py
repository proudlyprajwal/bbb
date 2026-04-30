from collections import defaultdict, deque

def course_planner():

    n = int(input("Enter number of courses: "))
    courses = []

    print("Enter course names:")
    for i in range(n):
        course = input().strip()
        courses.append(course)


    m = int(input("Enter number of prerequisite pairs: "))
    prerequisites = []

    print("Enter prerequisite pairs (CourseA CourseB):")
    for i in range(m):
        a, b = input().split()
        prerequisites.append((a, b))


    graph = defaultdict(list)
    indegree = {course: 0 for course in courses}

    for pre, course in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1


    queue = deque()
    for course in courses:
        if indegree[course] == 0:
            queue.append(course)

    topo_order = []

    while queue:
        current = queue.popleft()
        topo_order.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)


    if len(topo_order) != len(courses):
        print("\nError: Curriculum plan is invalid.")
        print("Reason: Cyclic dependencies detected.")
    else:
        print("\nValid course completion order:")
        for course in topo_order:
            print(course)


course_planner()