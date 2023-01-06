from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi_sqlalchemy import DBSessionMiddleware
from db.session import engine   
from typing import List, Optional
from db.schema import Curso as SchemaCurso
from db.models import Curso as ModelCurso



def create_tables():           #new
	ModelCurso.metadata.create_all(bind=engine)


app = FastAPI()


cursos = {
  1: {
    "titulo": "Programação para Leigos",
    "aulas": 112,
    "horas": 58
  },
  2: {
    "titulo": "Algoritmos e Lógica de Programação",
    "aulas": 87,
    "horas": 39
  }
}

@app.get("/cursos")
async def getCursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def getCursoById(curso_id: int):
  try:
    curso = cursos[curso_id]
    return curso
  except KeyError:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: SchemaCurso):
  if (curso.id == None):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos[next_id] = curso
    return curso
  elif curso.id not in cursos:
    cursos[curso.id] = curso
    return curso
  else:
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Curso de id {curso.id} já existe")

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")

