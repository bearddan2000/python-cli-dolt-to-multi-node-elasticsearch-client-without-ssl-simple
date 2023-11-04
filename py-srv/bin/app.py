from node import Cluster

def main():
    es = Cluster('es1')
    es.print_search()
    es = Cluster('es2')
    es.print_search()
    es = Cluster('es3')
    es.print_search()

main()