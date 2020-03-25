from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pokemon(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    usage_percent = db.Column(db.Integer, nullable=False)
    monthly_rank = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String, nullable=False)
    type1 = db.Column(db.String, nullable=False)
    type2 = db.Column(db.String, nullable=True)
    # Needs foreign keys for moveset, teammates, items, abilities, natures, and EVs


class Moveset(db.Model):
    __tablename__ = "movesets"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"), nullable=False)
    moves = db.Column(db.String, unique=True, nullable=False)


class Teammate(db.Model):
    __tablename__ = "teammates"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"), nullable=False)
    teammates = db.Column(db.String, unique=True, nullable=False)


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"), nullable=False)
    items = db.Column(db.String, unique=True, nullable=False)


class Ability(db.Model):
    __tablename__ = "abilities"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"), nullable=False)
    abilities = db.Column(db.String, unique=True, nullable=False)


class Nature(db.Model):
    __tablename__ = "natures"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"), nullable=False)
    natures = db.Column(db.String, unique=True, nullable=False)


class EV(db.Model):
    __tablename__ = "EVs"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    p_attack = db.Column(db.Integer, nullable=False)
    p_defense = db.Column(db.Integer, nullable=False)
    sp_attack = db.Column(db.Integer, nullable=False)
    sp_defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)

    # self.url = url
    # self.usage_percent = usage_percent
    # self.monthly_rank = monthly_rank
    # self.type1 = type1
    # self.type2 = None
    # self.stats = stats
    # self.moves = []
    # self.teammates = []
    # self.items = []
    # self.abilities = []
    # self.nature = [] 
    # self.ev = []
