from django.shortcuts import render
from .forms import AnalysisForm
from attention_feature.get_features import get_analysis
from attention_feature.utility import format_data
import os
import json

def index(request):
    return render(request, template_name='index.html')


def video_upload(request):
    if request.method == 'POST':
        form = AnalysisForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            result_list = get_analysis(os.getcwd()+"/media/"+str(video))
            formatted_data = format_data(result_list)
            return render(request, template_name='index.html', context={"analysis": json.dumps(formatted_data)})

    video_upload_form = AnalysisForm()
    return render(request, template_name='upload.html', context={
        "form": video_upload_form,
    })
