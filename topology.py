

from mininet.topo import Topo
from mininet.util import irange
from mininet.log import error
from mininet.node import Node
from mininet.link import TCIntf

from modify_Link import get_next

import config



#!  卫星node的ip分配问题, 分配node的时候会默认分配ip








class STKTopo(Topo):
    def build(self, n_obit, sat_per_obit):
        self.node_list = [[] for i in range(n_obit) ]

        # 创建node
        for n in range(n_obit):
            for m in range(sat_per_obit):
                if not (n==0 and m==0):
                    ip_ = f'10.{n}.{m}.3' if n==0  else f'10.{n}.{m}.4'
                else:
                    ip_ = '10.0.0.1'
                node = self.addNode(f'node_{n}-{m}', ip = ip_)
                self.node_list[n].append(node)
        

        # link
        for n in range(n_obit):
            for m in range(sat_per_obit):
                this_node = self.node_list[n][m]
                n_, m_ = get_next(n,m, n_obit, sat_per_obit)
                next_node1 = self.node_list[n][m_]
                next_node2 = self.node_list[n_][m]
                self.addLink(this_node, 
                            next_node1, 
                            intf=TCIntf, 
                            params1={ #? ip最后一位, 1,2,3,4 分别对应 右 下 左 上
                                'ip': f'10.{n}.{m}.1/8',  # nm 到 nm_的接口 #! +1 是为了避免0.0.0.1这样的ip
                                'bw': config.bw,
                                'delay': config.delay,
                                'jitter': config.jitter,
                                'loss': config.loss
                            },
                            params2={
                                'ip': f'10.{n}.{m_}.3/8',  # nm_ 到 nm的接口
                                'bw': config.bw,
                                'delay': config.delay,
                                'jitter': config.jitter,
                                'loss': config.loss
                            }
                            )
                self.addLink(this_node, 
                            next_node2,
                            intf=TCIntf, 
                            params1={
                                'ip': f'10.{n}.{m}.2/8',  
                                'bw': config.bw,
                                'delay': config.delay,
                                'jitter': config.jitter,
                                'loss': config.loss
                            },
                            params2={
                                'ip': f'10.{n_}.{m}.4/8',  
                                'bw': config.bw,
                                'delay': config.delay,
                                'jitter': config.jitter,
                                'loss': config.loss
                            })