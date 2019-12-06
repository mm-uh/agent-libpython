from lib_agent.wrapper.agent_wrapper import PlatformWrapper, AgentWrapper
from lib_agent.rest import ApiException
import sys
import time

def main():
    ip = sys.argv[1]
    port = sys.argv[2]
    a = int(sys.argv[3])
    b = int(sys.argv[4])
    platform = PlatformWrapper(ip, port)
    ag = platform.get_agent("Adder",strict=False)
    acum = 0
    for _ in range(b):
        acum = int(ag.sendToAgent(f'{acum} {a}'))
        time.sleep(2)
    
    print(acum)
    




if __name__ == '__main__':
    main()
