from flask import Blueprint, request, render_template
from app import dbModule

#블루프린트(Blueprint)와 란 백엔드중
#블루프린트(Blueprint) 미리 만들어 놓은 부분을 애플리케이션에 추가하는 방식으로 대용량 애플리케이션 개발 및 유지를 크게 단순화할 수 있도록 해줍니다.
#플러거블 뷰(Pluggable View)는HTTP 메소드 별 코드 작성을 편리하게 해주는것이라서

#블루프린트를(Blueprint)사용 하게 되었습니다.
main = Blueprint('main', __name__, url_prefix='/')

def mysqld():
    #dbMoudule.py의 Database()라는 함수를 db_class에 지정해 줍니다.
    db_class = dbModule.Database()
    #sql마다 필요한 문장을 써서 넣어줍니다.
    #select*from 은 원하는 테이블의 컬럼을 전체 선택하는 것입니다.
    sql1 = "SELECT*FROM webdb.danger_rank"
    sql2 = "SELECT*FROM webdb.today"
    sql3 = "SELECT*FROM webdb.view_news"
    sql4 = "SELECT*FROM webdb.Best_news"
    #테이블내용을 모두 읽어옵니다.
    row1 = db_class.executeAll(sql1)
    row2 = db_class.executeAll(sql2)
    row3 = db_class.executeAll(sql3)
    row4 = db_class.executeAll(sql4)
    #database를 닫습니다.
    db_class.close()
    #가져온 데이터를 보내줍니다.
    return row1, row2, row3, row4

def Post():
    #dbMoudule.py의 Database()라는 함수를 db_class에 지정해 줍니다.
    db_class = dbModule.Database()
    #html의 from에서 보낸 데이터를 result에 지정해줍니다.
    result = request.form
    #view_news에서 데이터를 읽어옵니다.
    sqlread = "select id, live, star from view_news"
    starRead = db_class.executeAll(sqlread)
    #갯수를 카운트할 변수 t를 생성
    t=0
    #check라는 확인할 변수를 하나 생성합니다.
    #같은 id가 있다면 1 없다면 0으로 합니다.
    check = 0
    for star in starRead:
        if starRead[t]['id'] == int(result['title']) :
            check =1
            break;
        t= t+1

    #입력 id가 없을때 종료합니다.
    if check == 0 :
        return check

    #텅 빈상태라면
    if starRead[t]['star'] == None:
        star = int(result['stars'])
        people = 1

        #mysql에 원하는 id에 내용을 수정해 줍니다. temp = 3 이였는데 3을 2로 바꾸는 행위 입니다.
        sqlin1 = "UPDATE today_news set temp=%s, live =%s, star = %s, starset = %s where id =%s"
        db_class.execute(sqlin1, ('1', people, star, star, int(result['title'])))
        sqlin2 = "UPDATE view_news set stara = %s where id =%s"
        db_class.execute(sqlin2, (star, int(result['title'])))
        db_class.commit()

    #내용이 추가되어있는 상태라면
    else:
        #별점에 대한 평균을 구해서 starset이라는 변수에 넣어줍니다.
        star = int(starRead[t]['star']) + int(result['stars'])
        people = int(starRead[t]['live']) + 1
        starset = float(round(star/people, 1))

        #mysql에 원하는 id에 내용을 수정해 줍니다. temp = 3 이였는데 3을 2로 바꾸는 행위 입니다.
        sqlin = "UPDATE today_news set temp=%s, live =%s, star = %s, starset = %s where id =%s"
        db_class.execute(sqlin, ('1', people, star, starset, int(result['title'])))
        sqlin2 = "UPDATE view_news set stara = %s where id =%s"
        db_class.execute(sqlin2, (starset, int(result['title'])))
        db_class.commit()

    db_class.close()
    #check로 보내줍니다.
    #1을 보내줍니다 있어서 변경 되었기때문에 1 입니다.
    return check

@main.route('/', methods=['POST', 'GET'])
def index():
    check =0
    if request.method == 'POST':
        check = Post()

    row1, row2, row3, row4= mysqld()
    #template 폴더에 있는 html에 데이터 resultData,라는 변수를 보내줍니다.
    return render_template('/main.html',
                           resultData=row1[0],
                           today_Data=row2,
                           Show_news=row3,
                           Best_news=row4,
                           check_in = check)