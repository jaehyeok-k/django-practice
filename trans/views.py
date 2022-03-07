from django.shortcuts import render
import googletrans
from googletrans import Translator

# Create your views here.
def index(request): 

    context = {"ndict": googletrans.LANGUAGES}
    if request.method == "POST":
        text = request.POST.get("bf")
        fr = request.POST.get("fr")
        to = request.POST.get("to")
        translator = Translator()
        if text:
            inter = translator.translate(text, src=fr, dest=to)
            context.update({
                "bf" : text,
                "fr" : fr,
                "to" : to,
                "af" : inter.text
            })
    return render(request, "trans/index.html", context)

