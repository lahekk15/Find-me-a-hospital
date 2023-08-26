# views.py
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ReportForm
import os

def complain(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            aadhaar_number = form.cleaned_data['aadhaar_number']
            pincode = form.cleaned_data['pincode']
            mobile_number = form.cleaned_data['mobile_number']
            severity = form.cleaned_data['severity']
            report_image = form.cleaned_data['report_image']

            # Save the uploaded image to media directory
            report_image_path = os.path.join(settings.MEDIA_ROOT, report_image.name)
            with open(report_image_path, 'wb') as destination:
                for chunk in report_image.chunks():
                    destination.write(chunk)

            return redirect('hospital_portal', name=name, aadhaar_number=aadhaar_number, pincode=pincode, mobile_number=mobile_number, severity=severity, report_image=report_image.name)
    else:
        form = ReportForm()

    return render(request, 'complain.html', {'form': form})

def hospital_portal(request, name, aadhaar_number, pincode, mobile_number, severity, report_image):
    context = {
        'name': name,
        'aadhaar_number': aadhaar_number,
        'pincode': pincode,
        'mobile_number': mobile_number,
        'severity': severity,
        'report_image': report_image,
    }
    return render(request, 'hospital_portal.html', context)
