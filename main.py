import Screen
import database
import AI

from server import Server
import Consts


def main():
    sv = Server(Consts.SERVER_HOST, Consts.SERVER_PORT)
    Server.run_server(sv)


if __name__ == "__main__":
    # main()
    print(AI.does_earn_more_than_7000_dollars())
