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

        return {
            "completed": TaskService.get_completed_tasks(tasks_list),
            "overdue":  TaskService.get_overdue_tasks(tasks_list),
            "today": TaskService.get_today_tasks(tasks_list)
        }
