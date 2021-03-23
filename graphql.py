from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


class GraphqlClient(object):
    headers = {"Content-type": "application/json"}

    def __init__(self, url):
        self.transport = None
        self.client = None
        self.url = url

    def define_transport(self):
        self.transport = RequestsHTTPTransport(
            use_json=True,
            url=self.url,
            verify=False,
            headers=self.headers,
            retries=3
        )

    def define_client(self):
        self.client = Client(transport=self.transport,
                             fetch_schema_from_transport=True)

    def execute(self, query, variables):
        self.define_transport()
        self.define_client()
        return self.client.execute(query, variable_values=variables)
