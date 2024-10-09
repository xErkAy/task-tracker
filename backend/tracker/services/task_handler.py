from tracker.models import Task, Tag


class TaskHandler:
    @staticmethod
    def create(data: dict) -> Task:
        obj = Task.objects.create(
            name=data['name'],
            description=data['description'],
            author_id=data['author']['id'],
            performer_id=data['performer']['id'],
            due_date=data['due_date'],
        )

        tags_id = [i['id'] for i in data['tags']]
        tags = Tag.objects.filter(id__in=tags_id)
        obj.tags.set(tags)

        return obj

    @staticmethod
    def update(instance: Task, data: dict) -> Task:
        instance.status = data['status']

        if list(data.keys()) != ['status']:
            instance.name = data['name']
            instance.description = data['description']
            instance.author_id = data['author']['id']
            instance.performer_id = data['performer']['id']
            instance.due_date = data['due_date']

            tags_id = [i['id'] for i in data['tags']]
            tags = Tag.objects.filter(id__in=tags_id)
            instance.tags.clear()
            instance.tags.set(tags)

        instance.save()

        return instance
