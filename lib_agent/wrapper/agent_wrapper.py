from __future__ import print_function

import socket

import lib_agent

from random import seed
from random import randint


class AgentWrapper:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.config = lib_agent.Configuration()
        self.config.host = f'http://{host}:{port}/api/v1'

        self.know_peers = []
        self.api_instance = lib_agent.DefaultApi(lib_agent.ApiClient(self.config))
        self.get_peers()

    def get_peers(self):
        print('Getting peers')
        try:
            temp_peers = self.api_instance.get_peers()
            print('Obtained peers')
            self.know_peers = list(set().union(self.know_peers, temp_peers))
        except Exception as e:
            print('Could\'t get peers' + str(e))
        self.update_peers()

    def update_peers(self):
        print('Updating peers')
        if not self.is_open(self.host, self.port):
            return
        if len(self.know_peers) < 1:
            return
        if len(self.know_peers) > 20:
            self.know_peers = self.know_peers[10:]
        # rand number [0, len(self.know_peers)]
        seed(1)
        rnd = randint(0, len(self.know_peers))
        config = lib_agent.Configuration()
        config.host = f'http://{self.know_peers[rnd].ip}:{self.know_peers[rnd].port+1000}/api/v1'
        api_temp = lib_agent.DefaultApi(lib_agent.ApiClient(config))
        try:
            temp_peers = api_temp.get_peers()
            print('Obtained peers')
            self.know_peers = list(set().union(self.know_peers, temp_peers))
        except:
            print('Could\'t get peers')

    @staticmethod
    def is_open(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, int(port)))
            s.shutdown(2)
            return True
        except:
            return False

    def update_api(self):
        self.get_peers()
        print('Updating api instance')
        if not self.is_open(self.host, self.port):
            for node in self.know_peers:
                if self.is_open(node.ip, node.port):
                    self.host = node.ip
                    self.port = node.port + 1000
                    self.config.host = f'http://{self.host}:{self.port}/api/v1'
                    self.api_instance = lib_agent.DefaultApi(lib_agent.ApiClient(self.config))
                    return True
            else:
                return False
        return True

    def get_agent(self, name: str):
        if not self.update_api():
            print('Could\'t get peers')
            return None
        print(f'Getting agent {name}')
        try:
            agent = self.api_instance.get_agent(name)
            return agent
        except:
            print('Could\'t get agent')
            return None

    def register_agent(self, agent):
        if not self.update_api():
            print('Could\'t get peers')
            return

        print('Registering agent')
        try:
            self.api_instance.register_agent(agent)
        except:
            print('Couldn\'t Registering agent')
            return None

    def get_all_agents(self):
        if not self.update_api():
            print('Could\'t get peers')
            return

        print('Getting all agents names')
        try:
            return self.api_instance.get_agents_names()
        except:
            print('Couldn\'t get agent all agents')
            return None

    def get_agent_by_function(self, name):
        if not self.update_api():
            print('Could\'t get peers')
            return None

        print('Getting agent by function')
        try:
            func = self.api_instance.get_agents_by_function(name)
            return func
        except:
            print('Couldn\'t get agent by function')
            return None

    def run_agent(self, agent_name: str, params: str):
        if not self.update_api():
            print('Could\'t get peers')
            return

        agent = self.get_agent(agent_name)
        if agent is None or len(agent) != 3:
            return None
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (agent[0].ip, agent[0].port)
        sock.connect(server_address)
        response = ''
        try:
            print(f'sending {params} to agent {agent_name}')
            sock.sendall(params.encode())

            while True:
                data: bytes = sock.recv(16)
                if len(data) == 0:
                    break
                response += data.decode()

        finally:
            sock.close()
        return response
