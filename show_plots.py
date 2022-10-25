import dune
import process

def main():
    dune_prices = dune.get_prices()
    process.process_data(dune_prices)

if __name__ == "__main__":
    main()