import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.semi_supervised.tests.test_self_training import y_train

"""### Notebook Presentation"""

pd.options.display.float_format = '{:,.2f}'.format

data = pd.read_csv('boston.csv', index_col=0)

"""### Understand the Boston House Price Dataset

---------------------------

**Characteristics:**  

    :Number of Instances: 506 

    :Number of Attributes: 13 numeric/categorical predictive. The Median Value (attribute 14) is the target.

    :Attribute Information (in order):
        1. CRIM     per capita crime rate by town
        2. ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        3. INDUS    proportion of non-retail business acres per town
        4. CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        5. NOX      nitric oxides concentration (parts per 10 million)
        6. RM       average number of rooms per dwelling
        7. AGE      proportion of owner-occupied units built prior to 1940
        8. DIS      weighted distances to five Boston employment centres
        9. RAD      index of accessibility to radial highways
        10. TAX      full-value property-tax rate per $10,000
        11. PTRATIO  pupil-teacher ratio by town
        12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        13. LSTAT    % lower status of the population
        14. PRICE     Median value of owner-occupied homes in $1000's

"""

# Preliminary Data Exploration
print(data.shape)

print(data.columns)

"""## Data Cleaning - Check for Missing Values and Duplicates"""

print(data.head())

print(data.tail())

# Check for Missing Values
print(data.info())
print(data.count())

# Check NaN values
print(data.isna().values.any())

# Check any duplitaes
print(data.duplicated().values.any())

"""## Descriptive Statistics"""

# Descriptive Statistics
print(data.describe())

"""## Visualise the Features"""

sns.displot(data['PRICE'],
            bins=50,
            aspect=2,
            kde=True,
            color='#2196f3')
plt.title(f'1970s home values in Boston. Average: ${(1000 * data.PRICE.mean()):.6}')
plt.xlabel('Price in 000s')
plt.ylabel('Nr. of Homes')
plt.show()


# Distance to Employment - Length of Commute
sns.displot(data.DIS,
            bins=50,
            aspect=2,
            kde=True,
            color='darkblue')
plt.title(f'Distance to emplyment centres. Average: {(data.DIS.mean()):.2}')
plt.xlabel('Weighted Distance to 5 Boston Employment Centres')
plt.ylabel('Nr.of homes')
plt.show

"""#### Number of Rooms"""

# Number of Rooms
sns.displot(data.RM,
            aspect=2,
            kde=True,
            color='#00796b')
plt.title = (f'Distribution of rooms in Boston {data.RM.mean():.2}')
plt.xlabel('Average number of romms')
plt.ylabel('Nr. of homes')
plt.show()

"""#### Access to Highways 🛣"""

# Access to Highways
plt.figure(figsize=(14, 8), dpi=200)
plt.hist(data['RAD'],
         bins=24,
         ec='red',
         color='#7b1fa2',
         rwidth=2)
plt.xlabel('Accessibility to Highways')
plt.ylabel('Nr. of Houses')
plt.show()

"""#### homes are away from the river versus next to it? ⛵️"""

river = data['CHAS'].value_counts()
print(river)

# bar chart with plotly for CHAS to show many more homes are away from the river versus next to it.
bar = px.bar(x=['No', 'Yes'],
             y=river.values,
             color=river.values,
             color_continuous_scale=px.colors.sequential.haline,
             title='Next to Charles River')
bar.update_layout(xaxis_title='Property Located next to the River?',
                  yaxis_title='Number of Homes',
                  coloraxis_showscale=False)
bar.show()

# Pair Plot
sns.pairplot(data)
plt.show()

# with regresion line
sns.pairplot(data, kind='reg', plot_kws={'line_kws': {'color': 'cyan'}})
plt.show()


# Compare DIS (Distance from employment) with NOX (Nitric Oxide Pollution) using Seaborn's .jointplot()
with sns.axes_style('darkgrid'):
    sns.jointplot(x=data['DIS'],
                  y=data['NOX'],
                  height=8,
                  kind='scatter',
                  color='deeppink',
                  joint_kws={'alpha': 0.5})
plt.show()

