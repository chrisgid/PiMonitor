from storage import Database
import network


def main():
    result = network.run_speedtest()

    db = Database('database.db')
    db.connect()
    db.add_speedtest(result)


if __name__ == '__main__':
    main()
