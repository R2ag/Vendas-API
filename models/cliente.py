from db import db
from typing import List

class ClienteModel(db.Model):
    __tablename__="cliente"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    
    vendas = db.relationship("VendaModel", lazy="dynamic", primaryjoin="ClienteModel.id == VendaModel.cliente_id")
    
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def __repr__(self) -> str:
        return f'Cliente(nome={self.nome}, cpf={self.cpf}'
    
    def json(self):
        return{'nome': self.nome, 'cpf': self.cpf}
    
    @classmethod
    def find_by_name(cls, nome) -> "ClienteModel":
        return cls.query.filter_by(nome=nome).first()
    
    @classmethod
    def find_by_id(cls, id) -> "ClienteModel":
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls) -> List["ClienteModel"]:
        return cls.query.all()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()