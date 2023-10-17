
class Task:
    tasks =[]
    def __init__(self,task):
          self.tasks.append(task)
    
    def add_task(self,task):
        self.tasks.append(task)
    def list_tasks(self):
        for i,task in enumerate(self.tasks,start=1):
            print(f"{i},{task}")
    def run_task(self):
     while True:
         # input string value
         choice = input("Enter your choice: ")
         print(choice)
         if choice == "1":
            task = input("Enter a task ")
            self.add_task(task)
         elif choice == "2":
            self.list_tasks()
         elif choice == "3":
            print("Good Bye!")
            break
         else:
            print("Invalid choice. Press try again.")

