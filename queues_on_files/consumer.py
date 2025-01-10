import csv
from time import sleep


def find_job():
    with open('jobs.csv', mode='r', newline='', encoding='utf-8') as jobs_file:
        jobs = csv.DictReader(jobs_file)
        for job in jobs:
            if job['status'] == 'pending':
                return job
    return None


def start_finish_job(todo_job, job_status):
    if not todo_job:
        return

    job_id_to_update = todo_job['job_id']
    with open('jobs.csv', mode='r', newline='', encoding='utf-8') as jobs_file:
        jobs = list(csv.DictReader(jobs_file))

    for job in jobs:
        if job['job_id'] == job_id_to_update:
            job['status'] = job_status
            break

    with open('jobs.csv', mode='w', newline='', encoding='utf-8') as jobs_file:
        writer = csv.DictWriter(jobs_file, fieldnames=jobs[0].keys())
        writer.writeheader()
        writer.writerows(jobs)


def do_job():
    while True:
        print("Szukam pracy")
        todo_job = find_job()
        if todo_job is not None:
            print("Rozpoczynam pracę")
            start_finish_job(todo_job, 'in_progress')
            sleep(30)
            start_finish_job(todo_job, 'done')
            print("Kończę pracę")
        else:
            print("Brak pracy")
        sleep(5)


if __name__ == "__main__":
    do_job()
