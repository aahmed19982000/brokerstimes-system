<<<<<<< HEAD
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from datetime import date
from tasks.models import Task
from django.utils import timezone
from django.db.models import Count, Q , F
from django.utils.timezone import localdate



#صفحة لوحة التحكم 
@login_required(login_url=reverse_lazy('login'))
def dashboard_view(request):
    today = timezone.now().date()

    # عدد المهام الكلي
    total_tasks = Task.objects.count()

    # عدد المهام المكتملة
    completed_tasks = Task.objects.filter(status__in=['done','upload']).count()
    # عدد المهمام المنشورة
    completed_publish = Task.objects.filter(status__in=[ 'publish']).count()

    # نسبة التقدم للكل
    progress_percent = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0


    # عدد المهام المتبقية = أي حاجة غير "done"
    pending_tasks = Task.objects.exclude(status='done').count()

    # عدد المهام المُضافة اليوم
    today_tasks = Task.objects.filter(publish_date=today).count()

    # تجميع المهام لكل كاتب مع حساب عدد المكتملة منهم
    writers_progress = Task.objects.values(username=F('writer__username')).annotate(
    total_tasks=Count('id'),
    completed_tasks=Count('id', filter=Q(status__in=['done', 'upload', 'publish']))
)

    # حساب نسبة الإنجاز لكل كاتب
    for writer in writers_progress:
        total = writer['total_tasks']
        completed = writer['completed_tasks']
        writer['progress_percent'] = int((completed / total) * 100) if total > 0 else 0

    # جدول مصغر لآخر المهام
    latest_tasks = Task.objects.select_related('writer').order_by('-created_at')[:5]

    # المهام المجدولة لليوم
    today_task_list = Task.objects.filter(publish_date=today)

    # المهام المتأخرة (تاريخ نشرها قبل اليوم + لم تُكتمل)
    overdue_tasks = Task.objects.filter( publish_date__lt=today).exclude(status__in=['done', 'publish','upload'])

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'completed_publish': completed_publish,
        'pending_tasks': pending_tasks,
        'today_tasks': today_tasks,
        'progress_per_writer': writers_progress,
        'latest_tasks': latest_tasks,
        'today_task_list': today_task_list,
        'overdue_tasks': overdue_tasks,
        'progress_percent' : progress_percent,
    }

    return render(request, 'home/dashboard.html', context)
# views.py


@login_required
def employee_dashboard(request):
    user = request.user
    tasks = Task.objects.filter(writer=user)
    today = localdate()  # بدل date.today()

    total = tasks.count()
    completed = tasks.filter(status__in=['done','upload']).count()
    completed_publish= tasks.filter(status__in=['publish']).count()
    pending = total - completed
    progress_percent = int((completed / total) * 100) if total > 0 else 0

    # ✅ المهام المطلوبة اليوم
    todays_tasks = tasks.filter(publish_date=today)

    # ✅ المهام المؤخرة (قبل اليوم ولم تُنجز)
    overdue_tasks = tasks.filter(publish_date__lt=today).exclude(status__in=['done', 'publish','upload'])


    return render(request, 'home/employee_dashboard.html', {
        'total_tasks': total,
        'completed_tasks': completed,
        'completed_publish' : completed_publish,
        'pending_tasks': pending,
        'progress_percent': progress_percent,
        'todays_tasks': todays_tasks,
        'overdue_tasks': overdue_tasks,
        
=======
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy
from datetime import date
from tasks.models import Task
from django.utils import timezone
from django.db.models import Count, Q , F
from django.utils.timezone import localdate



#صفحة لوحة التحكم 
@login_required(login_url=reverse_lazy('login'))
def dashboard_view(request):
    today = timezone.now().date()

    # عدد المهام الكلي
    total_tasks = Task.objects.count()

    # عدد المهام المكتملة
    completed_tasks = Task.objects.filter(status__in=['done','upload']).count()
    # عدد المهمام المنشورة
    completed_publish = Task.objects.filter(status__in=[ 'publish']).count()

    # نسبة التقدم للكل
    progress_percent = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0


    # عدد المهام المتبقية = أي حاجة غير "done"
    pending_tasks = Task.objects.exclude(status='done').count()

    # عدد المهام المُضافة اليوم
    today_tasks = Task.objects.filter(publish_date=today).count()

    # تجميع المهام لكل كاتب مع حساب عدد المكتملة منهم
    writers_progress = Task.objects.values(username=F('writer__username')).annotate(
    total_tasks=Count('id'),
    completed_tasks=Count('id', filter=Q(status__in=['done', 'upload', 'publish']))
)

    # حساب نسبة الإنجاز لكل كاتب
    for writer in writers_progress:
        total = writer['total_tasks']
        completed = writer['completed_tasks']
        writer['progress_percent'] = int((completed / total) * 100) if total > 0 else 0

    # جدول مصغر لآخر المهام
    latest_tasks = Task.objects.select_related('writer').order_by('-created_at')[:5]

    # المهام المجدولة لليوم
    today_task_list = Task.objects.filter(publish_date=today)

    # المهام المتأخرة (تاريخ نشرها قبل اليوم + لم تُكتمل)
    overdue_tasks = Task.objects.filter( publish_date__lt=today).exclude(status__in=['done', 'publish','upload'])

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'completed_publish': completed_publish,
        'pending_tasks': pending_tasks,
        'today_tasks': today_tasks,
        'progress_per_writer': writers_progress,
        'latest_tasks': latest_tasks,
        'today_task_list': today_task_list,
        'overdue_tasks': overdue_tasks,
        'progress_percent' : progress_percent,
    }

    return render(request, 'home/dashboard.html', context)
# views.py


@login_required
def employee_dashboard(request):
    user = request.user
    tasks = Task.objects.filter(writer=user)
    today = localdate()  # بدل date.today()

    total = tasks.count()
    completed = tasks.filter(status__in=['done','upload']).count()
    completed_publish= tasks.filter(status__in=['publish']).count()
    pending = total - completed
    progress_percent = int((completed / total) * 100) if total > 0 else 0

    # ✅ المهام المطلوبة اليوم
    todays_tasks = tasks.filter(publish_date=today)

    # ✅ المهام المؤخرة (قبل اليوم ولم تُنجز)
    overdue_tasks = tasks.filter(publish_date__lt=today).exclude(status__in=['done', 'publish','upload'])


    return render(request, 'home/employee_dashboard.html', {
        'total_tasks': total,
        'completed_tasks': completed,
        'completed_publish' : completed_publish,
        'pending_tasks': pending,
        'progress_percent': progress_percent,
        'todays_tasks': todays_tasks,
        'overdue_tasks': overdue_tasks,
        
>>>>>>> d7023bb44d462afe13064eb16464741bb8208045
    })