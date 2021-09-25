from django.db import models
from django.db.models.deletion import SET_NULL

Gender_choice = [
    ("M", "M"),
    ("F", "F")
]

Spec = [
    ("Back end", "Back end"),
    ("Front end", "Front end"),
    ("Web design", "Web design"),
    ("SMM", "SMM"),
]
LEVEL = [
    ("JUNIOR", "JUNIOR"),
    ("MIDDLE", "MIDDLE"),
    ("SENIOR", "SENIOR"),
]

Spec_Choice_Course = [
    ("Python", "Python"),
    ("Framework Django", "Framework Django"),
    ("HTML", "HTML"),
    ("CSS", "CSS"),
    ("JS", "JS"),
    ("React", "React"),
    ("Figma", "Figma"),
    ("Photoshop", "Photoshop")
]

Status = [
    ("No", "No"),
    ("FULL", "FULL"),
    ("PART", "PART")
]


Time_Choice = [
        ("11:30 - 13:00", "11:30 - 13:00"),
        ("14:00 - 15:30", "14:00 - 15:30"),
        ("15:30 - 17:00", "15:30 - 17:00"),
        ("17:00 - 18:30", "17:00 - 18:30"),
        ("18:30 - 20:00", "18:30 - 20:00")
    ]

Room_Choice = [
    ("First room", "First room"),
    ("Second room", "Second room"),
    ("Third room", "Third room"),
    ("Co-working", "Co-working")
]

Payment_choice = [
    ("PAID", "PAID"),
    ("UNPAID", "UNPAID"),
]

Filter = [
    ('lesson', 'lesson'),
    ('studentFilter', 'studentFilter'),
    ('mentorFilter', 'mentorFilter',),
    ('group', ' groupFilter'),
]

Filter_lesson = [
    ('lesson', 'lesson'),
    ('studentFilter', 'studentFilter'),
    ('mentorFilter', 'mentorFilter',),
    ('group', ' groupFilter'),
]


class Mentor(models.Model):
    fullname = models.CharField(max_length=90)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=Gender_choice, default="M")
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    spec = models.CharField(max_length=90, choices=Spec, default='Spec_Choices')

    def __str__(self):
        return self.fullname


class Courses(models.Model):
    spec = models.PositiveIntegerField(choices=Spec, default="Python")
    mentor = models.CharField(max_length=45, null=True, blank=True)
    start = models.DateField(blank=True, null=True)
    finish = models.DateField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(choices=Status, default="No")

    def __str__(self):
        return self.spec


class Group(models.Model):
    name = models.CharField(max_length=25)
    specification = models.CharField(max_length=23, choices=Spec, default="Back end")
    developer_tech = models.CharField(max_length=30, choices=Spec_Choice_Course, default="Front end")
    mentor = models.ForeignKey(Mentor, on_delete=SET_NULL, blank=True, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=13, choices=Time_Choice, default="11:30 - 13:00")
    room = models.CharField(max_length=50, choices=Room_Choice, default="First")
    course = models.CharField(max_length=50, choices=Spec_Choice_Course, default='Python', null=True, blank=True)
    group = models.ForeignKey(Group,  on_delete=SET_NULL, null=True, blank=True)
    student_qty = models.PositiveIntegerField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    total = models.CharField(max_length=90)
    status = models.CharField(max_length=8, choices=Status, default="Planned")

    def __str__(self):
        return self.course


class Student(models.Model):
    fullname = models.CharField(max_length=50, verbose_name='fullname')
    age = models.PositiveIntegerField(verbose_name='age')
    gender = models.CharField(max_length=1, choices=Gender_choice, default='M')
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=SET_NULL, blank=True, null=True)
    payment = models.CharField(max_length=50, choices=Payment_choice, default='No')

    def __str__(self):
        return self.fullname






