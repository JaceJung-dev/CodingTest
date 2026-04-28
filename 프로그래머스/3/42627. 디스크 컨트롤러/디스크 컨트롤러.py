import heapq


def solution(jobs):
    n = len(jobs)

    jobs = [(i, jobs[i][0], jobs[i][1]) for i in range(n)]
    jobs.sort(key=lambda x: x[1])

    heap = []
    cur_time = 0
    cur_id = 0
    turnaround_time = 0
    done = 0

    while done < n:
        while cur_id < n and jobs[cur_id][1] <= cur_time:
            id, start, duration = jobs[cur_id]
            heapq.heappush(heap, (duration, start, id))
            cur_id += 1

        if heap:
            duration, start, id = heapq.heappop(heap)

            cur_time += duration
            turnaround_time += cur_time - start
            done += 1
        else:
            cur_time = jobs[cur_id][1]

    return turnaround_time // n
