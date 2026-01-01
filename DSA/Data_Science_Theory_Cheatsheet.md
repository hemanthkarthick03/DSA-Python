# Data Science Theory Cheatsheet 📊

## Statistics Fundamentals 📈

### Descriptive Statistics 📋
- **Mean (μ)** 🎯: Average value of dataset
- **Median** 🏠: Middle value when data is sorted
- **Mode** 🔄: Most frequently occurring value
- **Standard Deviation (σ)** 📏: Measure of data spread
- **Variance (σ²)** 📐: Square of standard deviation
- **Skewness** ⚖️: Measure of asymmetry in distribution
- **Kurtosis** 🏔️: Measure of tail heaviness in distribution

### Probability Distributions 🎲
- **Normal Distribution** 🔔: Bell-shaped, symmetric (68-95-99.7 rule)
- **Binomial Distribution** 🪙: Success/failure trials (coin flips)
- **Poisson Distribution** ⏰: Rate of events over time/space
- **Exponential Distribution** ⚡: Time between events
- **Uniform Distribution** 📏: All outcomes equally likely
- **Chi-Square Distribution** ✖️: Sum of squared normal variables

### Central Limit Theorem 🎯
- **Key Point**: Sample means approach normal distribution as n increases
- **Magic Number**: n ≥ 30 for CLT to apply
- **Formula**: σ_x̄ = σ/√n (standard error)

## Hypothesis Testing 🧪

### Test Types 🔬
- **One-sample t-test** 1️⃣: Compare sample mean to population mean
- **Two-sample t-test** 2️⃣: Compare two group means
- **Paired t-test** 👥: Compare before/after measurements
- **Chi-square test** ✖️: Test independence of categorical variables
- **ANOVA** 🎭: Compare multiple group means
- **Mann-Whitney U** 🚫📊: Non-parametric alternative to t-test

### Key Concepts 🔑
- **Null Hypothesis (H₀)** ❌: No effect/difference exists
- **Alternative Hypothesis (H₁)** ✅: Effect/difference exists
- **p-value** 📊: Probability of observing data if H₀ is true
- **Alpha (α)** 🎯: Significance level (usually 0.05)
- **Type I Error** 🚨: False positive (reject true H₀)
- **Type II Error** 😴: False negative (fail to reject false H₀)
- **Power** 💪: Probability of correctly rejecting false H₀

## Machine Learning Fundamentals 🤖

### Learning Types 📚
- **Supervised Learning** 👨‍🏫: Learn from labeled data
  - Classification 🏷️: Predict categories
  - Regression 📈: Predict continuous values
- **Unsupervised Learning** 🔍: Find patterns in unlabeled data
  - Clustering 🎯: Group similar data points
  - Dimensionality Reduction 📉: Reduce feature space
- **Reinforcement Learning** 🎮: Learn through rewards/penalties

### Bias-Variance Tradeoff ⚖️
- **Bias** 🎯: Error from oversimplifying model
- **Variance** 📊: Error from sensitivity to training data
- **Underfitting** 📉: High bias, low variance
- **Overfitting** 📈: Low bias, high variance
- **Sweet Spot** 🎯: Balance both for optimal performance

### Cross-Validation 🔄
- **k-Fold CV** 📁: Split data into k parts, train on k-1, test on 1
- **Leave-One-Out** 1️⃣: Special case where k = n
- **Stratified CV** 📊: Maintain class proportions in splits
- **Time Series CV** ⏰: Respect temporal order in splits

## Classification Algorithms 🏷️

### Linear Models 📏
- **Logistic Regression** 📈: Uses sigmoid function for probability
- **Linear Discriminant Analysis** 📐: Finds linear decision boundary
- **Support Vector Machine** ⚔️: Finds optimal separating hyperplane

### Tree-Based Models 🌳
- **Decision Tree** 🌲: Recursive binary splits
- **Random Forest** 🌲🌲🌲: Ensemble of decision trees
- **Gradient Boosting** 🚀: Sequential weak learners
- **XGBoost** ⚡: Optimized gradient boosting

