from storage import Database
import network


def main():
    run()


def run():
    result = network.run_speedtest()

    db = Database.from_config()
    db.connect()
    db.add_speedtest(result)


if __name__ == '__main__':
    main()
