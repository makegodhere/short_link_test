from hashlib import md5
from config.db import db

POSTFIX_BASE_LENGTH = 6


class LinkStorage(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    longLink = db.Column(
        db.Text,
        unique=True,
        nullable=False
    )
    postfix = db.Column(
        db.String(255),
        unique=True,
        default='',
        nullable=False
    )
    count = db.Column(
        db.BigInteger,
        default=0,
        unique=False,
        nullable=False
    )

    def __init__(self, *args, **kwargs):
        kwargs['postfix'] = md5(kwargs['longLink'].encode()).hexdigest()[:POSTFIX_BASE_LENGTH]
        super(LinkStorage, self).__init__(*args, **kwargs)
