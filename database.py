tasks_db = []

current_id = 1

def get_all_tasks():
    return tasks_db

def add_task(title: str, deadline: str, chat_id: int):
    global current_id

    new_task = {
        "id": current_id,
        "title": title,
        "deadline": deadline,
        "chat_id": chat_id,
        "completed": False,
        "notified": False 
    }

    tasks_db.append(new_task)
    current_id += 1
    return new_task

def mark_task_completed(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    return None