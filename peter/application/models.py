from application import crud_db

class Games(crud_db.Model):
    id = crud_db.Column(crud_db.Integer, primary_key=True)
    name = crud_db.Column(crud_db.String(30))