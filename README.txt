pip install django

django-admin startproject mysite # 프로젝트 폴더 생성

cd ./mysite # 프로젝트 폴더로 이동

# 모델 배울 때 나옴
python manage.py makemigrations (app_name)
python manage.py migrate

python manage.py runserver # 서버 실행

cf) MTV : Model(데이터베이스) Template(보이는 부분) View(명령하는 부분)

python manage.py startapp polls # 폴더 생성
# Django에서는 application 단위로 웹페이지를 개발함


--------------------------------------------------------------------------


python manage.py shell
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# 하기 커맨드로 데이터베이스에서 Question 데이터베이스를 전부 불러옵니다.
# 아직 추가한게 없으면 [] 이렇게 빈 데이터들이 뜹니다.
>>> Question.objects.all()
<QuerySet []>

# Question에 관한 새로운 데이터를 만드는 과정입니다.
# What's new? 라는 질문 데이터를 만들어봅시다.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# 데이터를 만들었으면 데이터베이스에다가 데이터를 저장해줍시다.
>>> q.save()

# 방금 저장한 데이터의 id는 1이 됩니다.
>>> q.id
1

# 파이썬 attribute를 통해 데이터의 내용을 확인 할 수 있습니다.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# 아래처럼 데이터를 변경하고 save를 통하여 다시 데이터베이스에 업데이트 가능합니다.
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() 은 데이터베이스에서 Question에 관한 모든 데이터를 보여줍니다.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>


--------------------------------------------------------------------------

Shortcut 코드
1. Render()
2. Get_object_or_404()

--------------------------------------------------------------------------

{{ 로 시작하고 }} 닫히는 문법은 variable이라고 합니다.
{% 로 시작하고 %} 로 닫히는 문법은 tag라고 합니다.


variable은 말그대로 context에서 넘어오는 변수를 접근하는 syntax이고
tag는 tag내에 파이썬 코드를 실행 시킬 수 있는 syntax입니다.
 

고로 단순히 변수를 받아오고 싶으면 {{ }} 이걸 쓰면되고
파이썬 코드를 실행시키고 싶으시면 {% %} 하면 됩니다.
