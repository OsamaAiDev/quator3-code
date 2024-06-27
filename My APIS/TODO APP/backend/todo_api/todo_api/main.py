from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated, List
from sqlmodel import SQLModel, Field, create_engine, Session, select
from todo_api import settings
from contextlib import asynccontextmanager

# Creating Todo Model
class Todo(SQLModel, table = True):
    id: int | None = Field(default= None, primary_key= True)
    content: str = Field(index= True, min_length=3, max_length=50)
    is_completed: bool = Field(default= False)

connection_string: str = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)
def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Creating Tables')
    create_tables()
    print("Tables Created")
    yield

app: FastAPI = FastAPI(
    lifespan= lifespan,
    title = "TODO API",
    version= "1.0.0"
    )
@app.get("/")
async def root():
    return {"message": "Wecome to my todo API!"}

@app.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo, session: Annotated[Session, Depends(get_session)]):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

@app.get("/todos/", response_model=List[Todo])
async def get_all_todos(session: Annotated[Session, Depends(get_session)]):
    todos = session.exec(select(Todo)).all()
    return todos

@app.get("/todos/{id}", response_model=Todo)
async def get_single_todo(id: int, session: Annotated[Session, Depends(get_session)]):
    todo = session.exec(select(Todo).where(Todo.id == id)).first()
    return todo
    
@app.put("/todos/{id}")
async def update_todo(id: int, todo: Todo, session: Annotated[Session, Depends(get_session)]):
    exisiting_todo = session.exec(select(Todo).where(Todo.id == id)).first()
    if exisiting_todo:
        exisiting_todo.content = todo.content
        exisiting_todo.is_completed = todo.is_completed
        session.commit()
        session.refresh(exisiting_todo)
        return exisiting_todo
    else:
        raise HTTPException(status_code=404, detail= "No task found enter valid id")
@app.delete("/todos/{id}")
async def delete_todo(id: int, session: Annotated[Session, Depends(get_session)]):
    # todo = session.exec(select(Todo).where(Todo.id == id)).first()
    todo = session.get(Todo, id)
    if todo:
        session.delete(todo)
        session.commit()
        return {"message": "Task successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail= "No task found enter valid id")