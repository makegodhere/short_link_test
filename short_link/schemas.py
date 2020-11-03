from marshmallow import fields
from config.db import ma
from .models import LinkStorage


class LongToShortSchema(ma.SQLAlchemySchema):
    long_url = fields.String(
        attribute='longLink',
        required=True
    )

    class Meta:
        model = LinkStorage


class ActionByShortPostfixSchema(ma.SQLAlchemySchema):
    short_postfix = fields.String(
        attribute='postfix',
        required=True
    )

    class Meta:
        model = LinkStorage
