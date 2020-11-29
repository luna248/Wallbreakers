class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        #Summarize problem: Find the most optimal way to spread out the work between
        #d days to acheive minimal difficulty with the schedule

        #prevDayMinimal: Keep track of minimal difficulty from the previous day with all the jobs
        #bestCase: Helps us keep track of bestcase scenario uptil that index over the number
        #of days
        numOfJobs = len(jobDifficulty)

        if numOfJobs < d:
            return -1

        prevDayMinimal = [float(inf)] *numOfJobs
        bestCase = [0] *numOfJobs

        for day in range(d):
            #the stack helps us keep track of all the jobs that require as much or less effort in
            #the day as the current job
            stack = []
            for x in range(day, numOfJobs):
                #The first job on the first days has to be jobDifficulty[0]
                if not x:
                    bestCase[0] = jobDifficulty[x]
                else:
                    bestCase[x] = prevDayMinimal[x-1] + jobDifficulty[x]

                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[x]:
                    thisJob = stack.pop()
                    bestCase[x] = min(bestCase[x], bestCase[thisJob] - jobDifficulty[thisJob] + jobDifficulty[x])
                if stack:
                    bestCase[x] = min(bestCase[x], bestCase[stack[-1]])
                stack.append(x)

            #When we're done evaluating a day, we update the prevDayMinimal and reset bestCase
            prevDayMinimal = bestCase
            bestCase = [0] * numOfJobs

        return prevDayMinimal[-1]