### Distance-Based Models 📏
- **k-Nearest Neighbors** 👥: Classify based on k closest points
- **Naive Bayes** 🎲: Assumes feature independence

### Neural Networks 🧠
- **Perceptron** ⚡: Single layer linear classifier
- **Multi-layer Perceptron** 🧠: Multiple hidden layers
- **Deep Learning** 🏗️: Many hidden layers

## Regression Algorithms 📈

### Linear Regression Family 📏
- **Simple Linear** ➡️: y = mx + b
- **Multiple Linear** ➡️➡️: y = β₀ + β₁x₁ + β₂x₂ + ...
- **Polynomial** 🌊: Non-linear relationships
- **Ridge Regression** 🏔️: L2 regularization (λΣβ²)
- **Lasso Regression** 🎯: L1 regularization (λΣ|β|)
- **Elastic Net** 🕸️: Combines L1 + L2 regularization

### Non-Linear Models 🌊
- **Decision Tree Regression** 🌳: Recursive splits for continuous target
- **Random Forest Regression** 🌲🌲🌲: Ensemble averaging
- **Support Vector Regression** ⚔️: Uses kernel trick for non-linearity

## Clustering Algorithms 🎯

### Partitioning Methods 📊
- **k-Means** 🎯: Minimize within-cluster sum of squares
- **k-Medoids** 🏠: Use actual data points as centers
- **Fuzzy c-Means** 🌫️: Soft clustering with membership degrees

### Hierarchical Methods 🌳
- **Agglomerative** ⬆️: Bottom-up clustering
- **Divisive** ⬇️: Top-down clustering
- **Dendrogram** 🌳: Tree visualization of clusters

### Density-Based Methods 🌊
- **DBSCAN** 🔍: Density-based spatial clustering
- **OPTICS** 👁️: Ordering points to identify clustering structure

## Dimensionality Reduction 📉

### Linear Methods 📏
- **Principal Component Analysis (PCA)** 🎯: Maximize variance
- **Linear Discriminant Analysis (LDA)** 📐: Maximize class separation
- **Independent Component Analysis (ICA)** 🔄: Find independent sources

### Non-Linear Methods 🌊
- **t-SNE** 🗺️: Preserve local neighborhood structure
- **UMAP** 🚀: Uniform manifold approximation
- **Kernel PCA** 🔄: PCA in higher dimensional space

## Model Evaluation Metrics 📊

### Classification Metrics 🏷️
- **Accuracy** 🎯: (TP + TN) / Total
- **Precision** 🔍: TP / (TP + FP) - "How many selected are relevant?"
- **Recall (Sensitivity)** 📡: TP / (TP + FN) - "How many relevant are selected?"
- **Specificity** 🛡️: TN / (TN + FP) - "How many irrelevant are rejected?"
- **F1-Score** ⚖️: 2 × (Precision × Recall) / (Precision + Recall)
- **AUC-ROC** 📈: Area under ROC curve
- **Confusion Matrix** 🤔: 2×2 table of predictions vs actual

### Regression Metrics 📈
- **Mean Absolute Error (MAE)** 📏: Average absolute differences
- **Mean Squared Error (MSE)** 📐: Average squared differences
- **Root Mean Squared Error (RMSE)** √📐: Square root of MSE
- **R-squared (R²)** 📊: Proportion of variance explained
- **Adjusted R²** 🔧: R² adjusted for number of features

## Feature Engineering 🔧

### Feature Selection 🎯
- **Filter Methods** 🔍: Statistical tests (correlation, chi-square)
- **Wrapper Methods** 📦: Use ML algorithm (forward/backward selection)
- **Embedded Methods** 🏗️: Built into algorithm (Lasso, tree importance)

