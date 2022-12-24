from application import crud_db
from application.models import Games


crud_db.drop_all()

new_game = Games(name="peter is testing")
new_game1 = Games(name="of the wall")

crud_db.create_all()
crud_db.session.add(new_game)
crud_db.session.add(new_game1)
crud_db.session.commit()
