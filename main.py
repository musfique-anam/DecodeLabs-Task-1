#Project 1: The To-Do List

# MODEL (Data Logic & Memory Management)
def insert_task(database_list, task_description):

    # Create an auto-incrementing Primary Key ID based on current list state
    task_id = len(database_list) + 1
    
    # Primitive Database Table Row mapping
    task_record = {
        "id": task_id,
        "task": task_description
    }
    
    # Store reference pointer in the volatile memory container
    database_list.append(task_record)
    return task_record

# VIEW (User Interface / Read Operations)
def render_task_view(database_list):
    if not database_list:
        print("\n[SYSTEM] Heap status: Clear. Volatile database is currently empty.")
        return

    print("\n" + "=" * 40)
    print(f"{'ID':<6} | {'TASK RECORD SYSTEM (IN-MEMORY)':<30}")
    print("=" * 40)
    
    # Avoids non-Pythonic range(len()) manual indexing
    for sequence_num, task_record in enumerate(database_list, start=1):
        # Extracting structural dictionary key values
        record_id = task_record["id"]
        task_text = task_record["task"]
        print(f"[{record_id:02d}]  | {task_text}")
        
    print("=" * 40)

# CONTROLLER / INPUT (System Orchestration)
def main():

    # The volatile RAM container (The primitive core database list)
    my_tasks = []
    
    while True:
        print("\n>>> DECODELABS SYSTEM ENGINE <<<")
        print("1. [INPUT]   Add New Task Record")
        print("2. [DISPLAY] View Dynamic Array State")
        print("3. [EXIT]    Terminate Process (Data Volatility Warning)")
        
        user_choice = input("\nSelect system execution parameter (1-3): ").strip()
        
        if user_choice == "1":
            raw_input = input("Enter task description string: ").strip()
            if raw_input:
                new_record = insert_task(my_tasks, raw_input)
                print(f"[SUCCESS] Record serialized to Heap Memory: {new_record}")
            else:
                print("[WARNING] Constraints Violation: Task cannot be empty.")
                
        elif user_choice == "2":
            render_task_view(my_tasks)
            
        elif user_choice == "3":
            # Warning block: The Volatile Trap
            print("\n[WARNING] Process Terminated. RAM container released. Volatile data cleared.")
            break
            
        else:
            print("[ERROR] Instruction code invalid. Please input 1, 2, or 3.")

if __name__ == "__main__":
    main()