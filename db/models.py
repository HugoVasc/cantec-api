
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Curso(Base):
    __tablename__ = 'curso'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    aulas = Column(Integer)
    horas = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relacionamento 1 para N
    # 1 curso tem N alunos
    alunos = relationship('Aluno', back_populates='curso')