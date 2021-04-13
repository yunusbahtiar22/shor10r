import string
from app.extension import db
from datetime import datetime
from random import choices


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()
    
    def generate_short_url(self):
        chars = string.digits + string.ascii_letters
        shortened = ''.join(choices(chars, k=5))

        url_exist = self.query.filter_by(short_url=shortened).first()


        if url_exist:
            return self.generate_short_url()
        
        return shortened
