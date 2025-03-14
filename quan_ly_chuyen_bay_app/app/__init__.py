from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = "((*DSKLFJLSKJF)(W(#)))"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:matkhau@localhost/quanlychuyenbay2?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 8
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
login = LoginManager(app)
cloudinary.config(
    cloud_name='dx6brcofe',
    api_key='716129595449135',
    api_secret='drKg8CvyTumADgnoKln06YGRfss'
)
limiter = Limiter(
    key_func=  get_remote_address,  # Lấy địa chỉ IP client
    app=app,
    default_limits=["100 per minute"]
)
