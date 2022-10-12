from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import pandas as pd

def get_prices():
  # USDC 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48
  # WETH 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2

  # Select your transport with a defined url endpoint
  transport = AIOHTTPTransport(url="https://api.thegraph.com/subgraphs/name/openpredict/chainlink-prices-subgraph")

  # Create a GraphQL client using the defined transport
  client = Client(transport=transport, fetch_schema_from_transport=True)

  # Provide a GraphQL query
  query = gql(
      """
      query MyQuery {
    prices(where: {assetPair: "ETH/USD"}, orderBy: timestamp, orderDirection: desc, first: 1000){
      timestamp,
      price,
    }
  }
  """
  )

  # Execute the query on the transport
  result = client.execute(query)
  df = pd.DataFrame(result['prices'])

  # Now we need to resample our data so that there is only 1 per hour
  df['Datetime'] = df['time']

  df.set_index('Datetime', inplace=True)

  sample = df.resample('1H').last()

  print(len(sample))
  return sample