from django.contrib import admin
from .models import User, Student, Subject, Question, Answer, Quiz,StudentAnswer, TakenQuiz
# # Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(StudentAnswer)
admin.site.register(TakenQuiz)


