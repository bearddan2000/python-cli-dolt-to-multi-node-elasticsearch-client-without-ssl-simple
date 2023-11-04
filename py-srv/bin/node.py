from elasticsearch import Elasticsearch

from data import DOC, INDEX_NAME

class Cluster():
    server_name = ''

    def __init__(self, server) -> None:
        self.server_name = server
        self.es = Elasticsearch(
            server + ":9200",
            http_auth=["elastic", "changeme"],
        )
        self.seed()

    def seed(self):
        for record in DOC:
            resp=self.es.index(index=INDEX_NAME, id=record['id'], document=record)
            print("from {} seed: {}".format(self.server_name, resp['result']))

    def print_get(self):
        resp=self.es.get(index=INDEX_NAME, id=1)
        print("from {} print_get: {}".format(self.server_name, resp['_source']))

    def print_search(self):
        SELECT_ALL = {"match_all": {}}
        self.es.indices.refresh(index=INDEX_NAME)
        resp=self.es.search(index=INDEX_NAME, query=SELECT_ALL, size=5)
        print("from {} print_search_hits: {}".format(self.server_name, resp['hits']['total']['value']))
        for hit in resp['hits']['hits']:
            print("from {} print_search: {}".format(self.server_name, hit["_source"]))
