from fastapi import APIRouter, Depends
from src.services import users
from src.db.schemas import UserBase
from src.db.database import get_db

router = APIRouter(prefix='/user', tags=['user'])


# Get All Users
@router.get('/')
def get_user():
    return {"message": "all users are here"}


@router.post('/creat')
async def creat_user(user: UserBase, db=Depends(get_db)):
    return await users.create_user(db, user)


@router.get('/allUsers')
async def get_all_users(db=Depends(get_db)):
    return await users.get_all_users(db)


@router.get('/getUser/{id}')
async def get_user_by_id(id: int, db=Depends(get_db)):
    return await users.get_user_by_id(id, db)
