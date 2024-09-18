def findByTitle(obj, title):
    return obj.title == title

class Task:
    title = str()
    description = str()
    priority = str()
    status = str()
    
    def setStatus(self, status):
        self.status = status

class TaskManager: 
    listTask = []

    def add_task(self, task):
        t1 = Task()
        
        t1.title = 'Оно работает?'
        t1.description = 'Надеюсь'
        t1.priority = 'High'
        t1.status = 'выполнена'
        
        self.listTask.append(task) 
        
    def remove_task(self, key):
        del self.listTask[key]
    
    def change_status(self, title, status='done'):
        task = list(filter(lambda elem: elem.title == title, self.listTask))[0]
        task.setStatus(status)
        print(task.status)
    
    def get_tasks_by_priority(self, listTask, priority):
        for key in self.listTask:
            if(key.status == priority):
                print(self.listTask[key])
                
    def list_all_task(self):
        return self.listTask
    

m1 = TaskManager()


m1.add_task(t1)
print(m1.list_all_task())
m1.change_status('Оно работает?')