from __future__ import print_function

import socket

import lib_agent


from random import seed
from random import randint


def Retry(f):
    def decorate(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except ConnectionRefusedError or ConnectionRefusedError or ConnectionResetError as e:
                args = [arg for arg in args]
                args[0] = args[0].refreshAgent()
                if args[0] is None:
                    raise Exception("There is not active agents")
    return decorate
        

class PlatformWrapper:
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
        config.host = f'http://{self.know_peers[rnd].ip}:{self.know_peers[rnd].port}/api/v1'
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
            s.settimeout(2)
            s.connect((host, int(port)))
            
            return True
        except:
            return False

    def update_api(self):
        
        print('Updating api instance')
        if not self.is_open(self.host, self.port):
            for node in self.know_peers:
                if self.is_open(node.ip, node.port):
                    self.host = node.ip
                    self.port = node.port
                    self.config.host = f'http://{self.host}:{self.port}/api/v1'
                    self.api_instance = lib_agent.DefaultApi(lib_agent.ApiClient(self.config))
                    self.get_peers()
                    return True
            else:
                return False
        self.get_peers()
        return True

    def get_agent(self, name: str, strict = True):
        if not self.update_api():
            print('Could\'t get peers')
            return None
        print(f'Getting agent {name}')
        try:
            agent = self.api_instance.get_agent(name)
            return AgentWrapper(name, agent, self, strict)
         
        except Exception as e:
            if strict:
                print('Could\'t get agent '+e)
                return None
            print("SIMILARS")
            try:
                for a in self.get_similars(name):
                    print("CICLO "+a)
                    try:
                        agent = self.api_instance.get_agent(a)
                        return AgentWrapper(name, agent, self, True)
                    except:
                        print('Could\'t get agent ')
                        return None
                    
                        
            
                
            except:
                print('Could\'t get agent '+e)
                return None

    def register_agent(self, agent):
        if not self.update_api():
            raise 'Could\'t get peers'
        print('Registering agent')
        try:
            self.api_instance.register_agent(agent)
        except:
            raise 'Couldn\'t Registering agent'
            

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
        except Exception as e:
            print('Couldn\'t get agent by function ' + str(e))
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

    def get_all_functions(self):
        if not self.update_api():
            print('Could\'t get peers')
            return
        print('Getting all agents names')
        try:
            return self.api_instance.get_functions_names()
        except:
            print('Couldn\'t get all functions')
            return None

    def edit_agent(self, agent):
        if not self.update_api():
            print('Could\'t get peers')
            return

        print('Registering agent')
        try:
            self.api_instance.edit_agent(agent)
        except:
            print('Couldn\'t Registering agent')
            return None

    def add_endpoint(self, name, password, serviceEndpoint, isAliveEndpoint, documentationEndpoint):
        body = lib_agent.models.UpdaterAgent()
        body.name = name
        body.password = password
        body.endpoint_service = serviceEndpoint
        body.is_alive_service = isAliveEndpoint
        body.documentation = documentationEndpoint

        if not self.update_api():
            raise 'Could\'t get peers'
        try:
            self.api_instance.add_endpoints(body)
        except Exception as e:
            raise 'Couldn\'t Edit agent'
            

    def recover_agent(self, name, password):
        body = lib_agent.models.RecoverAgent()
        body.name = name
        body.password = password
       
        if not self.update_api():
            print('Could\'t get peers')
            return

        print('Recovering agent')
        try:
            self.api_instance.recover_agent(body)
        except:
            print('Couldn\'t recover agent')
            return None

    def get_similars(self, name):
        if not self.update_api():
            print('Could\'t get peers')
            return
        print('Getting similar agents')
        try:
            return self.api_instance.get_similar_agent(name)
        except:
            print('Couldn\'t get similars agents')
            return None

class AgentWrapper:
    def __init__(self, name, addrs, platform, strict = True):
        self.addrs = addrs
        self.strict = strict
        self.serviceEndpoint = (addrs[0].ip, addrs[0].port)
        self.isAliveEndpoint = (addrs[1].ip, addrs[1].port)
        self.documentationEndpoint = (addrs[2].ip, addrs[2].port)
        self.name = name
        self.platform = platform

    def isAlive(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(self.isAliveEndpoint)
            sock.send("IsAlive?".encode())
            response = sock.recv(20)
            if response.decode() == "Yes":
                return True
            return False
        except:
            return False
    @Retry
    def getDocumentation(self):
        # if not self.isAlive():
        #     self.refreshAgent()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(self.documentationEndpoint)
        sock.send("get".encode())
        data = sock.recv()
        return data.decode()

    def refreshAgent(self):
            return self.platform.get_agent(self.name, self.strict)
        # if agent is None:
        #     raise Exception(f'Couldn\'t get agent for {self.name}')
        # return agent

        
        # if not len(newAddr):
        #     if self.strict:
        #         raise Exception(f'There is no active agent with name {self.name}')
        #     else:
        #         #Try similars
        #         similars = self.platform.get_similars(self.name)
        #         for a in similars:
        #            newAddr = self.platform.get_agent(a).addrs
        #            if len(newAddr):
        #                return AgentWrapper(self.name, newAddr, self.platform, self.strict)
        #         raise Exception(f'There is no active agent compatible with {self.name}')
        # return AgentWrapper(self.name, newAddr, self.platform, self.strict)
    
    @Retry
    def sendToAgent(self, dataSend):
        # if not self.isAlive():
            # self.refreshAgent()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(self.serviceEndpoint)

        sock.sendall(dataSend.encode())
        data = sock.recv(1024)
        return data.decode()
        



