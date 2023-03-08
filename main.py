from fastapi import APIRouter, FastAPI

from views import assets_router, user_router

app = FastAPI()
router = APIRouter()


@router.get('/')
def first():
    return 'Hello world!'


@router.get("/teste")
def teste_router():
    return "rota de teste ativa"


app.include_router(prefix='/first', router=router)
app.include_router(user_router)
app.include_router(assets_router)
