# BenfordLawAnalyzer
This small project aims to show how to spot anomalies in a dataset using the Benford's Law and few lines of Python

------

Steps to use the code with your own dataset:

1) Select the right column with pandas library:
2) Use the Benford class to analyze it and plot the histogram
3) Calculate the correlation

Note that using Benford's Law for spot data anomalies is only suitable in particular conditions:

- *Sample Size*: if the sample size is too small, the distribution of the leading digits may not follow the expected pattern.
- *Selection Bias*: the dataset needs to be representative of the population it is drawn from, otherwise it may not follow Benford’s Law.
- *Leading Digit Preference*: Benford’s Law assumes that people are equally likely to report any leading digit, i.e. each number 1 through 9 should have an equal chance of being the leading digit.



#### **More details in the Medium article.**



### System Requirements

- Python 3.10
- Numpy 1.23.5
- Pandas 1.5.2



------

#### Datasets

The datasets used for the tests come from Kaggle

- [*6,000 Largest Companies Ranked by Market Cap* by KANAWATTANACHAI](https://www.kaggle.com/datasets/prasertk/6000-largest-companies-ranked-by-market-cap)
- [*Covid-19 Data Deaths and Vaccinations* by DIGVIJAYSINH GOHIL](https://www.kaggle.com/datasets/digvijaysinhgohil/covid19-data-deaths-and-vaccinations)
- [*Worldwide deaths by country/risk factors* by ARPIT VERMA](https://www.kaggle.com/datasets/varpit94/worldwide-deaths-by-risk-factors)
- [*GoodReads 100k books* by MANAV DHAMANI](https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k)
- [*Stars from Gaia DR2 and RAVE DR5* by JOSÉ H. SOLÓRZANO](https://www.kaggle.com/datasets/solorzano/rave-dr5-gaia-dr2-consolidated)
- [*World Population 1960–2018* by DEVAKUMAR K. P.](https://www.kaggle.com/datasets/imdevskp/world-population-19602018)



#### Bibliography

- Frank Benford (March 1938). “[The law of anomalous numbers](https://www.jstor.org/stable/984802)“. *Proc. Am. Philos. Soc.* 78 (4): 551–572.
- [Using Excel and Benford’s Law to detect fraud](https://www.journalofaccountancy.com/issues/2017/apr/excel-and-benfords-law-to-detect-fraud.html) By J. Carlton Collins, CPA April 1, 2017
- [Breaking the (Benford) Law: Statistical Fraud Detection in Campaign Finance](http://cho.pol.illinois.edu/wendy/papers/tas.pdf), by Wendy K. Tam Cho and Brian J. Gaines
- [Emergence of Benford’s Law in Classical Music](https://www.arxiv-vanity.com/papers/1805.06506/), Azar Khosravani and Constantin Rasinariu
