from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

MAX_FILE_SIZE = 1 * 1024 * 1024  # 1 МБ

def upload_file_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return HttpResponseBadRequest("Файл не был загружен.")
        if uploaded_file.size > MAX_FILE_SIZE:
            return HttpResponseBadRequest("Файл превышает 1 МБ.")
        # можно сохранить файл или просто подтвердить
        return HttpResponse("Файл принят.")
    return render(request, 'upload.html')
