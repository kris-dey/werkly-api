from rest_framework import serializers
from . import models

class JobsListSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = models.Job
        fields = ('id', 'employer_id', 'details', 'status', 'right_swipes', 'tags')

    def get_details(self, obj):
        details = {
            'id': obj.details.id,
            'job_name': obj.details.job_name,
            'date': obj.details.date,
            'time_from': obj.details.time_from,
            'time_to': obj.details.time_to,
            'pay_per_hour': obj.details.pay_per_hour,
            'address': obj.details.address,
            'description': obj.details.description,
            'required_experience': obj.details.required_experience
        }
        return details

    def get_status(self, obj):
        status = {
            'id': obj.status.id,
            'accepted': obj.status.accepted,
            'completed': obj.status.completed,
            'pay': obj.status.pay,
            'worker_time_in': obj.status.worker_time_in,
            'worker_time_out': obj.status.worker_time_out,
            'amount_paid': obj.status.amount_paid
        }
        return status

class WorkerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ('right_swipes',)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('tag',)

class DetailsSerializer(serializers.ModelSerializer):
    # tags = TagsSerializer(many=True)
    class Meta:
        model = models.Details
        fields = ('id', 'job_name', 'date', 'time_from', 'time_to', 'duration', 'pay_per_hour', 'address', 'description', 'required_experience')

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = ('id', 'accepted', 'completed', 'pay', 'worker_time_in', 'worker_time_out', 'amount_paid')

class JobsCreationSerializer(serializers.ModelSerializer):
    details = DetailsSerializer(many=False)
    status = StatusSerializer(many=False)
    tags = TagsSerializer(many=True)
    class Meta:
        model = models.Job
        fields = ('id', 'employer_id', 'details', 'status', 'right_swipes', 'tags')

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        status_data = validated_data.pop('status')
        tag_data = validated_data.pop('tags')
        job_object = models.Job.objects.create(**validated_data)
        for obj in tag_data:
            job_object.tags.add(obj)
        models.Details.objects.create(job=job_object, **details_data)
        models.Status.objects.create(job=job_object, **status_data)

        return job_object
