"""隐马尔可夫模型API"""

from fastapi import APIRouter

from echo.research.hmm_predictor import get_hidden_markov_model


router = APIRouter(prefix="/api/hmm", tags=["hmm"])


@router.post("/forward")
async def forward(obs: list[int]):
    hmm = get_hidden_markov_model()
    init = [0.5, 0.5]
    trans = [[0.7, 0.3], [0.3, 0.7]]
    emit = [[0.9, 0.1], [0.2, 0.8]]
    return {"probability": hmm.forward(obs, init, trans, emit)}
