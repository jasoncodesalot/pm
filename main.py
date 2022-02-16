import json

def main():
    tasks = [
        {"name": "Make UI", "completed": False},
        {"name": "Make storage backend", "completed": True},
        {"name": "Make github project", "completed": True}
    ]
    with open('data.json', 'w') as f:
        json.dump(tasks, f)

main()