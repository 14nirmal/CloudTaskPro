from app.db.database import SessionLocal
from app.models.user import User
from app.core.security import create_access_token

db = SessionLocal()
nirmal = db.query(User).filter(User.email.in_(["nirmalpatel93280@gmail.com", "admin@cloudtaskpro.in"])).first()
if nirmal:
    token = create_access_token({"sub": nirmal.email, "role": nirmal.role})
    print(token)
