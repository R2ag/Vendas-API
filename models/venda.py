from db import db
from typing import List

class VendaModel(db.Model):
    __tablename__ = "venda"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    cliente = db.relationship("ClienteModel",)
    
    carrinhos = db.relationship("CarrinhoModel", lazy="dynamic", primaryjoin="VendaModel.id == CarrinhoModel.venda_id")
    
    
    def __init__(self, cliente_id) -> None:
        self.cliente_id = cliente_id
    
    def __repr__(self) -> str:
        return f'Venda(Id={self.id}, Cliente={self.cliente_id}'
    
    def json(self):
        return {'Id':self.id, 'Cliente':self.cliente_id}
    
    @classmethod
    def find_by_cliente(cls, id_cliente) -> List["VendaModel"]:
        return cls.query.filter_by(cliente_id=id_cliente)
    
    @classmethod
    def find_by_id(cls, id) -> "VendaModel":
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls) -> List["VendaModel"]:
        return cls.query.all()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()