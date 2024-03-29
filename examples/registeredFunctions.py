import lib_agent
import sys
import time


def main():
    ip = sys.argv[1]
    port = sys.argv[2]
    platform = lib_agent.PlatformWrapper(ip, port)
    while True:
        functions = platform.get_all_functions()
        print(functions)
        time.sleep(10)

if __name__ == '__main__':
    main()