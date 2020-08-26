from database import Database
import speedtest


def main():
    result = speedtest.run_speedtest()

    db = Database('database.db')
    db.connect()
    db.add_speedtest(result.as_tuple)


if __name__ == '__main__':
    main()