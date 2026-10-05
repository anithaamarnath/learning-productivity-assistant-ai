from datetime import date


class TaskService:
    @staticmethod
    def get_completed_tasks(tasks_list):
        return [
            task for task in tasks_list
            if task.is_completed()
        ]

    @staticmethod
    def get_overdue_tasks(tasks_list):
        return [
            task for task in tasks_list
            if task.is_overdue() and not task.is_completed()
        ]

    @staticmethod
    def get_today_tasks(tasks_list):
        return [
            task for task in tasks_list
            if task.due_date == date.today()
        ]

    @staticmethod
    def get_daily_summary(tasks_list):
        print("\nToday's Tasks:")
        for task in TaskService.get_today_tasks(tasks_list):
            print(
                f"Task: {task.title},"
                f"Status: {task.status},"
                f"Due Date: {task.due_date}"
            )

        print("\nOverdue Tasks:")
        for task in TaskService.get_overdue_tasks(tasks_list):
            print(
                f"Overdue Task: {task.title},"
                f"Status: {task.status},"
                f"Due Date: {task.due_date}"
            )

        print("\nCompleted Tasks:")
        for task in TaskService.get_completed_tasks(tasks_list):
            print(
                f"Completed Task: {task.title},"
                f"Status: {task.status},"
                f"Due Date: {task.due_date}"
            )
