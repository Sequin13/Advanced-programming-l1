import csv
import os


def get_latest_id():
    if not os.path.exists('jobs.csv'):
        with open('jobs.csv', 'w') as file:
            file.write('')
    with open('jobs.csv', 'r') as jobs:
        reader = csv.DictReader(jobs)
        ids = [
            int(row['job_id']) for row in reader if row['job_id'].isdigit()
        ]
        return max(ids, default=0)


def save_job():
    job_id = get_latest_id() + 1
    data = [{'job_id': job_id, 'status': 'pending'}]

    write_header = not os.path.exists('jobs.csv')

    with open('jobs.csv', 'a', newline='') as jobs:
        fieldnames = ['job_id', 'status']
        writer = csv.DictWriter(jobs, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    save_job()
