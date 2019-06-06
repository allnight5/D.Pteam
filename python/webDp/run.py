# file name : run.py
# pwd : /project_name/run.py

from app import app
#서버를 실행 시키기 위해서 필요함
#port 번호는 열고 싶은곳에서 열어야하며
#host 0.0.0.0의 경우 모든 곳에서 들어올수있따는 것입니다.
#debug는 True로 하면 내용을 새롭게 저장했을때 내용이 바뀌게 됩니다.
app.run(host='0.0.0.0', debug=True,port=9000)