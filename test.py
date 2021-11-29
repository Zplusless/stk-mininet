
from mininet.topo import Topo
from mininet.util import irange
from mininet.log import error
from mininet.node import Node
from mininet.link import TCIntf

import config



#!  卫星node的ip分配问题, 分配node的时候会默认分配ip






def get_next(n, m, n_max, m_max):
    n_ = (n+1)%n_max
    m_ = (m+1)%m_max
    return n_, m_

class STKTopo(Topo):
    def build(self, n_obit, sat_per_obit):
        self.node_list = [[] for i in range(n_obit) ]

        # 创建node
        node1 = self.addNode('node1')
        node2 = self.addNode('node2')
        
        

        self.addLink(node1, node2)