# Compare INDUS (the proportion of non-retail industry i.e., factories) with NOX (Nitric Oxide Pollution) using Seaborn's .jointplot()
with sns.axes_style('darkgrid'):
    sns.jointplot(x=data['NOX'],
                  y=data['INDUS'],
                  height=8,
                  kind='hist',
                  color='darkgreen',
                  joint_kws={'alpha': 0.5})
plt.show()

# Compare LSTAT (proportion of lower-income population) with RM (number of rooms) using Seaborn's .jointplot().
with sns.axes_style('darkgrid'):
    sns.jointplot(x=data['LSTAT'],
                  y=data['RM'],
                  color='orange',
                  height=8,
                  kind='hex',
                  joint_kws={'alpha': 0.5})
plt.show()

# Compare LSTAT with PRICE using Seaborn's .jointplot()
with sns.axes_style('darkgrid'):
    sns.jointplot(x=data['LSTAT'],
                  y=data['PRICE'],
                  color='crimson',
                  height=8,
                  kind='hex',
                  joint_kws={'alpha': 0.5})
plt.show()

# Compare RM (number of rooms) with PRICE using Seaborn's .jointplot()
with sns.axes_style('darkgrid'):
    sns.jointplot(x=data['RM'],
                  y=data['PRICE'],
                  color='darkblue',
                  height=8,
                  kind='scatter',
                  joint_kws={'alpha': 0.5})
plt.show()

"""# Split Training & Test Dataset"""

from sklearn.model_selection import train_test_split
target = data['PRICE']
features = data.drop('PRICE', axis=1)
X_train,X_test,Y_train,Y_test = train_test_split(features,
                                                 target,
                                                 test_size=0.2,
                                                 random_state=10
                                            )

print(X_train)
print(X_test)

# % of training set
train_pct = 100*len(X_train)/len(features)
print(f'Training data {train_pct:.3}% of the total data.')
# % of test data set
test_pct = 100*X_test.shape[0]/features.shape[0]
print(f'Test data makes up the remaining {test_pct:0.3}%')

"""# Multivariable Regression
regression on the training dataset. How high is the r-squared for the regression on the training data?"""

regr = LinearRegression()
regr.fit(X_train, Y_train)
rsquared = regr.score(X_train, Y_train)
print(f'Training data r_squared: {rsquared:.2}')

"""### Evaluate the Coefficients of the Model"""

regr_coef = pd.DataFrame(data=regr.coef_, index=X_train.columns, columns=['Coefficient'])
print(regr_coef)

"""### Analyse the Estimated Values & Regression Residuals"""

predicted_vals = regr.predict(X_train)
residuals = (Y_train - predicted_vals)

#Original regression of actual vs predicted prices
plt.figure(dpi=100)
plt.scatter(x=Y_train,
            y=predicted_vals,
            c='indigo',
            alpha=0.6)
plt.plot(Y_train,
         Y_train,
         color='cyan')
# plt.title('Actual vs predicted prices', fontsize=17)
plt.xlabel('Actual prices 000s',fontsize=14)
plt.ylabel('Predicted prices 000s', fontsize=14)
plt.show()

#Residuals vs predicted values
plt.figure(dpi=100)
plt.scatter(x=predicted_vals,
            y=residuals,
            c='indigo',
            alpha=0.6)