### Feature Transformation 🔄
- **Scaling** 📏: StandardScaler, MinMaxScaler, RobustScaler
- **Encoding** 🏷️: One-hot, Label, Target encoding
- **Binning** 📊: Convert continuous to categorical
- **Log Transform** 📈: Handle skewed distributions
- **Polynomial Features** 🌊: Create interaction terms

## Data Preprocessing 🧹

### Missing Data Handling 🕳️
- **Deletion** ❌: Remove rows/columns with missing values
- **Mean/Median Imputation** 📊: Fill with central tendency
- **Mode Imputation** 🔄: Fill with most frequent value
- **Forward/Backward Fill** ➡️⬅️: Use previous/next value
- **KNN Imputation** 👥: Use similar observations
- **Multiple Imputation** 🔄🔄: Create multiple complete datasets

### Outlier Detection 🚨
- **Z-Score Method** 📊: |z| > 3 (assuming normal distribution)
- **IQR Method** 📦: Outside Q1 - 1.5×IQR or Q3 + 1.5×IQR
- **Isolation Forest** 🌳: Anomaly detection algorithm
- **Local Outlier Factor** 🎯: Density-based outlier detection

## Time Series Analysis ⏰

### Components 🧩
- **Trend** 📈: Long-term direction
- **Seasonality** 🔄: Regular patterns (daily, weekly, yearly)
- **Cyclical** 🌊: Irregular long-term patterns
- **Noise** 📻: Random variation

### Stationarity 📊
- **Stationary Series** ⚖️: Constant mean, variance, covariance
- **Augmented Dickey-Fuller Test** 🧪: Test for stationarity
- **Differencing** ➖: Remove trend to achieve stationarity

### Forecasting Models 🔮
- **ARIMA** 📈: AutoRegressive Integrated Moving Average
- **SARIMA** 🔄: Seasonal ARIMA
- **Exponential Smoothing** 📉: Weighted averages
- **Prophet** 🔮: Facebook's forecasting tool

## Deep Learning Basics 🧠

### Neural Network Components ⚡
- **Neuron** 🔵: Basic processing unit
- **Weights** ⚖️: Connection strengths
- **Bias** 🎯: Threshold adjustment
- **Activation Functions** 🔥: ReLU, Sigmoid, Tanh
- **Loss Function** 📉: Measure prediction error
- **Optimizer** 🚀: Update weights (SGD, Adam)

### Network Types 🏗️
- **Feedforward** ➡️: Information flows forward only
- **Convolutional (CNN)** 🖼️: For image processing
- **Recurrent (RNN)** 🔄: For sequential data
- **Long Short-Term Memory (LSTM)** 🧠: Advanced RNN
- **Transformer** 🔄: Attention-based architecture

## Ensemble Methods 🎭

### Bagging 👜
- **Bootstrap Aggregating** 🎒: Train on bootstrap samples
- **Random Forest** 🌲🌲🌲: Bagging + random feature selection
- **Extra Trees** 🌳: Extremely randomized trees

### Boosting 🚀
- **AdaBoost** 📈: Adaptive boosting
- **Gradient Boosting** 📊: Sequential error correction
- **XGBoost** ⚡: Extreme gradient boosting
- **LightGBM** 💡: Light gradient boosting

### Stacking 📚
- **Meta-learner** 🎓: Learn from base model predictions
- **Blending** 🌀: Simple averaging of predictions

## Model Selection & Tuning 🎛️

### Hyperparameter Tuning 🔧
- **Grid Search** 🔍: Exhaustive search over parameter grid
- **Random Search** 🎲: Random sampling of parameters
- **Bayesian Optimization** 🧠: Smart parameter search
- **Genetic Algorithm** 🧬: Evolution-based optimization

### Model Selection Criteria 📊
- **AIC** 📈: Akaike Information Criterion
- **BIC** 📊: Bayesian Information Criterion
- **Cross-Validation Score** 🔄: Average performance across folds
- **Learning Curves** 📈: Plot training vs validation error

## Statistical Concepts 📊

