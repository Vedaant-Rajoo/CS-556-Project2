import networkx as nx
import datetime as dt

def getNow():
    return int(dt.datetime.now().timestamp())

# Algorithm to recursively revoke all authorizations from a user
def rec_revoke(g, admin, user):
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
    pass
class AuthGraph(nx.DiGraph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def add_user(self,user,role=None):
        self.add_node(user,role=role)
    
    def delegate(self, grantor, grantee):
        if grantor or grantee not in self.nodes:
            raise AuthGraphError("User not in Database")
        elif (self.nodes[grantor]['role'] not in ['owner','admin']):
            raise AuthGraphError("You are not authorized to delegate")
        else:
            self.add_edge(grantor,grantee,weight=getNow())
    
    def recursive_revoke(self, admin, user):
        # if admin is not the grantor of user, raise error
        if not self.has_edge(admin, user):
            raise AuthGraphError("You are not authorized to revoke this user's privileges")
        else:
            rec_revoke(self, admin, user)
            self.remove_node(user)
        
        
