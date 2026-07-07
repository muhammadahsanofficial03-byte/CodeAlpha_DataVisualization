import pandas as pd
import plotly.express as px
import plotly.io as pio

# Load the dataset
# Ensure 'tested.csv' is in the same folder as this script
df = pd.read_csv('tested.csv')

# 1. Survival Rate by Sex
# This helps us see if gender played a role in survival (a famous Titanic fact)
fig_sex = px.bar(df, x='Sex', color='Survived', barmode='group', 
                 title='Survival Distribution by Sex',
                 labels={'Survived': 'Survived (0=No, 1=Yes)'})

# 2. Survival Rate by Passenger Class (Pclass)
# This reveals if wealth/ticket class affected survival chances
fig_class = px.bar(df, x='Pclass', color='Survived', barmode='group',
                   title='Survival Distribution by Class',
                   labels={'Pclass': 'Ticket Class'})

# 3. Age Distribution
# Shows the age demographics of the passengers
fig_age = px.histogram(df, x='Age', nbins=20, 
                       title='Age Distribution of Passengers',
                       template='plotly_white')

# 4. Fare Distribution (Box Plot)
# Helps identify outliers in ticket prices
fig_fare = px.box(df, y='Fare', title='Distribution of Ticket Fares')

# To display these, you can show them one by one
fig_sex.show()
fig_class.show()
fig_age.show()
fig_fare.show()