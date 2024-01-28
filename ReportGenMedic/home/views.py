from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Patient
from rest_framework import status
from .serializers import PatientSerializer

@api_view(['GET'])
def patient_list(request):
    patients = Patient.objects.all()
    patient_data = []

    for p in patients:
        patient_data.append({
            'id': p.username,
            'name': p.name,
            'username': p.username,
            'phone': str(p.phone),
            'email': p.email,
            'report_id': p.report.id if p.report else None,
            'report_url': p.report.report.url if p.report else None,
            'src_url': p.report.src.url if p.report else None,
        })

    return Response({'patients': patient_data})

@api_view(['GET'])
def patient_search(request, name):
    patients = Patient.objects.filter(name__icontains=name)
    patient_data = []

    for p in patients:
        patient_data.append({
            'id': p.username,
            'name': p.name,
            'username': p.username,
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
    username = request.data.get('username')
    phone = request.data.get('phone')
    email = request.data.get('email')
    image = request.data.get('image')

    # Check if the user already exists
    existing_patient = Patient.objects.filter(name=name, username=username, phone=phone, email=email).first()

    if existing_patient:
        # Update the existing user's information
        existing_patient.report.src = image
        existing_patient.report.save()
        existing_patient.save()

        serializer = PatientSerializer(existing_patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        # Create a new user
        new_patient = Patient.objects.create(name=name, username=username, phone=phone, email=email)
        new_patient.report.src = image
        new_patient.report.save()
        new_patient.save()

        serializer = PatientSerializer(new_patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def login(request):
    if request.method == "POST":
        data = request.data
        user = data['username']
        password = data['password']
        user = Patient.objects.get(username=user)
        return Response("Success")