from fastapi import FastAPI
from pydantic import BaseModel

#Criando Modelo de Dados
class ProductCreate(BaseModel):
    codigo: int
    nome: str
    qtd: int 
    preco: float

app = FastAPI()

products = [
    {
        "codigo" : 0,
        "nome" : "violão",
        "qtd" : 12, 
        "preco" : 500
    },
    {
        "codigo" : 1,
        "nome" : "guitarra",
        "qtd" : 5, 
        "preco" : 1000
    },
    {
        "codigo" : 2,
        "nome" : "bateria",
        "qtd" : 9, 
        "preco" : 1500
    },
]

#Produtos
@app.get("/products")
def GetAllProducts():
    return products

@app.get("/products/{id}")
def GetProductById(id: int):
    for product in products:
        if product["codigo"] == id:
            return product
    return "Produto não encontrado"
    
@app.post("/products")
def AddProduct(dados: ProductCreate):
    products.append(
        {
            "codigo": dados.codigo,
            "nome": dados.nome,
            "qtd": dados.qtd,
            "preco": dados.preco
        }
    )
    return "Produto adicionado ao estoque"

@app.put("/products/{id}")
def EditProduct(id: int, productEdit: ProductCreate):
    for product in products:
        if product["codigo"] == id:
            product["codigo"] = productEdit.codigo
            product["nome"] = productEdit.nome
            product["qtd"] = productEdit.qtd
            product["preco"] = productEdit.preco
            return "Produto Adicionado"
    return "Produto não encontrado"

#Usuarios
@app.get("/users")
def GetAllUsers():
    return "Aqui serão listados os usuários"