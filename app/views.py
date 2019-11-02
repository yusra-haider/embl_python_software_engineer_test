from fastapi import Query
from .main import app, session
from .models import Gene


@app.get("/")
def home():
    return {"where there's a will, there's a way": "Yusra's attempt at becoming a Python Developer at EMBL-EBI :)"}


@app.get("/gene_search/")
def gene_search(name: str = Query(..., min_length = 3), species: str = None, limit: int = 10):
    filters  = [Gene.name.like("{}%".format(name))]
    if species:
        filters.append(Gene.species == species)
    filters = tuple(filters)

    genes = session.query(Gene.id, Gene.name, Gene.species).filter(*filters).limit(limit)
    return [gene._asdict() for gene in genes]





