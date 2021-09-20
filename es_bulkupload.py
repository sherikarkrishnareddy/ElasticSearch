#posting bulk_data to Elastic Search
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
SAMPLE_DATA_DIR = "shakespeare_6.0.json"


# elasticsearch config
ES_HOST = "http://localhost"
ES_PORT = 9200

es = Elasticsearch(host= ES_HOST, port= ES_PORT)
es = Elasticsearch()
es.indices.create(index="shakespeare", ignore=400)
def load_jsondata():
    with open(SAMPLE_DATA_DIR) as f:
        data = [json.loads(line) for line in f]
        return data

def insert_data_by_bulk(data):
    res = helpers.parallel_bulk(es, data)
    print(res)


if __name__ == "__main__":
    demo_data_2 = load_jsondata()
    insert_data_by_bulk(demo_data_2)
