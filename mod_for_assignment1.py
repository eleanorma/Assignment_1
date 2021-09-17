def compute_total_per_week(hrs1,hrs2,hrs3,total_hrs):
    total_hrs = float(hrs1) + float(hrs2) + float(hrs3)
    return total_hrs

def compute_task_avg(total_hrs,avg_hrs):
    avg_hrs = 0
    avg_hrs = round((total_hrs/3),2)
    return avg_hrs