from app import app
from models import Base

if __name__ == '__main__':
    Base.metadata.create_all()
    app.run()
