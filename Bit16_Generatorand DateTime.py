from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

def gen_special_pybites_dates():
    
    next_date =  datetime(year=2016, month=12, day=19)  #creates local object PYBITES_BORN, so we can mutate it
    hundred_days =timedelta(days = 100)
    
    while True:
        next_date += hundred_days    
        yield next_date

'''
Want the following output:
def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 10))
    expected = [datetime(2017, 3, 29, 0, 0),
                datetime(2017, 7, 7, 0, 0),
                datetime(2017, 10, 15, 0, 0),
                datetime(2018, 1, 23, 0, 0),
                datetime(2018, 5, 3, 0, 0),
                datetime(2018, 8, 11, 0, 0),
                datetime(2018, 11, 19, 0, 0),
                datetime(2019, 2, 27, 0, 0),
                datetime(2019, 6, 7, 0, 0),
                datetime(2019, 9, 15, 0, 0)]
    assert dates == expected


'''