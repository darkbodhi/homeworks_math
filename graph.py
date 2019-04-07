class Graph(object):
    pass

    def __init__(self):
        self.nodes_number = None
        main_list = []
        legacy_list = []

    def create_graph(self):
        self.nodes_number = int(input("Please, insert the number of nodes: "))
        for j in range(self.nodes_number):
            main_list.append(j)
            sorted(main_list)

    def legacy_connection(self):
        x = int(input("Please insert the number of the node you want to connect: "))
        y = int(input("Please insert the number of the node to which you want to connect: "))
        for x in self.node_number:
            legacy_list.append(x, y)
            sorted(legacy_list)

    def give_allnodes(self):
        print(main_list)

    def graph_length(self):
        print(len(main_list))

    def give_node(self):
        node = int(input("Please, insert the number of node you want to return: "))
        if node in main_list:
            return node
        else:
            print("An error has occurred. There is no such node.")

    def give_legacy(self):
        node = int(input("Please, insert the number of node legacy of which you want to return: "))
        for node in legacy_list:
            return(legacy_list(y))

    def give_ancsestor(self):
        node = int(input("Please, insert the number of node ancestor of which you want to return: "))
        for node in legacy_list:
            return(legacy_list(x))

    def new_legacy(self):
        node = int(input("Please, insert the number of node legacy of which you want to renew: "))
        new = int(input("Please, insert the nodes you want to add: "))
        for node in legacy_list:
            legacy_list.append(new)
            sorted(legacy_list)

    def new_ancestor(self):
        node = int(input("Please, insert the number of node ancsestor of which you want to renew: "))
        new = int(input("Please, insert the nodes you want to add: "))
        for node in legacy_list:
            legacy_list.append(new)