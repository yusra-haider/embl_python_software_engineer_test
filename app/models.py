from sqlalchemy import Column, String
from .database import Base

# There are 3 ways to connect to an existing db in SQLAlchemy (as per this answer:
# https://stackoverflow.com/questions/39955521/sqlalchemy-existing-database-query
# and other resources)

# 1) use reflection to reflect a particular table or the entire db as SQLAlchemy objects
# reflection is generally used with SQL core. A good thing is that this can work even with
# tables that don't have primary keys by monkey-patching a dynamic id column. Reflection has its
# own limitations tho, as per the documentation

# 2) use automap with reflection. This reflects the entire database into SQLAlchemy ORM objects
# this does not work with  tables that don't have any defined or candidate primary keys

# 3) define custom classes yourself, as I have done so below. SQLAlchemy ORM objects *have* to have
# a primary key, and `stable_id` seemed like the appropriate column for this

# the pros and cons of each approach are worth further looking into


class Gene(Base):
    __tablename__ = "gene_autocomplete"
    id = Column("stable_id", String, primary_key=True)
    name = Column("display_label", String)
    species = Column("species", String)


# Specify 'extend_existing=True' to redefine options and columns on an existing Table object
#Base.prepare(engine, reflect=True)
