from flask import Blueprint, request, render_template, flash, redirect, url_for
from app import dbModule

from flask import current_app as current_app
main = Blueprint('main', __name__, url_prefix='/')

def mysqld():
    db_class = dbModule.Database()
    sql1 = "SELECT*FROM webdb.danger_rank"
    sql2 = "select*from webdb.today"
    sql3 = "select*from webdb.today_news"
    #db_class.execute(sql2, 3)
    #db_class.commit()
    #sql2 = "SELECT id, 서울 FROM webdb.danger_rank"
    #row2 = db_class.executeAll(sql2)
    row1 = db_class.executeAll(sql1)
    row2 = db_class.executeAll(sql2)
    row3 = db_class.executeAll(sql3)

    db_class.close()
    return row1, row2, row3

def Post():
    db_class = dbModule.Database()
    result = request.form
    sqlread = "select live, star from today_news"
    starRead = db_class.executeOne(sqlread)

    print(int(result['stars']))
    if starRead['star'] == None:
        star = int(result['stars'])
        people = 1
        sqlin = "UPDATE today_news set temp=%s, live =%s, star = %s where id =%s"
        db_class.execute(sqlin, ('1', people, star, 1))
        db_class.commit()
    else:
        star = int(starRead['star']) + int(result['stars'])
        people = int(starRead['live']) + 1
        sqlin = "UPDATE today_news set temp=%s, live =%s, star = %s where id =%s"
        db_class.execute(sqlin, ('1', people, star, 1))
        db_class.commit()

    db_class.close()

@main.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        Post()

    row1, row2, row3= mysqld()
    #a = row3[0]['star']
    #b = row3[0]['live']
    #star = round(a/b, 1)
    #template 폴더에 있는 html에 데이터 resultData,라는 변수를 보내줍니다.
    return render_template('/main.html',
                           resultData=row1[0],
                           today_Data=row2,
                           today_news=row3 )

'''
# SELECT 함수 예제
@main.route('/', methods=['GET'])
def select():
    db_class = dbModule.Database()
    sql = "SELECT 서울, 부산 FROM webdb.danger_rank"
    sql2 = "UPDATE webdb.danger_rank \
                SET 서울='%s'"
    db_class.execute(sql2, 7)
    db_class.commit()
    sql2 = "SELECT id, 서울 \
                FROM webdb.danger_rank"
    row2 = db_class.executeAll(sql2)
    row = db_class.executeAll(sql)
    print(row)

    return render_template('/test.html',
                           resultData=row[0],
                           resultUPDATE=row2[0])
# UPDATE 함수 예제
@main.route('/application/update', methods=['GET'])
def update():
    db_class = dbModule.Database()
    sql = "UPDATE webdb.danger_rank \
                SET 서울='%s'"
    db_class.execute(sql, 6)
    db_class.commit()
    sql = "SELECT id, 서울 \
                FROM webdb.danger_rank"
    row = db_class.executeAll(sql)
    return render_template('/test.html',
                           resultData=None,
                           resultUPDATE=row[0])
'''