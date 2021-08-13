<p style="text-align: justify;"><span style="color: #000000;">I Collecting environmental data from Json Api Hourly meteostat</span><br /><span style="color: #000000;">with a subscription-free account.</span><br /><span style="color: #000000;">for the data column can refer to the following <a href="https://dev.meteostat.net/api/point/hourly.html#endpoint"><strong>link</strong></a> (response)</span><br /><span style="color: #000000;"><a href="https://dev.meteostat.net/api/point/hourly.html#endpoint">https://dev.meteostat.net/api/point/hourly.html#endpoint</a></span></p>

I made 2 scripts app.py and appThredpool.py for app.py managed to collect data, to optimize data collection time I added multi threads in appThreadpool.py but my api uses free acc so there is a time limit access api there was a response from api meteostat that it was too fast to access the API because multi thread

we can use correlation to find relationships in the dataset as in correlation.py 
in this example i'm using pearson correlation to find relationship between dataset

The Pearson Correlation coefficient can be computed in Python using corrcoef() method from Numpy.

The input for this function is typically a matrix, say of size mxn, where:

Each column represents the values of a random variable
Each row represents a single sample of n random variables
n represent the total number of different random variables
m represents the total number of samples for each variable
For n random variables, it returns an nxn square matrix M, with M(i,j) indicating the correlation coefficient between the random variable i and j. As the correlation coefficient between a variable and itself is 1, all diagonal entries (i,i) are equal to one.