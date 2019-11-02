from sqlalchemy import Column, String
from .database import Base

# ADD COMMENTS
# https://stackoverflow.com/questions/39955521/sqlalchemy-existing-database-query
class Gene(Base):
    __tablename__ = "gene_autocomplete"
    id = Column("stable_id", String, primary_key=True)
    name = Column("display_label", String)
    species = Column("species", String)


# Specify 'extend_existing=True' to redefine options and columns on an existing Table object

#Base.prepare(engine, reflect=True)
