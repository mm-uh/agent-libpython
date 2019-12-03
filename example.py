from __future__ import print_function

import sys

import lib_agent
from lib_agent.rest import ApiException


def main():
    name = sys.argv[1]
    function = sys.argv[2]
    port = sys.argv[3]

    config = lib_agent.Configuration()
    config.host = f'http://localhost:{port}/api/v1'
    test_case = [
        lib_agent.TestCase('a b', 'ab'),
        lib_agent.TestCase('b c', 'bc'),
    ]
    endpoint_service = [
        lib_agent.Addr('localhost', 10083),
        lib_agent.Addr('localhost', 10084),
        lib_agent.Addr('localhost', 10085),
    ]
    is_alive_service = dict()
    is_alive_service['localhost:10083'] = lib_agent.Addr('localhost', 10183)
    is_alive_service['localhost:10084'] = lib_agent.Addr('localhost', 10184)
    is_alive_service['localhost:10085'] = lib_agent.Addr('localhost', 10185)
    documentation = dict()
    documentation['localhost:10083'] = lib_agent.Addr('localhost', 10183)
    documentation['localhost:10084'] = lib_agent.Addr('localhost', 10184)
    documentation['localhost:10085'] = lib_agent.Addr('localhost', 10185)
    # Agent | Agent to register
    agent = lib_agent.Agent(name=name, function=function, endpoint_service=endpoint_service,
                            documentation=documentation, is_alive_service=is_alive_service, test_cases=test_case)
    # agent1 = lib_agent.Agent(name='Sumaitor', function='sum', endpoint_service=endpoint_service,
    #                          documentation=documentation, is_alive_service=is_alive_service, test_cases=test_case)
    # agent2 = lib_agent.Agent(name='Rest', function='rest', endpoint_service=endpoint_service,
    #                          documentation=documentation, is_alive_service=is_alive_service, test_cases=test_case)
    # agent3 = lib_agent.Agent(name='Multiplicator', function='multiply', endpoint_service=endpoint_service,
    #                          documentation=documentation, is_alive_service=is_alive_service, test_cases=test_case)
    # Create an instance of the API class
    api_instance = lib_agent.DefaultApi(lib_agent.ApiClient(config))

    try:
        api_instance.register_agent(agent)
        # api_instance.register_agent(agent1)
        # api_instance.register_agent(agent2)
        # api_instance.register_agent(agent3)
        print(api_instance.get_agents_names())
        ag = api_instance.get_agent(name)
        print(f'Agent Name -> {ag.name}')
        print(f'Agent Function -> {ag.function}')
    except ApiException as e:
        print("Exception when calling DefaultApi->register_agent: %s\n" % e)


if __name__ == '__main__':
    main()
