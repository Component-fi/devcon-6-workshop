import dune
import graph
import process
import transaction

def main():
    graph_prices = graph.get_prices()
    dune_prices = dune.get_prices()
    buy_graph = process.process_data(graph_prices)
    buy_dune = process.process_data(dune_prices)
    if (buy_graph and buy_dune):
        transaction.buy()