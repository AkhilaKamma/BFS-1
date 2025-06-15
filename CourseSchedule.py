#detecting a cycle in a directed graph, 
# which can be solved using Kahn's algorithm (topological sorting using BFS).

#Time Complexity: O(V + E)
#Space Complexity: O(V + E)

from collections import deque, defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Create adjacency list and in-degree array
        hashmap = defaultdict(list)  # key: course, value: list of dependent courses
        in_degree = [0] * numCourses

        # Build the graph
        for dest, src in prerequisites:
            hashmap[src].append(dest)
            in_degree[dest] += 1

        # Initialize queue with nodes having in-degree 0 (no prerequisites)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Count how many courses can be completed
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1
            for neighbor in hashmap[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses completed, return True
        return completed == numCourses
