1. 프로젝트 뼈대 만들기

   - `django-admin startproject *`
   - `python manage.py startapp *`
   - `setting.py` HOSTS 추가 및 INSTALLED_APPS에  생성한 `app` 추가
   - `python manage.py migrate` 기본 테이블 생성 (이 후 변경사항 반영하는 명령어)
   - `python manage.py runserver` 진행상황 웹서버로 확인
   - `python manage.py createsuperuser` 관리자 생성

2. `url` 및 `view` 설정

   - 프로젝트 폴더 내 `urls.py` 에서 각 `app` 으로 넘어가는 **url** 과 `admin` **url** 설정
   - 각 `app` 의 urls 와 view 설정
     - ` url` 에서 `view` 로 넘긴 후, `view`에서  처리할 데이터를 서버로 전송
       - 이때 `render` 함수를 이용하여 `html` 로 넘기는게 일반적

3. CRUD 구성

   - `Create`

     - 카테고리 추가

       - 하나의 맛집이 하나의 카테고리에 속하는 방법
       - `models.py` 카테고리 생성
         - `makemigrations` `migrate` 진행하여 데이터베이스 생성

       - `categoryCreate.html` 에 `./create` 설정을 위해 `urls.py`에서 생성
       - `views` 함수로 지정하여 넘겼으니, `views.py`에 해당 함수를 만들고 Create기능 생성
       - Create 시의 데이터를 `models.py`에 `Category` 함수를 이용하여 넘기고 해당 데이터를 DB에 저장 후 URL `name` 이나, viewname을 통해 다시 URL로 되돌려줌

   - `Read`

     - 위에서 생성 된 데이터를 다시 `html`로 전달

     - `Category` 모델로 생성 된 데이터를 가져오기 위해 `views.py` 수정

       ```python
       def index(request):
           categories = Category.objects.all() #모든 객체 가져오기
           content = {'categories': categories} #딕셔너리에 담기
           return render(request, 'shareRes/index.html', content) #
       ```

       

