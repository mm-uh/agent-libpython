import lib_agent
import sys
import time
from random import randint


def main():
    ip = sys.argv[1]
    port = sys.argv[2]
    platform = lib_agent.PlatformWrapper(ip, port)
    while True:
        try:
            functions = platform.get_all_functions()
            if len(functions) == 0:
                print("There are not registered functions")
                continue
            index = randint(0, len(functions)-1)
            print("Getting agents of function "+ functions[index])
            agents = platform.get_agent_by_function(functions[index])
            print(agents)
        except Exception as e:
            print("Error " + str(e))
        time.sleep(10)
        

if __name__ == '__main__':
    main()