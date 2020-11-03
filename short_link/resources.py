from flask import request, redirect
from marshmallow import ValidationError
from flask_restplus import Resource
from config.db import db
from .models import LinkStorage
from .settings import BASE_URL
from .schemas import LongToShortSchema, ActionByShortPostfixSchema


class LongToShortResource(Resource):
    """
    Генерируем короткую ссылку по длинной
    """

    def post(self, *args, **kwargs):
        # Служебное создание таблиц для тестового задания
        db.create_all()

        # Получаем входные входные данные из запроса и проводим валидацию
        try:
            data = request.get_json(force=True)
            dataSchema = LongToShortSchema()
            dataSchema.load(data)
        except ValidationError as err:
            return err.messages, 422

        # Проверяем наличие объекта по длинной ссылке
        # В случае отсутствия - создаем новый объект
        linkStorageObj = LinkStorage.query.filter_by(longLink=data['long_url']).first()
        if not linkStorageObj:
            linkStorageObj = LinkStorage(
                longLink=data['long_url']
            )
            db.session.add(linkStorageObj)
            db.session.commit()

        response = {
            'short_link': f'{BASE_URL}{linkStorageObj.postfix}'
        }

        return response


class RedirectToLongLinkResource(Resource):
    """
    Перенаправялем на длинную ссылку
    """

    def get(self, *args, **kwargs):
        # Служебное создание таблиц для тестового задания
        db.create_all()

        # Проверяем корректность урла
        dataSchema = ActionByShortPostfixSchema()
        try:
            dataSchema.load(kwargs)
        except ValidationError as err:
            return err.messages, 422

        # Проверяем наличие объекта по короткой сслыке
        try:
            linkStorageObj = LinkStorage.query.filter_by(postfix=kwargs['short_postfix']).first()
            getattr(linkStorageObj, 'longLink')
        except AttributeError:
            return 'Invalid short_postfix', 422

        # Учитываем новое количество переходов по сслыке
        linkStorageObj.count += 1
        db.session.add(linkStorageObj)
        db.session.commit()

        return redirect(linkStorageObj.longLink, code=302)


class StatisticsResource(Resource):
    """
    Показываем статистику (количество переходов) по короткой сслыке
    """

    def get(self, *args, **kwargs):
        # Служебное создание таблиц для тестового задания
        db.create_all()

        # Проверяем корректность урла
        dataSchema = ActionByShortPostfixSchema()
        try:
            dataSchema.load(kwargs)
        except ValidationError as err:
            return err.messages, 422

        # Проверяем наличие объекта по короткой сслыке
        try:
            linkStorageObj = LinkStorage.query.filter_by(postfix=kwargs['short_postfix']).first()
            getattr(linkStorageObj, 'count')
        except AttributeError:
            return 'Invalid short_postfix', 422

        response = {
            'count': linkStorageObj.count
        }

        return response
