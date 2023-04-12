import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from sklearn.metrics import classification_report
from tensorflow.keras.utils import to_categorical
import numpy as np

# 1 Load the data
data = pd.read_csv('heart_failure.csv')

# 2 print columns and types
print(data.info())

# 3 distribution of death event using collections.Counter
print(Counter(data.death_event))

# 4 extract the label column 'death_event' from the 'data'
# DataFrame
y = data['death_event']
 
# 5 Extract features columns from data DF
x = data[['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time']]

# --- Data Preprocessing
# 6 convert categorical features to one hot encoding vectors
x = pd.get_dummies(x)

# 7, split data into training features, test features
# training labels and test labels respectively
# set test_size to be the % of data to be set to test 
# use any value for random_state
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# 8, Initialize a ColumnTransformer object by using 
# StandardScaler to scale the numeric features in the dataset
ct = ColumnTransformer([("numeric", StandardScaler(), ['age','creatinine_phosphokinase','ejection_fraction','platelets','serum_creatinine','serum_sodium','time'])])

# 9 - 10 use ColumnTransformer.fit_transform() function to
# train the scaler instance (ct) on the training data
# (X_train)
# (do the same for X_test w/ ConsumerTransformer.transform())
X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)

# --- Prepare labels for classification.

# 11, initialize an instance of LabelEncoder
le = LabelEncoder()

# 12/13, use LabelEncoder.fit_transform() function
# fit the encoder instance (le) to the training labels
# (Y_train) while converting the training labels 
# according to the trained encoder
# (do the same for Y_test w/ LabelEncoder.transform())
Y_train = le.fit_transform(Y_train.astype(str))
Y_test = le.transform(Y_test.astype(str))

# 14/15, use tensorflow.keras.utils.to_categorical() to
# transform the encoded training and test labels into
# binary vectors
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)

# --- Design the model
# 16 initialize tensorflow.keras.models.Sequential model i
# instance
model = Sequential()

# 17, create input layer instance of
# tensorflow.keras.layers.InputLayer and add it to model 
# w/ Model.add()
model.add(InputLayer(input_shape=(X_train.shape[1],)))

# 18, create hidden layer instance of
# tensorflow.keras.layers.Dense w/ 'relu' activation
# and 12 neurons. 
model.add(Dense(12, activation='relu'))

# 19, create an output layer instance of
# tensorflow.keras.layers.Dense w/ a softmax activation
# function (for classification) w/ the number of
# neurons corresponding to the no. of classes in the 
# data set. 
model.add(Dense(2, activation='softmax'))

# 20, compile the model w/ Model.compile() using
# the categorical_crossentropy loss function, 
# adam optimizer and accuracy metrics
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# ---- Train and evaluate the model
# 21, use Model.fit() function to fit the model instance
# to the training data (X_train) and training lables (Y_train)
# epochs 100, batch_size 16
model.fit(X_train, Y_train, epochs = 100, batch_size = 16, verbose = 1)

# 22, evaluate the function w/ Model.evaluate() using the
# trained model instance on the test data and labels (X_test, Y_test)
loss, acc = model.evaluate(X_test, Y_test, verbose=0)
print("Loss", loss, "Accuracy:", acc)

# 23, use Model.predict() to get predictions for the test data, X_test w/ the
# trained model instance
y_estimate = model.predict(X_test, verbose=0)

# 24, use numpy.argmax() to select indices of the true classes
# for each label encoding in y_estimate
# do the same for each label encoding in Y_test
y_estimate = np.argmax(y_estimate, axis=1)
y_true = np.argmax(Y_test, axis=1)

# Print additional metrics w/ classification_report
print(classification_report(y_true, y_estimate))