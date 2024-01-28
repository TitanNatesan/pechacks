from rest_framework import serializers
from .models import Patient, XrayReport

class XrayReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = XrayReport
        fields = ['report', 'src']

class PatientSerializer(serializers.ModelSerializer):
    report = XrayReportSerializer()

    class Meta:
        model = Patient
        fields = ["username",'name', 'phone', 'email', 'report']

    def create(self, validated_data):
        # Extract report data from validated data
        report_data = validated_data.pop('report')

        # Create XrayReport instance
        report_instance = XrayReport.objects.create(**report_data)

        # Create patient instance with the nested XrayReport instance
        patient_instance = Patient.objects.create(report=report_instance, **validated_data)

        return patient_instance
