'''You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

 

Example 1:

Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)
Example 2:

Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)
Example 3:

Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.'''


from collections import deque

class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)

        def canAssign(k):
            # try to assign the k smallest tasks using the k strongest workers
            dq = deque()
            p = pills
            i = 0
            # iterate through the k strongest workers in ascending order
            for w in workers[m-k:]:
                # enqueue every task that this worker could do if boosted
                while i < k and tasks[i] <= w + strength:
                    dq.append(tasks[i])
                    i += 1
                # if no candidate tasks, we fail
                if not dq:
                    return False
                # if the weakest queued task can be done without a pill, do it
                if dq[0] <= w:
                    dq.popleft()
                else:
                    # otherwise use a pill on the strongest queued task
                    if p == 0:
                        return False
                    p -= 1
                    dq.pop()
            return True

        left, right, ans = 0, min(n, m), 0
        while left <= right:
            mid = (left + right) // 2
            if canAssign(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
