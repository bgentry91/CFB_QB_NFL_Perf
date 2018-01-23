# CFB_QB_NFL_Perf
For this project, I am attempting to predict college football quarterback performance in their first year in the NFL. The response variable is the first year passer rating of a given quarterback and I am using a number of their college football stats to attempt to predict this.

I am currently using an Elastic Net regularization on a linear model - an example of predicted vs actual values for a testing set can be seen below. Currently the model has an R^2 value around .35, but it tends to predict values relatively close to the mean, indicating that it is somewhat underfit. I believe this underfitting is due to a lack of strong relationships between my features & response.
(https://github.com/bgentry91/CFB_QB_NFL_Perf/blob/master/images/ElasticNet_PredvsAct.png)

Also below is a residual plot of the predicted values for a test set - the data looks to be mostly randomly distributed around the mean, which indicates the validity of the model.

(https://github.com/bgentry91/CFB_QB_NFL_Perf/blob/master/images/ElasticNet_Residuals.png)
