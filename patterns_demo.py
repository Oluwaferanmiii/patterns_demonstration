# Singleton Pattern: Ensures only one instance of AccessPolicyManager exists
class AccessPolicyManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating the AccessPolicyManager instance")
            cls._instance = super(AccessPolicyManager, cls).__new__(cls)
            # Initialization code here if needed
        return cls._instance

    def manage_policy(self):
        print("Managing access policy")


# Factory Method Pattern: Creates different types of users based on role

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_role(self):
        raise NotImplementedError("Subclasses must implement get_role")


class AdminUser(User):
    def get_role(self):
        return f"Admin user {self.user_id}"


class LecturerUser(User):
    def get_role(self):
        return f"Lecturer user {self.user_id}"


class StudentUser(User):
    def get_role(self):
        return f"Student user {self.user_id}"


class VisitorUser(User):
    def get_role(self):
        return f"Visitor user {self.user_id}"


class RoleUserFactory:
    @staticmethod
    def create_user(role, user_id):
        if role == "ADMIN":
            return AdminUser(user_id)
        elif role == "LECTURER":
            return LecturerUser(user_id)
        elif role == "STUDENT":
            return StudentUser(user_id)
        else:
            return VisitorUser(user_id)


# Observer Pattern: Subject notifies observers of events

class Observer:
    def update(self, event):
        raise NotImplementedError("Subclasses must implement update")


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, event):
        print(f"Observer {self.name} received event: {event}")


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)
        print(f"Attached observer: {observer.name}")

    def detach(self, observer):
        self.observers.remove(observer)
        print(f"Detached observer: {observer.name}")

    def notify(self, event):
        print(f"Notifying observers about event: {event}")
        for observer in self.observers:
            observer.update(event)


# Demonstration
if __name__ == "__main__":
    print("Demonstrating Singleton Pattern:")
    manager1 = AccessPolicyManager()
    manager2 = AccessPolicyManager()
    print(f"Are both instances the same? {manager1 is manager2}")
    manager1.manage_policy()

    print("\nDemonstrating Factory Method Pattern:")
    factory = RoleUserFactory()
    admin = factory.create_user("ADMIN", 1)
    lecturer = factory.create_user("LECTURER", 2)
    student = factory.create_user("STUDENT", 3)
    visitor = factory.create_user("GUEST", 4)
    print(admin.get_role())
    print(lecturer.get_role())
    print(student.get_role())
    print(visitor.get_role())

    print("\nDemonstrating Observer Pattern:")
    subject = Subject()
    obs1 = ConcreteObserver("Observer1")
    obs2 = ConcreteObserver("Observer2")
    subject.attach(obs1)
    subject.attach(obs2)
    subject.notify("Event occurred!")
    subject.detach(obs1)
    subject.notify("Another event occurred!")
