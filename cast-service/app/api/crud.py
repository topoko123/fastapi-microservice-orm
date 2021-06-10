from typing import Dict

import sqlalchemy

from sqlalchemy.orm import Session

from fastapi import status

from . import models_db


def get_current_cast(db: Session, cast_id):
    return db.query(models_db.Casts).filter(models_db.Casts.cast_id == cast_id).first()

def get_all_cast(db: Session):
    return db.query(models_db.Casts).all()

def post_cast(db: Session, payload: Dict):
    try:
        db_cast = models_db.Casts(**payload)
        db.add(db_cast)
        db.commit()
        db.refresh(db_cast)
    except sqlalchemy.exc.SQLAlchemyError as e:
        db.rollback()
        print('found problem\n', e)
        
    return db_cast

def update_current_cast(db: Session, cast_id, payload):
    try:
        db_cast = db.query(models_db.Casts).filter(models_db.Casts.cast_id == cast_id)
        if not db_cast.first():
            return {'status_code': status.HTTP_400_BAD_REQUEST, 'detail': 'Delete Failed'}
        db_cast.delete(synchronize_session=False)
        db.commit()
    except sqlalchemy.exc.SQLAlchemyError as e:
        db.rollback()
        print('found problem\n', e)
        return 'Delete Failed' 
    return 'Delete Success'

def delete_current_cast(db: Session, cast_id):
    try:
        db_cast = db.query(models_db.cast).filter(models_db.cast.cast_id == cast_id)
        if not db_cast.first():
            return {'status_code': status.HTTP_400_BAD_REQUEST, 'detail': 'Delete Failed'}
        db_cast.delete(synchronize_session=False)
        db.commit()
    except sqlalchemy.exc.SQLAlchemyError as e:
        db.rollback()
        print('found problem\n', e)
        return 'Delete Failed'
    return 'Delete Success'
    