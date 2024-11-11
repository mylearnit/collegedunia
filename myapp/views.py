from django.shortcuts import render
import json
from django.http import JsonResponse
from myapp.models import College
from django.db.models import Count

# Create your views here.
def home(request):
    streams=College.objects.values('stream_data_name').annotate(c=Count('id'))
    sub_streams = College.objects.values('sub_stream_data_id').annotate(c=Count('id'))
    courses = College.objects.values('course_id').annotate(c=Count('id'))
    print(list(streams))
    return JsonResponse({'total':College.objects.count(),'streams':list(streams),'sub_streams':list(sub_streams),'courses':list(courses)})

def parse(request):
    # College.objects.all().delete()
    for i in range(24639):  
        try:
            with open(f"college_json/{i}.json") as f:
                d = json.load(f)
        except:
            continue
        if "status" in d:
            continue
        
        
        for j, c in enumerate(d["course_data"]["courses"]):
            sub_stream_data_name=''
            sub_stream_data_id=None
            if 'sub_stream_data' in c:
                sub_stream_data_name= c['sub_stream_data']['name']
                sub_stream_data_id=c['sub_stream_data']['id']
            x,created=College.objects.get_or_create(
                code = i,
                course_id=c['course_id'], 
                # slug=c['slug'],             
                defaults={
                    'stream_data_name':c['stream_data']['name'],
                    'stream_data_id':c['stream_data']['id'],
                    'display_name':c['display_name'],
                    'sub_stream_data_name':sub_stream_data_name,
                    'sub_stream_data_id':sub_stream_data_id,
                    # 'short_head':c['short_head'],
                    'categories': c['categories'],
                    'forum_data': c['forum_data'],
                    'qna_data': c['qna_data'],
                    'offered_by': c['offered_by'],

                }
            )
            print(created,i)
            
        # break
    # slug = models.CharField(max_length=200)
    # duration_year	= models.CharField(max_length=200)
    # duration_month 	= models.CharField(max_length=200)

    # level=	models.CharField(max_length=200)
    # course_type	= models.CharField(max_length=200)
    # degree_could_be	= models.CharField(max_length=200)
    # short_admission 	= models.CharField(max_length=200, null=True)
    # qna_count 	= models.CharField(max_length=200, null=True)
    # admission_criteria =models.CharField(max_length=200, null=True)
    # admission_admission_post_id= models.CharField(max_length=200, null=True)
    # admission_admission_post_title= models.CharField(max_length=200, null=True)
    
    # admission_admission_post_name= models.CharField(max_length=200, null=True)
    
    # admission_display_head= models.CharField(max_length=200, null=True)
    # admission_admission_start_date= models.CharField(max_length=200, null=True)
    # admission_admission_end_date= models.CharField(max_length=200, null=True)
    # course_rating = models.CharField(max_length=200, null=True)
    # reviews_count = models.IntegerField(null=True)
    
    # url = models.CharField(max_length=200, null=True)
    
    # qna_link = models.CharField(max_length=200, null=True)
    # course_tag_id= models.IntegerField(null=True)
    # fees_data_amount= models.CharField(max_length=200, null=True)
    # fees_data_text= models.CharField(max_length=200, null=True)
    # fees_data_is_tentative= models.CharField(max_length=200, null=True)
    # fees_data_priority_category= models.CharField(max_length=200, null=True)
    # type = models.CharField(max_length=200, null=True)
    # stream_id= models.IntegerField(null=True)
    # course_id= models.IntegerField(null=True)
    # course_tag = models.CharField(max_length=200, null=True)
    # available_seats = models.CharField(max_length=200, null=True)
    # exams=models.ManyToManyField(Exam)
    # courses_count= models.IntegerField(null=True)
    # eligibility = models.CharField(max_length=200, null=True)
    # streams=models.ManyToManyField(Stream)
    
    # admission_guide_link = models.CharField(max_length=200, null=True)
    # cutoff_year = models.CharField(max_length=200, null=True)
    # cutoff_course_name = models.CharField(max_length=200, null=True)
    # cutoff_course_id = models.CharField(max_length=200, null=True)
    # cutoff_cutoff = models.CharField(max_length=200, null=True)
    # cutoff_exam = models.CharField(max_length=200, null=True)
    # cutoff_cutoff_type = models.CharField(max_length=200, null=True)
    # duration = models.CharField(max_length=200, null=True)
    # is_discontinued= models.IntegerField(null=True)
    # ranking_stats_key_college_id= models.IntegerField(null=True)
    # ranking_stats_key_stream_id= models.IntegerField(null=True)
    # ranking_stats_key_agency_id= models.IntegerField(null=True)
    # ranking_stats_key_data_key= models.CharField(max_length=200, null=True)
    
    
    return JsonResponse(c)