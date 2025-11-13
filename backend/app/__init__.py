from pymongo import MongoClient # type: ignore
from elasticsearch import Elasticsearch # type: ignore
import config

mongo_client = MongoClient(config.MONGO_URI)
db = mongo_client[config.MONGO_DB]

es = Elasticsearch(config.ELASTIC_URL)
