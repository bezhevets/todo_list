from django.db.models import F
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"
    queryset = Task.objects.all().order_by(F("is_completed"), "-created_time")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:home")
    template_name = "tasks/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:home")
    template_name = "tasks/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:home")
    template_name = "tasks/task_confirm_delete.html"


class TaskCompletedView(generic.View):
    model = Task
    fields = ("is_completed",)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)

        task.is_completed = not task.is_completed
        task.save()

        return redirect("tasks:home")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag_list")
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag_list")
    template_name = "tasks/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag_list")
    template_name = "tasks/tag_confirm_delete.html"
