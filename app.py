import os
import yaml
from classes import Task

tasks_folder_path = '/mnt/c/Users/f77541a/repos/kb/2 Areas/Journal/tasks'
ignore_files = ['TASKS DB.md', 'TASKS DV TABLE.md', 'tasks-config.md']

# clear the console
os.system('cls' if os.name == 'nt' else 'clear')

print(f"Task Commander v0.1.")

tasks = []

# ------------------------------------------------------------------------
# Function: load
# ------------------------------------------------------------------------

def load():

    if len(tasks) > 0:
        tasks.clear()

    for filename in os.listdir(tasks_folder_path):
        if filename.endswith('.md'):

            # Skip ignored files...
            if filename in ignore_files:
                continue

            with open(os.path.join(tasks_folder_path, filename), 'r') as file:
                contents = file.read().split('---')[1]
                metadata = yaml.safe_load(contents)
                rank = metadata.get('rank')
                # Get external-tracking-id if it exists, otherise set it to None
                external_tracking_id = metadata.get('external-tracking-id')
            tasks.append(Task(filename, rank, external_tracking_id))
    tasks.sort()
    print('Tasks Loaded')

# ------------------------------------------------------------------------
# Function: ls
# ------------------------------------------------------------------------

def list_tasks():
    
    if len(tasks) == 0:
        load()

    result = ""
    for task in tasks:
        result += str(task)

    return result

# ------------------------------------------------------------------------
# Function: normalize_rank
# ------------------------------------------------------------------------

def normalize_rank():
    #if tasks is not loaded, load it
    if len(tasks) == 0:
        load()

    # Renumber the rank field in each task and save the modified file
    rank_counter = 5
    for task in tasks:
        old_rank = task.rank
        task.rank = rank_counter
        rank_counter += 5
        print(f"Renumbering rank from {old_rank} to {task.rank}: {task.name}")
    command = input("\n Proceed? Yes or No (y|n) > ")
    if command == "y" or command == "yes":
        for task in tasks:
            # Read the file
            with open(os.path.join(tasks_folder_path, task.name), 'r') as file:
                contents = file.read()
                # Split the file into frontmatter and body
                frontmatter, body = contents.split("---\n")[1:]
                # Parse the YAML frontmatter
                metadata = yaml.safe_load(frontmatter)
                metadata['rank'] = task.rank

            # Write the updated frontmatter and body back to the file
            with open(os.path.join(tasks_folder_path, task.name), "w") as f:
                f.write(f"---\n{yaml.dump(metadata)}---\n{body}")
        print('Task ranking normalized (5,10,15,20, etc...)')

    if command == "n" or command == "no":
        print("Task rank normalization aborted.")
        return

while True:
    command = input("> ")

    if command == "exit" or command == "q":
        break
    elif command == "help" or command == "?":
        help_cmds = """
        Available commands:\n
        'help' or '?'
        'bubble sort' or 'bubble'
        'load' - loads all mardown file meta into memory
        'ls' to load and list
        'exit' or 'q' to quit       
        """
        print(help_cmds)
    elif command == "load":
        load()
    elif command == "ls":
        tasks = list_tasks()
        print(tasks)
    elif command == "normalize rank" or command == "nr":
        normalize_rank()
    else:
        print("Unknown command. Type 'help' to see the list of available commands.")
