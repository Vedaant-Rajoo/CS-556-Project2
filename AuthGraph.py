import random
import json
import networkx as nx


def getNow():
    try:
        f = open('highest.txt', 'r')
        i = int(f.read().strip())
    except FileNotFoundError:
        open('highest.txt', 'w')
        i = random.randint(0, 10)

    increment = random.randrange(1, 10)
    i += increment

    with open('highest.txt', 'w') as f:
        f.write(str(i))

    return i


def rec_revoke(g, admin, user):
    """
    Recursive Revoke Algorithm that revokes all authorizations from previous grantors
    g: AuthGraph
    admin: str
    user: str
    Returns: None
    """
    if not g.has_edge(admin, user):
        return
    g.remove_edge(admin, user)

    # Check all the nodes revokee has delegated to before revoker delegated to us.
    nodes_to_keep = []
    for node in list(g.neighbors(user)):
        weight = g[user][node]['weight']
        if g.has_edge(admin, node) and g[admin][node]['weight'] < weight:
            nodes_to_keep.append(node)
        elif node != admin:
            rec_revoke(g, user, node)
            # Remove all edges to nodes that were not kept
    for node in g.neighbors(user):
        if node not in nodes_to_keep and node != admin:
            rec_revoke(g, admin, node)


class AuthGraphError(Exception):
    """
    A class that represents the authorization graph error types
    """

    def __init__(self, message):
        super().__init__(message)


class AuthGraph(nx.DiGraph):
    """
    The AuthGraph class that inherits from networkx.DiGraph
    """

    def __init__(self, policy, **attr):
        super().__init__(**attr)
        self.policy = policy
        self.graph['obj'] = self.policy[0]
        self.graph['for'] = self.policy[1]
        self.graph['delegate'] = self.policy[2]
        self.graph['transfer'] = self.policy[3]
        self.graph['acceptance'] = self.policy[4]
        self.graph['revoke'] = self.policy[5]

    def load_graph(self, graph):
        """
        Loads a graph from a json string
        graph: str
        Returns: None
        """
        data = json.loads(graph)
        g_atr = data["graph"]
        if len(g_atr) == 0:
            data = nx.node_link_graph(data)
            self.add_nodes_from(data.nodes(data=True))
            self.add_edges_from(data.edges(data=True))
        else:
            data = nx.node_link_graph(data)
            self.clear()
            self.add_nodes_from(data.nodes(data=True))
            self.add_edges_from(data.edges(data=True))
            self.graph = g_atr

    def save_graph(self):
        """
        Saves the graph to a json string
        Returns: str
        """
        if self.graph is not None:
            data = nx.node_link_data(self)
            data["graph"] = self.graph
            return json.dumps(data)
        else:
            raise AuthGraphError("Cant load attrributes")

    def add_user(self, user, role=None):
        if user in self.nodes:
            raise AuthGraphError("User already in Database")
        else:
            self.add_node(user, role=role)

    def delegate(self, grantor, grantee):
        if self.graph['delegate'] is None:
            raise AuthGraphError("Delegation not allowed")
        elif self.graph['delegate'] == 'delegation':
            if self.has_edge(grantor, grantee):
                raise AuthGraphError("Already delegated")
            if grantor not in self.nodes:
                raise AuthGraphError("Grantor not in Database")
            elif grantee not in self.nodes:
                self.add_user(grantee, role='admin')
            elif (self.nodes[grantor]['role'] not in ['owner', 'admin']) or (
                    self.nodes[grantee]['role'] == 'owner') or self.has_edge(grantee, grantor):
                raise AuthGraphError("You are not authorized to delegate")
            self.add_edge(grantor, grantee, weight=getNow())
            self.nodes[grantee]['role'] = 'admin'
        else:
            raise AuthGraphError("Invalid Delegation")

    def revoke(self, admin, user):
        if (admin or user) not in self.nodes:
            raise AuthGraphError("User not in Database")
        elif self.nodes[admin]['role'] not in ['owner', 'admin']:
            raise AuthGraphError("You are not authorized to revoke")
        self.remove_edge(admin, user)
        self.nodes[user]['role'] = None

    def recursive_revoke(self, admin, user):
        # if admin is not the grantor of user, raise error
        if not self.has_edge(admin, user):
            raise AuthGraphError("You are not authorized to revoke this user's privileges")
        else:
            rec_revoke(self, admin, user)
            self.remove_node(user)

    def grantor_transfer(self, grantor, grantee):
        if not self.has_node(grantor) or self.nodes[grantor]['role'] != 'owner':
            raise AuthGraphError("Either Grantor not in Database or Grantor is not an owner")
        elif not list(self.successors(grantor)):
            # This means that the grantor has not delegated any privileges
            if grantee not in self.nodes:
                # If grantee not in graph, add grantee as user and give it owner
                self.add_user(grantee, role='owner')
            else:
                self.nodes[grantee]['role'] = 'owner'
            self.remove_node(grantor)
            self.add_node(grantor, role='shadow')
        else:
            outgoing_edges = list(self.out_edges(grantor, data=True))
            for edge in outgoing_edges:
                receiver = edge[1]
                weight = edge[2]['weight']
                # remove cyclic edges
                if receiver == grantee:
                    continue
                else:
                    if self.has_edge(grantee, receiver):
                        old_weight = self.get_edge_data(grantee, receiver)['weight']
                        weight = min(old_weight, weight)
                    self.add_edge(grantee, receiver, weight=weight)
        # We remove all incoming edges to grantee coz he is now the owner
        incoming_edges = list(self.in_edges(grantee, data=False))
        if incoming_edges:
            self.remove_edges_from(incoming_edges)
        self.remove_node(grantor)
        self.add_node(grantor, role='shadow')

    def transfer(self, grantor, grantee):
        if self.graph['transfer'] is None or self.graph['transfer'] == 'no-transfer' or self.graph['transfer'] == 'nil':
            raise AuthGraphError("Transfer not allowed")
        else:
            if self.graph['revoke'] == 'grantor-transfer':
                self.grantor_transfer(grantor, grantee)
            elif self.graph['revoke'] == 'revoke':
                self.recursive_revoke(grantor, grantee)
            else:
                raise AuthGraphError("Invalid Transfer")
