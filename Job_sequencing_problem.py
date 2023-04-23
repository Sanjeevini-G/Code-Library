def job_sequencing(jobs):
    jobs.sort(reverse=True, key=lambda x: x[2])
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    slot = [False] * (max_deadline + 1)
    result = [None] * max_deadline
    for job in jobs:
        for i in range(job[1], 0, -1):
            if not slot[i]:
                slot[i] = True
                result[i - 1] = job[0]
                break
    return [x for x in result if x is not None]

jobs = [("J1", 2, 60), ("J2", 1, 100), ("J3", 3, 20), ("J4", 2, 40)]
print(job_sequencing(jobs))  # Output: ['J2', 'J1', 'J4']
