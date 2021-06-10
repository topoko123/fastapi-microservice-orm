from fastapi import APIRouter, Depends, status

from .models import CastBase, CastUpdate

from sqlalchemy.orm import Session

from . import crud, models_db

from .config_db import SessionLocal, engine

casts = APIRouter()

models_db.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@casts.get('/{cast_id}')
async def get_current_cast(cast_id: int, db: Session = Depends(get_db)):
    try:
        global msg
        db_cast = crud.get_current_cast(db, cast_id)
        assert db_cast != [], 'Not Infomation yet'
        
        msg = [{'status_code': status.HTTP_200_OK, 'detail': 'Infomation received'}, {'data': db_cast}]
    except AssertionError as e:
        msg = [{'status_code': status.HTTP_200_OK, 'detail': str(e)}, {'data': db_cast}]
    return msg

@casts.get('/get/all')
async def get_all_cast(db: Session = Depends(get_db)):
    try:
        global msg
        db_cast = crud.get_all_cast(db)
        assert db_cast != [], 'Not infomation yet'
        msg = [{'status_code': status.HTTP_200_OK, 'detail': 'Infomation received'}, {'data': db_cast}]
    
    except AssertionError as e:
        msg = [{'status_code': status.HTTP_200_OK, 'detail': str(e)}, {'data': db_cast}]
    return msg

@casts.post('/add-cast')
async def add_movie(payload: CastBase, db: Session = Depends(get_db)):
    try:
        global msg
            
        db_cast = crud.post_cast(db, payload.dict())
        if db_cast:
            msg = [{'status_code': status.HTTP_201_CREATED, 'detail': 'Create Movie'}, {'data': db_cast}]
            
    except AssertionError as e:
        msg = {'status_code': status.HTTP_404_NOT_FOUND, 'detail': e}

    return msg

@casts.patch('/update/{cast_id}')
async def update_current_cast(cast_id: int, payload: CastUpdate, db: Session = Depends(get_db)):
    new_payload_dict = payload.dict(exclude_unset=True)
    db_cast = crud.update_current_cast(db, cast_id, new_payload_dict)
    return {'data': db_cast}

@casts.delete('/delete/{cast_id}')
async def delete_current_cast(cast_id: int, db: Session = Depends(get_db)):
    db_cast = crud.delete_current_cast(db, cast_id)
    return {'data': db_cast}