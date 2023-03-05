import os
import yaml


tasks_folder_path = '/mnt/c/Users/f77541a/repos/kb/2 Areas/Journal/tasks'

class Task:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def __lt__(self, other):
         # If rank is None, set it to 0
        if self.rank is None:
            self.rank = 0
        if other.rank is None:
            other.rank = 0

        return self.rank < other.rank

    def __repr__(self):
        return f"T Rank={self.rank}. {self.name}"

tasks = []
for filename in os.listdir(tasks_folder_path):
    if filename.endswith('.md'):

        # If file name is "TASKS DB.md" or "TASKS DV TABLE.md", skip it
        if filename in ['TASK DB.md', 'TASKS DV TABLE.md']:
            continue

        # Print Processing: File Name
        # print(f"Processing: {filename}")

        with open(os.path.join(tasks_folder_path, filename), 'r') as file:
            contents = file.read().split('---')[1]
            metadata = yaml.safe_load(contents)
            rank = metadata.get('rank')
        tasks.append(Task(filename, rank))

# Sort the tasks list by rank in ascending order
#tasks.sort(key=lambda x: x.rank)

tasks.sort()

# Print each task nicely to the console
for task in tasks:
    print(task)
