from fastapi import Query
from .main import app, session
from .models import Gene


@app.get("/")
def home():
    return {"where there's a will, there's a way": "Yusra's attempt at becoming a Python Developer at EMBL-EBI :)"}

# currently the docs don't show any schema for the response
# The approach suggested in this thread https://github.com/tiangolo/fastapi/issues/280
# was tried out, but it didn't seem to work

# also I'm aware that the business requirements said to return all matching entries, and didn't
# say to add the limit parameter. My reason for adding this query parameter is two-fold:
# 1) currently ongoing connectivity issues in my region were resulting in timeouts without this parameter
# 2) I think it's generally good API design to limit the number of results being fetched
@app.get("/gene_search/")
def gene_search(name: str = Query(..., min_length = 3), species: str = None, limit: int = 10):
    filters = [Gene.name.like("{}%".format(name))]
    if species:
        filters.append(Gene.species == species)
    filters = tuple(filters)

    genes = session.query(Gene.id, Gene.name, Gene.species).filter(*filters).limit(limit)
    return [gene._asdict() for gene in genes]
