from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from src.utils.vk_parser import parsing_vk_user


router = APIRouter(prefix="/api/v1/operations", tags=["Operations"])


@router.post("/predict_professions")
async def predict_professions(
    vk_page_url: str
):
    vk_user_id = int(vk_page_url.split('https://vk.com/id')[1])
    parsing_vk_user(user_id=vk_user_id)
    return {"message": "message sended success"}