# plt.title('Residuals vs predicted values', fontsize=17)
plt.xlabel('Predicted Prices', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Residual distribution chart
resid_mean = round(residuals.mean(),2)
resid_skew = round(residuals.skew(),2)
sns.displot(residuals, kde=True, color='indigo')
plt.show()


"""#### How does the log transformation work?"""

plt.figure(dpi=150)
plt.scatter(data.PRICE, np.log(data.PRICE))

plt.title('Mapping the Original Price to a Log Price')
plt.ylabel('Log Price')
plt.xlabel('Actual $ Price in 000s')
plt.show()

#Data Transformations for a Better Fit
tgt_skew = data['PRICE'].skew()
sns.displot(data['PRICE'], kde='kde', color='green')
plt.title('Normal prices')
plt.show()

y_log = np.log(data['PRICE'])
sns.displot(y_log, kde=True)
plt.title('LOG Prices')
plt.show()

"""#### How does the log transformation work?"""

# the actual prices against the (transformed) log prices.
plt.figure(dpi=150)
plt.scatter(data.PRICE, np.log(data.PRICE))

plt.title('Mapping the Original Price to a Log Price')
plt.ylabel('Log Price')
plt.xlabel('Actual $ Price in 000s')
plt.show()



"""## Regression using Log Prices"""

#Regression using Log Prices
new = np.log(data['PRICE'])
features = data.drop('PRICE',axis=1)

X_train,X_test, log_y_train, log_y_test = train_test_split(features,
                                                           new,
                                                           test_size=0.2,
                                                           random_state=10)
log_regr = LinearRegression()
log_regr.fit(X_train,log_y_train)
log_rsquared = log_regr.score(X_train,log_y_train)
log_predictions = log_regr.predict(X_train)
log_residuals = (log_y_train - log_predictions)
print(f'Training data r-squared: {log_rsquared:.2}')

"""## Evaluating Coefficients with Log Prices"""

#Evaluating Coefficients with Log Prices
df_coef = pd.DataFrame(data=log_regr.coef_, index=X_train.columns, columns=['coef'])
print(df_coef)

"""## Regression with Log Prices & Residual Plots"""

# Graph of Actual vs. Predicted Log Prices
plt.scatter(x=log_y_train, y=log_predictions, c='navy', alpha=0.6)
plt.plot(log_y_train, log_y_train, color='cyan')
plt.title(f'Actual vs Predicted Log Prices: $y _i$ vs $\hat y_i$ (R-Squared {log_rsquared:.2})', fontsize=17)
plt.xlabel('Actual Log Prices $y _i$', fontsize=14)
plt.ylabel('Prediced Log Prices $\hat y _i$', fontsize=14)
plt.show()

# Original Regression of Actual vs. Predicted Prices
plt.scatter(x=y_train, y=predicted_vals, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Original Actual vs Predicted Prices: $y _i$ vs $\hat y_i$ (R-Squared {rsquared:.3})', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\hat y _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values (Log prices)
plt.scatter(x=log_predictions, y=log_residuals, c='navy', alpha=0.6)
plt.title('Residuals vs Fitted Values for Log Prices', fontsize=17)
plt.xlabel('Predicted Log Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.scatter(x=predicted_vals, y=residuals, c='indigo', alpha=0.6)
plt.title('Original Residuals vs Fitted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Distribution of Residuals (log prices) - checking for normality
log_resid_mean = round(log_residuals.mean(), 2)
log_resid_skew = round(log_residuals.skew(), 2)

sns.displot(log_residuals, kde=True, color='navy')
plt.title(f'Log price model: Residuals Skew ({log_resid_skew}) Mean ({log_resid_mean})')
plt.show()

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Original model: Residuals Skew ({resid_skew}) Mean ({resid_mean})')
plt.show()

"""# Compare Out of Sample Performance"""

print(f'Original Model Test Data r-squared: {regr.score(X_test, Y_test):.2}')
print(f'Log Model Test Data r-squared: {log_regr.score(X_test, log_y_test):.2}')

"""# Predict a Property's Value using the Regression Coefficients"""

# Starting Point: Average Values in the Dataset
features = data.drop(['PRICE'], axis=1)
average_vals = features.mean().values
property_stats = pd.DataFrame(data=average_vals.reshape(1, len(features.columns)),
                              columns=features.columns)
print(property_stats)

# Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Acutal Dollar Values
dollar_est = np.e**log_estimate * 1000

# or use
dollar_est = np.exp(log_estimate) * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')

# Define Property Characteristics
next_to_river = True
nr_rooms = 8
students_per_classroom = 20
distance_to_town = 5
pollution = data.NOX.quantile(q=0.75) # high
amount_of_poverty =  data.LSTAT.quantile(q=0.25) # low

#Solution
# Set Property Characteristics
property_stats['RM'] = nr_rooms
property_stats['PTRATIO'] = students_per_classroom
property_stats['DIS'] = distance_to_town

if next_to_river:
    property_stats['CHAS'] = 1
else:
    property_stats['CHAS'] = 0

property_stats['NOX'] = pollution
property_stats['LSTAT'] = amount_of_poverty

## Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Acutal Dollar Values
dollar_est = np.e**log_estimate * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')