### Correlation vs Causation ⚖️
- **Correlation** 🔗: Variables move together
- **Causation** ➡️: One variable causes another
- **Confounding Variables** 🌪️: Hidden factors affecting both
- **Simpson's Paradox** 🔄: Trend reverses when data is grouped

### Sampling 🎯
- **Simple Random** 🎲: Each item has equal probability
- **Stratified** 📊: Maintain population proportions
- **Systematic** 📏: Every kth item
- **Cluster** 🎯: Sample entire groups
- **Convenience** 🤷: Easy to collect samples

### Experimental Design 🧪
- **Control Group** 🛡️: No treatment applied
- **Treatment Group** 💊: Receives intervention
- **Randomization** 🎲: Random assignment to groups
- **Blinding** 👁️: Participants don't know group assignment
- **Double-Blind** 👁️👁️: Neither participants nor researchers know

## Business Intelligence 💼

### KPIs & Metrics 📊
- **Conversion Rate** 💰: Visitors who take desired action
- **Customer Lifetime Value (CLV)** 💎: Total value from customer
- **Churn Rate** 📉: Rate of customer attrition
- **A/B Testing** 🧪: Compare two versions
- **Cohort Analysis** 👥: Track user groups over time

### Data Quality 🏆
- **Completeness** ✅: No missing values
- **Accuracy** 🎯: Values are correct
- **Consistency** 🔄: Same format across dataset
- **Timeliness** ⏰: Data is up-to-date
- **Validity** ✔️: Data follows business rules

## Ethics & Bias 🤝

### Types of Bias 🚨
- **Selection Bias** 🎯: Non-representative sample
- **Confirmation Bias** ✅: Seeking confirming evidence
- **Survivorship Bias** 🏆: Only considering successful cases
- **Algorithmic Bias** 🤖: Unfair ML model decisions
- **Sampling Bias** 📊: Systematic error in sample selection

### Fairness Metrics ⚖️
- **Demographic Parity** 👥: Equal positive rates across groups
- **Equalized Odds** ⚖️: Equal TPR and FPR across groups
- **Individual Fairness** 👤: Similar individuals get similar outcomes

## Quick Reference Formulas 📐

### Statistics 📊
- **Standard Error**: SE = σ/√n
- **Confidence Interval**: x̄ ± z(α/2) × SE
- **Cohen's d**: d = (μ₁ - μ₂)/σ_pooled
- **Correlation**: r = Σ(x-x̄)(y-ȳ)/√[Σ(x-x̄)²Σ(y-ȳ)²]

### Machine Learning 🤖
- **Precision**: TP/(TP+FP)
- **Recall**: TP/(TP+FN)
- **F1-Score**: 2×(Precision×Recall)/(Precision+Recall)
- **Accuracy**: (TP+TN)/(TP+TN+FP+FN)

### Information Theory 📡
- **Entropy**: H(X) = -Σp(x)log₂p(x)
- **Information Gain**: IG = H(parent) - Σ(|child|/|parent|)×H(child)
- **Gini Impurity**: 1 - Σp(x)²

## Memory Tricks 🧠

### Statistical Tests 🧪
- **t-test** ☕: "Tea for Two" (compare means)
- **Chi-square** ✖️: "Chi-squared for Categories"
- **ANOVA** 🎭: "Analysis of Variance for Multiple groups"
- **F-test** 🏁: "F for comparing Variances"

### ML Algorithm Selection 🎯
- **Linear** 📏: Simple, interpretable, fast
- **Tree** 🌳: Non-linear, interpretable, handles mixed data
- **SVM** ⚔️: High-dimensional, kernel trick
- **Neural** 🧠: Complex patterns, needs lots of data
- **Ensemble** 🎭: Better performance, less interpretable

### Remember the 3 V's of Big Data 📊
- **Volume** 📈: Amount of data
- **Velocity** ⚡: Speed of data
- **Variety** 🌈: Types of data

This cheatsheet provides quick reference points for mastering data science theory! 🚀