// LeetCode 207: Course Schedule
// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.

import java.util.*;

public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // Build adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        int[] indegree = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int prereq = prerequisite[1];
            graph.get(prereq).add(course);
            indegree[course]++;
        }
        
        // Topological sort using Kahn's algorithm
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        int processedCourses = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            processedCourses++;
            
            for (int nextCourse : graph.get(course)) {
                indegree[nextCourse]--;
                if (indegree[nextCourse] == 0) {
                    queue.offer(nextCourse);
                }
            }
        }
        
        return processedCourses == numCourses;
    }
    
    // DFS approach to detect cycle
    public boolean canFinishDFS(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] prerequisite : prerequisites) {
            graph.get(prerequisite[1]).add(prerequisite[0]);
        }
        
        int[] visited = new int[numCourses]; // 0: unvisited, 1: visiting, 2: visited
        
        for (int i = 0; i < numCourses; i++) {
            if (visited[i] == 0 && hasCycle(graph, i, visited)) {
                return false;
            }
        }
        
        return true;
    }
    
    private boolean hasCycle(List<List<Integer>> graph, int course, int[] visited) {
        if (visited[course] == 1) {
            return true; // Cycle detected
        }
        if (visited[course] == 2) {
            return false; // Already processed
        }
        
        visited[course] = 1; // Mark as visiting
        
        for (int nextCourse : graph.get(course)) {
            if (hasCycle(graph, nextCourse, visited)) {
                return true;
            }
        }
        
        visited[course] = 2; // Mark as visited
        return false;
    }
    
    public static void main(String[] args) {
        CourseSchedule solution = new CourseSchedule();
        
        int[][] prerequisites1 = {{1, 0}};
        int[][] prerequisites2 = {{1, 0}, {0, 1}};
        
        System.out.println("Can finish 2 courses: " + solution.canFinish(2, prerequisites1));
        System.out.println("Can finish 2 courses: " + solution.canFinish(2, prerequisites2));
    }
}