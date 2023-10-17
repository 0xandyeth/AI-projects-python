#main.py
import sys
sys.path.append('todo')
from todo_module import Task

#create instance of Task class
object = Task("apple")

#use the Task class instance
object.run_task()