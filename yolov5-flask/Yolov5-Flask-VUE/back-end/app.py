import datetime
import logging as rel_log
import os
import shutil
from datetime import timedelta
from flask import *
from processor.AIDetector_pytorch import Detector
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash


import core.main

UPLOAD_FOLDER = r'./uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg'])
app = Flask(__name__)
app.secret_key = 'secret!'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 配置mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:fengyunjia@127.0.0.1:3306/object_detection'  # mysql://username:password@hostname/database
# 是否动态修改 如为True 则会消耗性能 且改接口以后会被弃用 不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

werkzeug_logger = rel_log.getLogger('werkzeug')
werkzeug_logger.setLevel(rel_log.ERROR)

# 解决缓存刷新问题
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        name = kwargs.get('name')
        password = kwargs.get('password')
        email = kwargs.get('email')
        self.name = name
        # 加密密码，注意需要导入
        self.password = generate_password_hash(password)
        self.email = email

    # 检查密码函数
    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result
    def __repr__(self):
        return '<Role: %s %s %s %s>' % (self.name, self.id, self.email, self.password)

# 登录限制装饰器 增加到购物车等函数
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_username'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('static', filename='./index.html'))
    return wrapper

# 添加header解决跨域
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
    return redirect(url_for('static', filename='./index.html'))

@app.route('/loginPage', methods=['POST'])
def loginPage():
    data = request.get_json()
    email =data["email"]
    password = data["password"]
    print(email)
    print(password)
    user = User.query.filter_by(email=email).first()
    if user:
        if user.check_password(password):
            print(user)
            print(user.password)
            session['user_username'] = user.name
            return 'Login successfully'
        else:
            return 'Wrong password'
    else:
        return "This email had not been registered yet."

@app.route('/signupPage', methods=['POST'])
def signupPage():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    username = data["username"]
    user = User.query.filter_by(email=email).first()
    if user:
        return "This email was already registered."
    else:
        new_user = User(name=username, password=password,email=email)
        db.session.add(new_user)
        db.session.commit()
        #保存session
        session['user_username'] = username
        return "Signup successfully!"

@app.route('/model', methods=['POST'])
def choose_model():
    for i in request.form.keys():
        print(i)
        current_app.model.changeModel(str(i))
    return "ok"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    print(datetime.datetime.now(), file.filename)

    current_app.model.currentModel()

    if file and allowed_file(file.filename):
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_path)
        shutil.copy(src_path, './tmp/ct')
        image_path = os.path.join('./tmp/ct', file.filename)

        # 通过Core main 给定的model来调用ALDetector_pytorch中的detect方法

        pid, image_info = core.main.c_main(
            image_path, current_app.model, file.filename.rsplit('.', 1)[1])
        return jsonify({'status': 1,
                        'image_url': 'http://127.0.0.1:5003/tmp/ct/' + pid,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid,
                        'image_info': image_info})

    return jsonify({'status': 0})


@app.route("/download", methods=['GET'])
def download_file():
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    return send_from_directory('data', 'testfile.zip', as_attachment=True)


# show photo
@app.route('/tmp/<path:file>', methods=['GET'])
def show_photo(file):
    if request.method == 'GET':
        if not file is None:
            image_data = open(f'tmp/{file}', "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response


if __name__ == '__main__':
    files = [
        'uploads', 'tmp/ct', 'tmp/draw',
        'tmp/image', 'tmp/mask', 'tmp/uploads'
    ]
    for ff in files:
        if not os.path.exists(ff):
            os.makedirs(ff)
    with app.app_context():
        current_app.model = Detector()

    # # 删除表
    # db.drop_all()
    # # 创建表
    # db.create_all()
    # # 生成数据
    # u1 = User(name='dazha', password='fengyunjia',email='758@qq.com')
    # db.session.add(u1)
    # # 提交会话
    # db.session.commit()


    app.run(host='127.0.0.1', port=5003, debug=True)
