from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos,users
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Mounting Technique - to mount our static files to the application - means adding a completely independent app to a specific path
#that takes care of handling evrything under hte path with the path operations defined in that sub application

app.mount("/static",StaticFiles(directory="static"),name="static")

# All the normal URLs like localhost:/ redirect to todos if logged in and /auth login page if not logged in
@app.get("/")
async def root():
    return RedirectResponse(url="/todos",status_code=status.HTTP_302_FOUND)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
