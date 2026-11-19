from app.db.database import SessionLocal
from app.models.user import User
from app.core.security import create_access_token
import app.models.project # import this to fix KeyError
import app.models.team
import app.models.task
import app.models.workspace
import app.models.file
db = SessionLocal()
user = db.query(User).filter(User.email.in_(["nirmalpatel93280@gmail.com", "admin@cloudtaskpro.in"])).first()
if user:
    print(f"Token for {user.name} ({user.email}):")
    print(create_access_token({"sub": user.email, "role": user.role}))
else:
    print("User not found.")
