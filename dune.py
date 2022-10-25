from duneanalytics import DuneAnalytics

def get_prices():
    dune = DuneAnalytics('devcon', 'devcon123456789!')

    # try to login
    dune.login()

    # fetch token
    dune.fetch_auth_token()

    # fetch query result id using query id
    result_id = dune.query_result_id(query_id=1390331)

    # fetch query result
    data = dune.query_result(result_id)

    import pandas as pd

    def beta(row):
        return row['data']

    data1 = (data['data']['get_result_by_result_id'])
    data2 = map(beta, data1)
    data3 = list(data2)

    df = pd.DataFrame(data3)

    df['time'] =  pd.to_datetime(df['minute'], infer_datetime_format=True)
    df = df.drop('minute', axis=1)

    # data viz
    import datetime

    # Reset index
    df = df[::-1].reset_index(drop = True)

    # for simpliciting let's just keep average eth:usd price per hour (get rid of all other columns)
    df = df.drop('maximum', axis=1)
    df = df.drop('min', axis=1)

    df = df.rename(columns={'time': 'Datetime', 'average': 'price'})
    df.set_index('Datetime', inplace = True)
    print(df)
    return df

if __name__ == "__main__":
    get_prices()