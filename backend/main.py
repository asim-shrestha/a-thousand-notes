import uvicorn
import os
from src import app

if __name__ == '__main__':
    uvicorn.run('main:app', host=os.environ.get('APT_HOST'), port=int(os.environ.get('API_PORT')), reload=os.environ.get('API_HOT_RELOAD'))