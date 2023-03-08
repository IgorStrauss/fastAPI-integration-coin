
from typing import List

from fastapi import APIRouter, HTTPException

from schemas import (ErrorOutPut, StandardOutput, UserCreateInput,
                     UserFavoriteAddInput, UserListoutput)
from services import FavoriteService, UserService

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')


@user_router.post('/create', description='Criação de usuário',
                  response_model=StandardOutput,
                  responses={400: {'model': ErrorOutPut}}
                  )
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandardOutput(message='Usuário cadastrado com sucesso!')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete('/delete/{user_id}', description='Deletar usuário',
                    response_model=StandardOutput,
                    responses={400: {'model': ErrorOutPut}}
                    )
async def user_delete(user_id: int):
    try:
        await UserService.delete_user(user_id)
        return StandardOutput(message='Deletado com sucesso.')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.post('/favorite/add', description='Adicionar moeda aos favoritos',
                  response_model=StandardOutput,
                  responses={400: {'model': ErrorOutPut}}
                  )
async def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
        await FavoriteService.add_favorite(user_id=favorite_add.user_id,
                                           symbol=favorite_add.symbol)
        return StandardOutput(message='Moeda adicionada aos favoritos.')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.delete('/favorite/remove/{user_id}',
                    description='Remover moeda de favoritos',
                    response_model=StandardOutput,
                    responses={400: {'model': ErrorOutPut}}
                    )
async def user_favorite_remove(user_id: int, symbol: str):
    try:
        await FavoriteService.remove_favorite(user_id=user_id, symbol=symbol)
        return StandardOutput(message='Moeda removida.')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@user_router.get('/list',
                 description='Listar usuário com suas moedas favoritas',
                 response_model=List[UserListoutput],
                 responses={400: {'model': ErrorOutPut}}
                 )
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

"""Corrigir rota para gerar lista de ativos - rota desatualizada"""
# @assets_router.get('/day_summary/{user_id}',
# response_model=List[DaySumaryOutput],
# responses={400: {'model': ErrorOutPut}})
# async def day_summary(user_id: int):
#     try:
#         user = await UserService.get_by_id(user_id)
#         favorites_symbols = [favorite.symbol for favorite in user.favorites]
#         tasks = [
    # AssetService.day_summary(symbol=symbol) for symbol in favorites_symbols]
#         return await gather(*tasks)

#     except Exception as error:
#         raise HTTPException(400, detail=str(error))
