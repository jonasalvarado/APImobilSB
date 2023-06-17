from fastapi import APIRouter



URL_AVATAR = 'https://veapi.subicicleta.com/storage/usuarios/'
URL_COMPLEMENT_AVATAR = '/avatar/'

router = APIRouter(prefix="/marcas",
                   tags=["marcas"],
                   responses={404: {"message": "No encontrado"}})

@router.get("/")
async def marcas():
    id =2
   
    return ["hola marcas"]

