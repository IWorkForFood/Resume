from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
import os
from django.views import View
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from weasyprint import HTML, CSS
from django.template.loader import render_to_string
from RGenerator.forms import CVForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import admin
from .models import Documents

admin.site.register(Documents)

# Create your views here.

def generate_pdf(request):
    #pdf_response = render(request, 'pattern_resume.html', {'joke':'ахаха'})
    old_post = request.session.get('_old_post', {})
    old_post['name'] += " "
    old_post['img_url'] = request.session.get('img_url', {})
    old_post['age'] = request.session.get('age', {})
    old_post['skills'] = request.session.get('skills', {})
    request.session['_old_post'] = old_post

    css = CSS(string='@page { margin: 0; }')
    context = old_post
    html_content = render_to_string('download.html', context, request=request)
    pdf = HTML(string=html_content).write_pdf(stylesheets=[css]) # write_pdf() - генерирует pdf на основе HTML

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_name = f"pdf_{timestamp}.pdf"

    with open(settings.MEDIA_ROOT+"/pdf-files/"+pdf_name, 'wb') as file:
        file.write(pdf)

    new_path = Documents(title = pdf_name, cover = settings.MEDIA_ROOT+"/pdf-files/"+pdf_name)
    new_path.save()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachement; filename="home_pdf.pdf"'
    return response

class UseCVForm(View):
    def get(self, request):
        cv_form = CVForm()
        documents = Documents.objects.all()
        return render(request, 'info_form.html', context={'cv_form': cv_form, 'documents':documents})

    def post(self, request):
        documents = Documents.objects.all()
        cv_form = CVForm(request.POST)
        if cv_form.is_valid():  # возвращает либо true, если данные успешно пройдут инициализацию, либо false в ином случ
            try:
                image = request.FILES['profile_photo']
                fs = FileSystemStorage(location=settings.MEDIA_ROOT+"/img")
                filename = fs.save(image.name, image)
                img_url = os.path.join(settings.MEDIA_URL,"img/",filename)
                request.session['img_url'] = img_url
            except Exception:
                pass

            request.session['skills'] = None
            request.session['age'] = None
            request.session['_old_post'] = request.POST
            if request.POST.get('birthyear', '').isdigit() and request.POST.get('birthmonth', '').isdigit() and request.POST.get('birthday', '').isdigit():
                current_date = datetime.now()
                birth_date = datetime(int(request.POST.get('birthyear', '')), int(request.POST.get('birthmonth', '')), int(request.POST.get('birthday', '')))
                age = current_date.year - birth_date.year - (
                        (current_date.month, current_date.day) < (birth_date.month, birth_date.day))
                request.session['age'] = age
            if cv_form.cleaned_data['skill8']:
                skills = cv_form.cleaned_data['skill8'].split(',')
                request.session['skills'] = skills

            return redirect('resume_pattern')
        return render(request, 'info_form.html', context={'cv_form': cv_form, 'documents':documents})

def resume_pattern(request):
    old_post = request.session.get('_old_post', {})
    old_post['name'] += " "
    old_post['img_url'] = request.session.get('img_url', {})
    old_post['age'] = request.session.get('age', {})
    old_post['skills'] = request.session.get('skills', {})
    request.session['_old_post'] = old_post
    return render(request, 'pattern_resume.html', context={'old_post': old_post})

def download(request):
    context = request.session.get('_old_post', {})
    return render(request, 'download.html', context=context)
