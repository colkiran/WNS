# duck types

class Manager:
    def doJob(self):
        print("Manager's Job.......")

class Developer:
    def doJob(self):
        print("Developer's Job..........")

def BankFunJobs(emps):       # polymorphism
    print("Bank Job Started...........")
    for emp in emps:
        emp.doJob()
    print("Bank Job Ended...........")
    print("-" * 40)

Mary = Manager()
Daniel = Developer()

BankFunJobs([Mary, Daniel])


