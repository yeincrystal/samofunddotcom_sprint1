from portfolio.models import Samofund

def get_db():
    import csv
    from portfolio.models import Samofund
    with opne('samofund_db.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = Samofund(company_name=row['\ufeffcompany_name'],fund_name=row['fund_name'],initial_date=row['initial_date'],m_strategy=row['m_strategy'],pbs=row['pbs'],setting=row['setting'],total_net_profit=row['total_net_profit'],modified_base=row['modified_base'],june_perf=row['june_perf'],week_perf=row['week_perf'],pday_perf=row['pday_perf'],perf_2019=row['perf_2019'],year_conv_perf=row['year_conv_perf'],cum_perf=row['cum_perf'])
            p.save()

    