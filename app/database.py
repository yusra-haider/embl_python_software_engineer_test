from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


engine = create_engine("mysql+pymysql://anonymous@ensembldb.ensembl.org/ensembl_website_97", pool_recycle=3600)
session = Session(engine)

Base = declarative_base()
##Base = automap_base()
