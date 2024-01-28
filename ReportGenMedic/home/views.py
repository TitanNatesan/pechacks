from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import patient
from rest_framework import status
from .serializers import PatientSerializer


@api_view(['GET'])
def patient_list(request):
    patients = patient.objects.all()
    patient_data = []

    for p in patients:
        patient_data.append({
            'id': p.id,
            'name': p.name,
            'phone': str(p.phone),
            'email': p.email,
            'report_id': p.report.id if p.report else None,
            'report_url': p.report.report.url if p.report else None,
            'src_url': p.report.src.url if p.report else None,
        })

    return Response({'patients': patient_data})

@api_view(['GET'])
def patient_search(request, name):
    patients = patient.objects.filter(name__icontains=name)
    patient_data = []

    for p in patients:
        patient_data.append({
            'id': p.id,
            'name': p.name,
            'phone': str(p.phone),
            'email': p.email,
            'report_id': p.report.id if p.report else None,
            'report_url': p.report.report.url if p.report else None,
            'src_url': p.report.src.url if p.report else None,
        })

    return Response({'patients': patient_data})



@api_view(['POST'])
def upload_image(request):
    # Get data from the request
    name = request.data.get('name')
    phone = request.data.get('phone')
    email = request.data.get('email')
    image = request.data.get('image')

    # Check if the user already exists
    existing_patient = patient.objects.filter(name=name, phone=phone, email=email).first()

    if existing_patient:
        # Update the existing user's information
        existing_patient.report.src = image
        existing_patient.report.save()
        existing_patient.save()

        serializer = PatientSerializer(existing_patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        # Create a new user
        new_patient = patient.objects.create(name=name, phone=phone, email=email)
        new_patient.report.src = image
        new_patient.report.save()
        new_patient.save()

        serializer = PatientSerializer(new_patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
