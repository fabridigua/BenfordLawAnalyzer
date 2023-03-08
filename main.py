from Benford import Benford

if __name__ == '__main__':

    benford = Benford()

    # List of largest companies in the world by marker cap
    # Original dataset: https://www.kaggle.com/datasets/prasertk/6000-largest-companies-ranked-by-market-cap
    # Total values: 5929
    benford.analyze('datasets\\6000 Largest Companies ranked by Market Cap.csv', 'marketcap', 'Largest companies market cap')
    print(benford.calculateCorrelation())
    benford.manipulateV2()
    benford.reanalyze()
    print(benford.calculateCorrelation())

    # Total cases of Covid-19 worldwide over a time frame of February 2020 till May 2022
    # Original dataset: https://www.kaggle.com/datasets/digvijaysinhgohil/covid19-data-deaths-and-vaccinations
    # Total values: 183583
    benford.analyze('datasets\\covid_data_cleaned.csv', 'total_cases', 'Cases of Covid-19 worldwide')
    print(benford.calculateCorrelation())
    benford.manipulateV2()
    benford.reanalyze()
    print(benford.calculateCorrelation())

    # Total annual deaths for smoking around the world in period 1990-2017
    # Original dataset: https://www.kaggle.com/datasets/varpit94/worldwide-deaths-by-risk-factors
    # Total values: 6468
    benford.analyze('datasets\\number-of-deaths-by-risk-factor.csv', 'Smoking', 'Annual deaths for smoking')
    print(benford.calculateCorrelation())
    benford.manipulateV2()
    benford.reanalyze()
    print(benford.calculateCorrelation())

    # Total rating of 100k GoodReads books
    # Original dataset: https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k
    # Total values: 100000
    benford.analyze('datasets\\GoodReads_100k_books.csv', 'totalratings', 'Ratings received by GoodReads books')
    print(benford.calculateCorrelation())
    benford.manipulateV2()
    benford.reanalyze()
    print(benford.calculateCorrelation())

    # Distance to Earth of 250k stars (measured by Gaia DR1)
    # Original dataset: https://www.kaggle.com/datasets/solorzano/rave-dr5-gaia-dr2-consolidated
    # Total values: 253040
    benford.analyze('datasets\\gaia-dr2-rave-35.csv', 'r_distance', 'Distance to Earth of 250k stars')
    print(benford.calculateCorrelation())
    benford.manipulateV2()
    benford.reanalyze()
    print(benford.calculateCorrelation())

    # World population in period 1960-2018 by country
    # Original dataset: https://www.kaggle.com/datasets/imdevskp/world-population-19602018
    # Total values: 12595
    benford.analyze('datasets\\population_total_long.csv', 'Count', 'World population (1960-2018)')
    print(benford.calculateCorrelation())
    benford.manipulateV2()
    benford.reanalyze()
    print(benford.calculateCorrelation())