from django.shortcuts import redirect, render
from .models import Topic, Choices
from django.utils import timezone

# Create your views here.
def create(request):
    if request.method == "POST":
        s = request.POST.get("sub")
        c = request.POST.get("con")
        names = request.POST.getlist("chname")
        files = request.FILES.getlist("chpic")
        comms = request.POST.getlist("chcom")
        if len(names) > 1:
            t = Topic(subject=s, maker=request.user, content=c, pubdate=timezone.now())
            t.save()
            for i,j,k in zip(names,files,comms):
                Choices(topic=t, chname=i, chpic=j, chcom=k).save()
            return redirect("vote:index")

    return render(request, "vote/create.html")

def cancel(request, tpk):
    t = Topic.objects.get(id=tpk)
    u = request.user
    if u in t.voter.all():
        t.voter.remove(u)
        u.choices_set.get(topic=t).choicer.remove(u)
    return redirect("vote:detail", tpk)


def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        # 토픽에 투표하지 않았던 사람들만 종속문장 실행됨
        t.voter.add(request.user)
    
        cpk = request.POST.get("ch")
        c = Choices.objects.get(id=cpk)
        c.choicer.add(request.user)

    return redirect("vote:detail", tpk)




def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choices_set.all()
    context = {
        "t" : t,
        "cset" : c
    }
    return render(request, 'vote/detail.html', context)

def index(request):
    t = Topic.objects.all()
    t = t.order_by("-pubdate")
    context = {
        "tset" : t
    }
    return render(request, 'vote/index.html', context)