# Machine Learning Cheatsheet for Data Scientists

## Table of Contents
- [Environment Setup](#environment-setup)
- [Data Understanding & EDA](#data-understanding--eda)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Algorithm Selection Guide](#algorithm-selection-guide)
- [Model Training & Evaluation](#model-training--evaluation)
- [Advanced Techniques](#advanced-techniques)
- [Production & Deployment](#production--deployment)
- [Data Scientist Tricks](#data-scientist-tricks)

## Environment Setup

### Essential Libraries Installation
```bash
# Core Data Science Stack
pip install numpy pandas matplotlib seaborn jupyter

# Machine Learning
pip install scikit-learn xgboost lightgbm catboost

# Deep Learning
pip install tensorflow torch transformers

# Advanced Analytics
pip install statsmodels scipy plotly dash streamlit

# Model Interpretation
pip install shap lime eli5 yellowbrick

# Production Tools
pip install mlflow wandb optuna joblib pickle
```

### Quick Setup Template
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
```

## Data Understanding & EDA

### First Look at Data
```python
def quick_data_overview(df):
    """Get comprehensive data overview"""
    print("=" * 50)
    print("DATASET OVERVIEW")
    print("=" * 50)
    
    print(f"Shape: {df.shape}")
    print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    print("\nData Types:")
    print(df.dtypes.value_counts())
    
    print("\nMissing Values:")
    missing = df.isnull().sum()
    missing_pct = (missing / len(df)) * 100
    missing_df = pd.DataFrame({
        'Missing Count': missing,
        'Percentage': missing_pct
    }).sort_values('Percentage', ascending=False)
    print(missing_df[missing_df['Missing Count'] > 0])
    
    print("\nNumerical Columns Summary:")
    print(df.describe())
    
    print("\nCategorical Columns:")
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        print(f"{col}: {df[col].nunique()} unique values")
        if df[col].nunique() <= 10:
            print(f"  Values: {df[col].unique()}")

# Usage
quick_data_overview(df)
```###
 Data Quality Assessment
```python
def assess_data_quality(df):
    """Comprehensive data quality assessment"""
    
    # Duplicates
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows: {duplicates} ({duplicates/len(df)*100:.2f}%)")
    
    # Outliers detection (for numerical columns)
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    
    print("\nOutliers (using IQR method):")
    for col in numerical_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        print(f"{col}: {len(outliers)} outliers ({len(outliers)/len(df)*100:.2f}%)")
    
    # Data consistency checks
    print("\nData Consistency:")
    for col in df.columns:
        if df[col].dtype == 'object':
            # Check for inconsistent formatting
            unique_vals = df[col].dropna().unique()
            if len(unique_vals) > 1:
                # Check for potential duplicates with different cases
                lower_vals = [str(val).lower().strip() for val in unique_vals]
                if len(set(lower_vals)) < len(unique_vals):
                    print(f"{col}: Potential formatting inconsistencies")

# Usage
assess_data_quality(df)
```

### Smart EDA Functions
```python
def smart_eda(df, target_col=None):
    """Intelligent EDA based on data types and target"""
    
    # Separate column types
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    if target_col in numerical_cols:
        numerical_cols.remove(target_col)
    if target_col in categorical_cols:
        categorical_cols.remove(target_col)
    
    # Correlation analysis for numerical features
    if len(numerical_cols) > 1:
        plt.figure(figsize=(12, 8))
        correlation_matrix = df[numerical_cols + [target_col]].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Feature Correlation Matrix')
        plt.show()
        
        # High correlation pairs
        high_corr_pairs = []
        for i in range(len(correlation_matrix.columns)):
            for j in range(i+1, len(correlation_matrix.columns)):
                if abs(correlation_matrix.iloc[i, j]) > 0.8:
                    high_corr_pairs.append((
                        correlation_matrix.columns[i],
                        correlation_matrix.columns[j],
                        correlation_matrix.iloc[i, j]
                    ))
        
        if high_corr_pairs:
            print("High correlation pairs (>0.8):")
            for pair in high_corr_pairs:
                print(f"{pair[0]} - {pair[1]}: {pair[2]:.3f}")
    
    # Distribution plots
    if numerical_cols:
        n_cols = min(3, len(numerical_cols))
        n_rows = (len(numerical_cols) + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
        axes = axes.flatten() if n_rows > 1 else [axes]
        
        for i, col in enumerate(numerical_cols):
            if i < len(axes):
                df[col].hist(bins=30, ax=axes[i], alpha=0.7)
                axes[i].set_title(f'Distribution of {col}')
                axes[i].axvline(df[col].mean(), color='red', linestyle='--', label='Mean')
                axes[i].axvline(df[col].median(), color='green', linestyle='--', label='Median')
                axes[i].legend()
        
        plt.tight_layout()
        plt.show()
    
    # Categorical analysis
    if categorical_cols and target_col:
        for col in categorical_cols[:5]:  # Limit to first 5 categorical columns
            plt.figure(figsize=(12, 4))
            
            plt.subplot(1, 2, 1)
            df[col].value_counts().plot(kind='bar')
            plt.title(f'Distribution of {col}')
            plt.xticks(rotation=45)
            
            plt.subplot(1, 2, 2)
            if df[target_col].dtype in ['int64', 'float64']:
                # Numerical target
                df.boxplot(column=target_col, by=col, ax=plt.gca())
            else:
                # Categorical target
                pd.crosstab(df[col], df[target_col], normalize='index').plot(kind='bar', stacked=True)
            
            plt.title(f'{col} vs {target_col}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

# Usage
smart_eda(df, target_col='target_column')
```

## Data Preprocessing

### Missing Value Handler
```python
def handle_missing_values(df, strategy='auto'):
    """Smart missing value handling based on data type and distribution"""
    
    df_processed = df.copy()
    missing_info = {}
    
    for col in df.columns:
        missing_count = df[col].isnull().sum()
        if missing_count > 0:
            missing_pct = missing_count / len(df) * 100
            
            if missing_pct > 50:
                print(f"Warning: {col} has {missing_pct:.1f}% missing values. Consider dropping.")
                missing_info[col] = 'high_missing'
                continue
            
            if df[col].dtype in ['int64', 'float64']:
                # Numerical column
                if strategy == 'auto':
                    # Check distribution
                    skewness = df[col].skew()
                    if abs(skewness) > 1:  # Highly skewed
                        fill_value = df[col].median()
                        strategy_used = 'median'
                    else:
                        fill_value = df[col].mean()
                        strategy_used = 'mean'
                elif strategy == 'median':
                    fill_value = df[col].median()
                    strategy_used = 'median'
                elif strategy == 'mean':
                    fill_value = df[col].mean()
                    strategy_used = 'mean'
                elif strategy == 'mode':
                    fill_value = df[col].mode()[0]
                    strategy_used = 'mode'
                
                df_processed[col].fillna(fill_value, inplace=True)
                missing_info[col] = f'filled_with_{strategy_used}_{fill_value:.2f}'
                
            else:
                # Categorical column
                if strategy == 'auto' or strategy == 'mode':
                    fill_value = df[col].mode()[0]
                    strategy_used = 'mode'
                else:
                    fill_value = 'Unknown'
                    strategy_used = 'unknown'
                
                df_processed[col].fillna(fill_value, inplace=True)
                missing_info[col] = f'filled_with_{strategy_used}_{fill_value}'
    
    print("Missing value handling summary:")
    for col, info in missing_info.items():
        print(f"{col}: {info}")
    
    return df_processed, missing_info

# Usage
df_clean, missing_info = handle_missing_values(df, strategy='auto')
```

### Outlier Detection and Treatment
```python
def detect_and_treat_outliers(df, method='iqr', action='cap'):
    """
    Detect and treat outliers
    Methods: 'iqr', 'zscore', 'isolation_forest'
    Actions: 'cap', 'remove', 'transform'
    """
    
    df_processed = df.copy()
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    outlier_info = {}
    
    for col in numerical_cols:
        if method == 'iqr':
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers_mask = (df[col] < lower_bound) | (df[col] > upper_bound)
            
        elif method == 'zscore':
            z_scores = np.abs(stats.zscore(df[col].dropna()))
            outliers_mask = z_scores > 3
            lower_bound = df[col].mean() - 3 * df[col].std()
            upper_bound = df[col].mean() + 3 * df[col].std()
        
        outlier_count = outliers_mask.sum()
        outlier_pct = outlier_count / len(df) * 100
        
        if outlier_count > 0:
            if action == 'cap':
                df_processed.loc[df_processed[col] < lower_bound, col] = lower_bound
                df_processed.loc[df_processed[col] > upper_bound, col] = upper_bound
                outlier_info[col] = f'capped_{outlier_count}_outliers'
                
            elif action == 'remove':
                df_processed = df_processed[~outliers_mask]
                outlier_info[col] = f'removed_{outlier_count}_outliers'
                
            elif action == 'transform':
                # Log transformation for positive skewed data
                if df[col].min() > 0:
                    df_processed[col] = np.log1p(df[col])
                    outlier_info[col] = 'log_transformed'
                else:
                    # Box-Cox transformation
                    df_processed[col], _ = stats.boxcox(df[col] - df[col].min() + 1)
                    outlier_info[col] = 'boxcox_transformed'
    
    print("Outlier treatment summary:")
    for col, info in outlier_info.items():
        print(f"{col}: {info}")
    
    return df_processed, outlier_info

# Usage
df_no_outliers, outlier_info = detect_and_treat_outliers(df, method='iqr', action='cap')
```

## Feature Engineering

### Automated Feature Engineering
```python
def auto_feature_engineering(df, target_col=None):
    """Automated feature engineering based on data types"""
    
    df_features = df.copy()
    new_features = []
    
    # Numerical features
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if target_col in numerical_cols:
        numerical_cols.remove(target_col)
    
    # Create polynomial features for highly correlated pairs
    if len(numerical_cols) > 1:
        corr_matrix = df[numerical_cols].corr()
        high_corr_pairs = []
        
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                if 0.3 < abs(corr_matrix.iloc[i, j]) < 0.9:  # Moderate correlation
                    col1, col2 = corr_matrix.columns[i], corr_matrix.columns[j]
                    
                    # Create interaction features
                    df_features[f'{col1}_x_{col2}'] = df[col1] * df[col2]
                    df_features[f'{col1}_div_{col2}'] = df[col1] / (df[col2] + 1e-8)
                    df_features[f'{col1}_plus_{col2}'] = df[col1] + df[col2]
                    
                    new_features.extend([f'{col1}_x_{col2}', f'{col1}_div_{col2}', f'{col1}_plus_{col2}'])
    
    # Statistical features for numerical columns
    for col in numerical_cols:
        # Binning
        df_features[f'{col}_binned'] = pd.cut(df[col], bins=5, labels=False)
        
        # Log transformation (if positive)
        if df[col].min() > 0:
            df_features[f'{col}_log'] = np.log1p(df[col])
            new_features.append(f'{col}_log')
        
        # Square root
        if df[col].min() >= 0:
            df_features[f'{col}_sqrt'] = np.sqrt(df[col])
            new_features.append(f'{col}_sqrt')
        
        new_features.append(f'{col}_binned')
    
    # Categorical features
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if target_col in categorical_cols:
        categorical_cols.remove(target_col)
    
    for col in categorical_cols:
        # Frequency encoding
        freq_map = df[col].value_counts().to_dict()
        df_features[f'{col}_frequency'] = df[col].map(freq_map)
        new_features.append(f'{col}_frequency')
        
        # Length of string
        df_features[f'{col}_length'] = df[col].astype(str).str.len()
        new_features.append(f'{col}_length')
    
    # Date features (if any datetime columns)
    date_cols = df.select_dtypes(include=['datetime64']).columns
    for col in date_cols:
        df_features[f'{col}_year'] = df[col].dt.year
        df_features[f'{col}_month'] = df[col].dt.month
        df_features[f'{col}_day'] = df[col].dt.day
        df_features[f'{col}_dayofweek'] = df[col].dt.dayofweek
        df_features[f'{col}_quarter'] = df[col].dt.quarter
        
        new_features.extend([f'{col}_year', f'{col}_month', f'{col}_day', 
                           f'{col}_dayofweek', f'{col}_quarter'])
    
    print(f"Created {len(new_features)} new features:")
    for feature in new_features[:10]:  # Show first 10
        print(f"  - {feature}")
    if len(new_features) > 10:
        print(f"  ... and {len(new_features) - 10} more")
    
    return df_features, new_features

# Usage
df_engineered, new_features = auto_feature_engineering(df, target_col='target')
```

### Feature Selection
```python
def smart_feature_selection(X, y, method='auto', k=10):
    """Intelligent feature selection based on problem type"""
    
    from sklearn.feature_selection import (
        SelectKBest, f_classif, f_regression, mutual_info_classif, 
        mutual_info_regression, RFE
    )
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    
    # Determine problem type
    if len(np.unique(y)) < 20 and y.dtype in ['int64', 'object']:
        problem_type = 'classification'
    else:
        problem_type = 'regression'
    
    feature_scores = {}
    
    if method == 'auto' or method == 'statistical':
        # Statistical tests
        if problem_type == 'classification':
            selector = SelectKBest(score_func=f_classif, k='all')
        else:
            selector = SelectKBest(score_func=f_regression, k='all')
        
        selector.fit(X, y)
        feature_scores['statistical'] = dict(zip(X.columns, selector.scores_))
    
    if method == 'auto' or method == 'mutual_info':
        # Mutual information
        if problem_type == 'classification':
            mi_scores = mutual_info_classif(X, y)
        else:
            mi_scores = mutual_info_regression(X, y)
        
        feature_scores['mutual_info'] = dict(zip(X.columns, mi_scores))
    
    if method == 'auto' or method == 'tree_based':
        # Tree-based feature importance
        if problem_type == 'classification':
            model = RandomForestClassifier(n_estimators=100, random_state=42)
        else:
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        
        model.fit(X, y)
        feature_scores['tree_based'] = dict(zip(X.columns, model.feature_importances_))
    
    # Combine scores if multiple methods
    if len(feature_scores) > 1:
        # Normalize scores and average
        normalized_scores = {}
        for method_name, scores in feature_scores.items():
            max_score = max(scores.values())
            normalized_scores[method_name] = {k: v/max_score for k, v in scores.items()}
        
        # Average normalized scores
        combined_scores = {}
        for feature in X.columns:
            combined_scores[feature] = np.mean([
                scores[feature] for scores in normalized_scores.values()
            ])
        
        feature_scores['combined'] = combined_scores
    
    # Select top k features
    if method == 'auto':
        final_scores = feature_scores['combined']
    else:
        final_scores = feature_scores[method]
    
    top_features = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)[:k]
    selected_features = [feature for feature, score in top_features]
    
    print(f"Top {k} features selected:")
    for i, (feature, score) in enumerate(top_features, 1):
        print(f"{i:2d}. {feature}: {score:.4f}")
    
    return selected_features, feature_scores

# Usage
selected_features, scores = smart_feature_selection(X, y, method='auto', k=15)
X_selected = X[selected_features]
```

## Algorithm Selection Guide

### Decision Tree for Algorithm Selection
```python
def recommend_algorithm(X, y, dataset_size='auto'):
    """Recommend best algorithms based on data characteristics"""
    
    # Analyze data characteristics
    n_samples, n_features = X.shape
    
    # Determine problem type
    if len(np.unique(y)) < 20 and (y.dtype in ['int64', 'object'] or len(np.unique(y)) / len(y) < 0.1):
        problem_type = 'classification'
        n_classes = len(np.unique(y))
    else:
        problem_type = 'regression'
        n_classes = None
    
    # Dataset size category
    if dataset_size == 'auto':
        if n_samples < 1000:
            dataset_size = 'small'
        elif n_samples < 100000:
            dataset_size = 'medium'
        else:
            dataset_size = 'large'
    
    # Feature to sample ratio
    feature_ratio = n_features / n_samples
    
    recommendations = []
    
    print(f"Dataset Analysis:")
    print(f"  - Problem type: {problem_type}")
    print(f"  - Samples: {n_samples:,}")
    print(f"  - Features: {n_features}")
    print(f"  - Dataset size: {dataset_size}")
    print(f"  - Feature/Sample ratio: {feature_ratio:.3f}")
    if n_classes:
        print(f"  - Number of classes: {n_classes}")
    
    print(f"\nRecommended Algorithms:")
    
    if problem_type == 'classification':
        if dataset_size == 'small':
            if feature_ratio > 0.1:  # High dimensional
                recommendations.extend([
                    ("Logistic Regression", "Good for high-dimensional small datasets"),
                    ("SVM with RBF kernel", "Effective in high dimensions"),
                    ("Naive Bayes", "Works well with limited data")
                ])
            else:
                recommendations.extend([
                    ("Random Forest", "Robust and interpretable"),
                    ("SVM", "Good performance on small datasets"),
                    ("k-NN", "Simple and effective for small data")
                ])
        
        elif dataset_size == 'medium':
            recommendations.extend([
                ("Random Forest", "Excellent balance of performance and interpretability"),
                ("Gradient Boosting (XGBoost/LightGBM)", "Often best performance"),
                ("SVM", "Good for medium-sized datasets"),
                ("Neural Networks", "If you have time for hyperparameter tuning")
            ])
        
        else:  # large
            recommendations.extend([
                ("Gradient Boosting (XGBoost/LightGBM)", "Excellent for large datasets"),
                ("Deep Neural Networks", "Can capture complex patterns"),
                ("Linear models with regularization", "Fast and scalable"),
                ("Random Forest", "Parallel processing friendly")
            ])
        
        # Special cases
        if n_classes > 10:
            recommendations.append(("One-vs-Rest with Linear models", "Efficient for many classes"))
        
        if feature_ratio > 1:  # More features than samples
            recommendations.append(("Regularized Linear Models (Lasso/Ridge)", "Prevents overfitting"))
    
    else:  # regression
        if dataset_size == 'small':
            recommendations.extend([
                ("Linear Regression with regularization", "Simple and interpretable"),
                ("Random Forest", "Robust to outliers"),
                ("SVM Regression", "Good for small datasets")
            ])
        
        elif dataset_size == 'medium':
            recommendations.extend([
                ("Random Forest", "Great default choice"),
                ("Gradient Boosting", "Often best performance"),
                ("Neural Networks", "For complex non-linear relationships")
            ])
        
        else:  # large
            recommendations.extend([
                ("Gradient Boosting (XGBoost/LightGBM)", "Excellent performance"),
                ("Deep Neural Networks", "For complex patterns"),
                ("Linear models", "Fast and scalable baseline")
            ])
    
    # Print recommendations
    for i, (algo, reason) in enumerate(recommendations, 1):
        print(f"{i}. {algo}: {reason}")
    
    return recommendations

# Usage
recommendations = recommend_algorithm(X, y)
```

### Model Implementation Templates
```python
def get_model_templates(problem_type='classification'):
    """Get ready-to-use model templates with good default parameters"""
    
    if problem_type == 'classification':
        models = {
            'logistic_regression': {
                'model': LogisticRegression(random_state=42, max_iter=1000),
                'hyperparams': {
                    'C': [0.1, 1, 10, 100],
                    'penalty': ['l1', 'l2'],
                    'solver': ['liblinear', 'saga']
                }
            },
            
            'random_forest': {
                'model': RandomForestClassifier(random_state=42, n_jobs=-1),
                'hyperparams': {
                    'n_estimators': [100, 200, 300],
                    'max_depth': [10, 20, None],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4]
                }
            },
            
            'xgboost': {
                'model': None,  # Will be imported if available
                'hyperparams': {
                    'n_estimators': [100, 200, 300],
                    'learning_rate': [0.01, 0.1, 0.2],
                    'max_depth': [3, 6, 10],
                    'subsample': [0.8, 0.9, 1.0]
                }
            },
            
            'svm': {
                'model': SVC(random_state=42),
                'hyperparams': {
                    'C': [0.1, 1, 10, 100],
                    'kernel': ['rbf', 'linear', 'poly'],
                    'gamma': ['scale', 'auto', 0.001, 0.01]
                }
            }
        }
    
    else:  # regression
        from sklearn.linear_model import Ridge, Lasso
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.svm import SVR
        
        models = {
            'linear_regression': {
                'model': LinearRegression(),
                'hyperparams': {}
            },
            
            'ridge': {
                'model': Ridge(random_state=42),
                'hyperparams': {
                    'alpha': [0.1, 1, 10, 100, 1000]
                }
            },
            
            'lasso': {
                'model': Lasso(random_state=42),
                'hyperparams': {
                    'alpha': [0.1, 1, 10, 100, 1000]
                }
            },
            
            'random_forest': {
                'model': RandomForestRegressor(random_state=42, n_jobs=-1),
                'hyperparams': {
                    'n_estimators': [100, 200, 300],
                    'max_depth': [10, 20, None],
                    'min_samples_split': [2, 5, 10]
                }
            },
            
            'svr': {
                'model': SVR(),
                'hyperparams': {
                    'C': [0.1, 1, 10, 100],
                    'kernel': ['rbf', 'linear'],
                    'gamma': ['scale', 'auto']
                }
            }
        }
    
    return models

# Usage
models = get_model_templates('classification')
```## Mod
el Training & Evaluation

### Automated Model Training Pipeline
```python
def train_multiple_models(X, y, models_dict, cv_folds=5, test_size=0.2):
    """Train and evaluate multiple models with cross-validation"""
    
    from sklearn.model_selection import cross_val_score, GridSearchCV
    from sklearn.metrics import classification_report, confusion_matrix
    from sklearn.preprocessing import StandardScaler
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y if len(np.unique(y)) < 20 else None
    )
    
    # Scale features for algorithms that need it
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    results = {}
    
    for model_name, model_info in models_dict.items():
        print(f"\nTraining {model_name}...")
        
        model = model_info['model']
        hyperparams = model_info.get('hyperparams', {})
        
        # Determine if scaling is needed
        needs_scaling = model_name in ['svm', 'logistic_regression', 'neural_network']
        X_train_use = X_train_scaled if needs_scaling else X_train
        X_test_use = X_test_scaled if needs_scaling else X_test
        
        try:
            if hyperparams:
                # Hyperparameter tuning
                grid_search = GridSearchCV(
                    model, hyperparams, cv=cv_folds, 
                    scoring='accuracy' if len(np.unique(y)) < 20 else 'r2',
                    n_jobs=-1, verbose=0
                )
                grid_search.fit(X_train_use, y_train)
                best_model = grid_search.best_estimator_
                best_params = grid_search.best_params_
            else:
                # No hyperparameter tuning
                model.fit(X_train_use, y_train)
                best_model = model
                best_params = {}
            
            # Cross-validation scores
            cv_scores = cross_val_score(
                best_model, X_train_use, y_train, cv=cv_folds,
                scoring='accuracy' if len(np.unique(y)) < 20 else 'r2'
            )
            
            # Test predictions
            y_pred = best_model.predict(X_test_use)
            
            # Calculate metrics
            if len(np.unique(y)) < 20:  # Classification
                test_score = accuracy_score(y_test, y_pred)
                report = classification_report(y_test, y_pred, output_dict=True)
            else:  # Regression
                from sklearn.metrics import r2_score, mean_squared_error
                test_score = r2_score(y_test, y_pred)
                mse = mean_squared_error(y_test, y_pred)
                report = {'mse': mse, 'rmse': np.sqrt(mse)}
            
            results[model_name] = {
                'model': best_model,
                'best_params': best_params,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'test_score': test_score,
                'report': report,
                'predictions': y_pred
            }
            
            print(f"  CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
            print(f"  Test Score: {test_score:.4f}")
            
        except Exception as e:
            print(f"  Error training {model_name}: {str(e)}")
            results[model_name] = {'error': str(e)}
    
    return results, X_test, y_test, scaler

# Usage
models = get_model_templates('classification')
results, X_test, y_test, scaler = train_multiple_models(X, y, models)
```

### Model Comparison and Selection
```python
def compare_models(results):
    """Compare model performance and select the best one"""
    
    comparison_df = []
    
    for model_name, result in results.items():
        if 'error' not in result:
            comparison_df.append({
                'Model': model_name,
                'CV_Mean': result['cv_mean'],
                'CV_Std': result['cv_std'],
                'Test_Score': result['test_score'],
                'Best_Params': str(result['best_params'])
            })
    
    comparison_df = pd.DataFrame(comparison_df)
    comparison_df = comparison_df.sort_values('Test_Score', ascending=False)
    
    print("Model Comparison:")
    print("=" * 80)
    print(comparison_df.to_string(index=False))
    
    # Best model
    best_model_name = comparison_df.iloc[0]['Model']
    best_model = results[best_model_name]['model']
    
    print(f"\nBest Model: {best_model_name}")
    print(f"Test Score: {comparison_df.iloc[0]['Test_Score']:.4f}")
    
    return best_model, best_model_name, comparison_df

# Usage
best_model, best_model_name, comparison = compare_models(results)
```

### Advanced Model Evaluation
```python
def detailed_model_evaluation(model, X_test, y_test, model_name, problem_type='classification'):
    """Comprehensive model evaluation with visualizations"""
    
    y_pred = model.predict(X_test)
    
    if problem_type == 'classification':
        from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
        
        print(f"Detailed Evaluation for {model_name}")
        print("=" * 50)
        
        # Classification report
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f'Confusion Matrix - {model_name}')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.show()
        
        # ROC Curve (for binary classification)
        if len(np.unique(y_test)) == 2:
            y_pred_proba = model.predict_proba(X_test)[:, 1]
            fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
            auc_score = roc_auc_score(y_test, y_pred_proba)
            
            plt.figure(figsize=(8, 6))
            plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {auc_score:.3f})')
            plt.plot([0, 1], [0, 1], 'k--', label='Random')
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title(f'ROC Curve - {model_name}')
            plt.legend()
            plt.show()
    
    else:  # Regression
        from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
        
        print(f"Detailed Evaluation for {model_name}")
        print("=" * 50)
        
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        
        print(f"R² Score: {r2:.4f}")
        print(f"MSE: {mse:.4f}")
        print(f"RMSE: {rmse:.4f}")
        print(f"MAE: {mae:.4f}")
        
        # Residual plots
        residuals = y_test - y_pred
        
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Predicted vs Actual
        axes[0].scatter(y_test, y_pred, alpha=0.6)
        axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        axes[0].set_xlabel('Actual Values')
        axes[0].set_ylabel('Predicted Values')
        axes[0].set_title(f'Predicted vs Actual - {model_name}')
        
        # Residual plot
        axes[1].scatter(y_pred, residuals, alpha=0.6)
        axes[1].axhline(y=0, color='r', linestyle='--')
        axes[1].set_xlabel('Predicted Values')
        axes[1].set_ylabel('Residuals')
        axes[1].set_title(f'Residual Plot - {model_name}')
        
        plt.tight_layout()
        plt.show()

# Usage
detailed_model_evaluation(best_model, X_test, y_test, best_model_name, 'classification')
```

## Advanced Techniques

### Ensemble Methods
```python
def create_ensemble_model(models_dict, X_train, y_train, method='voting'):
    """Create ensemble models from trained models"""
    
    from sklearn.ensemble import VotingClassifier, VotingRegressor
    
    # Extract trained models
    estimators = []
    for name, result in models_dict.items():
        if 'error' not in result and 'model' in result:
            estimators.append((name, result['model']))
    
    if len(estimators) < 2:
        print("Need at least 2 models for ensemble")
        return None
    
    # Determine problem type
    problem_type = 'classification' if len(np.unique(y_train)) < 20 else 'regression'
    
    if problem_type == 'classification':
        if method == 'voting':
            ensemble = VotingClassifier(estimators=estimators, voting='soft')
        else:
            # Stacking
            from sklearn.ensemble import StackingClassifier
            from sklearn.linear_model import LogisticRegression
            ensemble = StackingClassifier(
                estimators=estimators,
                final_estimator=LogisticRegression(),
                cv=5
            )
    else:
        if method == 'voting':
            ensemble = VotingRegressor(estimators=estimators)
        else:
            # Stacking
            from sklearn.ensemble import StackingRegressor
            from sklearn.linear_model import Ridge
            ensemble = StackingRegressor(
                estimators=estimators,
                final_estimator=Ridge(),
                cv=5
            )
    
    print(f"Creating {method} ensemble with {len(estimators)} models:")
    for name, _ in estimators:
        print(f"  - {name}")
    
    ensemble.fit(X_train, y_train)
    return ensemble

# Usage
ensemble_model = create_ensemble_model(results, X_train, y_train, method='voting')
```

### Hyperparameter Optimization
```python
def advanced_hyperparameter_tuning(model, param_grid, X, y, method='random_search'):
    """Advanced hyperparameter tuning with multiple methods"""
    
    from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
    
    if method == 'random_search':
        search = RandomizedSearchCV(
            model, param_grid, n_iter=100, cv=5,
            scoring='accuracy' if len(np.unique(y)) < 20 else 'r2',
            n_jobs=-1, random_state=42, verbose=1
        )
    elif method == 'grid_search':
        search = GridSearchCV(
            model, param_grid, cv=5,
            scoring='accuracy' if len(np.unique(y)) < 20 else 'r2',
            n_jobs=-1, verbose=1
        )
    elif method == 'bayesian':
        try:
            from skopt import BayesSearchCV
            search = BayesSearchCV(
                model, param_grid, n_iter=50, cv=5,
                scoring='accuracy' if len(np.unique(y)) < 20 else 'r2',
                n_jobs=-1, random_state=42
            )
        except ImportError:
            print("scikit-optimize not installed. Using RandomizedSearchCV instead.")
            search = RandomizedSearchCV(
                model, param_grid, n_iter=100, cv=5,
                scoring='accuracy' if len(np.unique(y)) < 20 else 'r2',
                n_jobs=-1, random_state=42
            )
    
    print(f"Starting {method} hyperparameter tuning...")
    search.fit(X, y)
    
    print(f"Best parameters: {search.best_params_}")
    print(f"Best cross-validation score: {search.best_score_:.4f}")
    
    return search.best_estimator_, search.best_params_

# Usage
# best_model, best_params = advanced_hyperparameter_tuning(
#     RandomForestClassifier(random_state=42),
#     {'n_estimators': [100, 200, 300], 'max_depth': [10, 20, None]},
#     X, y, method='random_search'
# )
```

### Feature Importance Analysis
```python
def analyze_feature_importance(model, feature_names, top_n=20):
    """Analyze and visualize feature importance"""
    
    # Get feature importance
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        importance_type = 'Tree-based Importance'
    elif hasattr(model, 'coef_'):
        importances = np.abs(model.coef_).flatten()
        importance_type = 'Coefficient Magnitude'
    else:
        print("Model doesn't have feature importance or coefficients")
        return None
    
    # Create importance dataframe
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': importances
    }).sort_values('importance', ascending=False)
    
    # Plot top features
    plt.figure(figsize=(10, 8))
    top_features = importance_df.head(top_n)
    
    plt.barh(range(len(top_features)), top_features['importance'])
    plt.yticks(range(len(top_features)), top_features['feature'])
    plt.xlabel(importance_type)
    plt.title(f'Top {top_n} Feature Importances')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
    
    print(f"Top {top_n} Most Important Features:")
    for i, (_, row) in enumerate(top_features.iterrows(), 1):
        print(f"{i:2d}. {row['feature']}: {row['importance']:.4f}")
    
    return importance_df

# Usage
importance_df = analyze_feature_importance(best_model, X.columns, top_n=15)
```

## Production & Deployment

### Model Serialization
```python
def save_model_pipeline(model, scaler, feature_names, model_name, save_path='models/'):
    """Save complete model pipeline for production"""
    
    import joblib
    import json
    import os
    
    # Create directory if it doesn't exist
    os.makedirs(save_path, exist_ok=True)
    
    # Save model
    model_path = os.path.join(save_path, f'{model_name}_model.joblib')
    joblib.dump(model, model_path)
    
    # Save scaler
    scaler_path = os.path.join(save_path, f'{model_name}_scaler.joblib')
    joblib.dump(scaler, scaler_path)
    
    # Save metadata
    metadata = {
        'model_name': model_name,
        'feature_names': list(feature_names),
        'model_type': type(model).__name__,
        'n_features': len(feature_names),
        'created_at': pd.Timestamp.now().isoformat()
    }
    
    metadata_path = os.path.join(save_path, f'{model_name}_metadata.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Model pipeline saved:")
    print(f"  Model: {model_path}")
    print(f"  Scaler: {scaler_path}")
    print(f"  Metadata: {metadata_path}")
    
    return {
        'model_path': model_path,
        'scaler_path': scaler_path,
        'metadata_path': metadata_path
    }

def load_model_pipeline(model_name, load_path='models/'):
    """Load complete model pipeline"""
    
    import joblib
    import json
    import os
    
    # Load model
    model_path = os.path.join(load_path, f'{model_name}_model.joblib')
    model = joblib.load(model_path)
    
    # Load scaler
    scaler_path = os.path.join(load_path, f'{model_name}_scaler.joblib')
    scaler = joblib.load(scaler_path)
    
    # Load metadata
    metadata_path = os.path.join(load_path, f'{model_name}_metadata.json')
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    
    return model, scaler, metadata

# Usage
paths = save_model_pipeline(best_model, scaler, X.columns, 'my_best_model')
# loaded_model, loaded_scaler, metadata = load_model_pipeline('my_best_model')
```

### Prediction Pipeline
```python
def create_prediction_pipeline(model, scaler, feature_names, needs_scaling=True):
    """Create a production-ready prediction pipeline"""
    
    def predict(input_data):
        """
        Make predictions on new data
        input_data: dict, pandas DataFrame, or numpy array
        """
        
        # Convert input to DataFrame if needed
        if isinstance(input_data, dict):
            input_df = pd.DataFrame([input_data])
        elif isinstance(input_data, np.ndarray):
            input_df = pd.DataFrame(input_data, columns=feature_names)
        else:
            input_df = input_data.copy()
        
        # Ensure all required features are present
        missing_features = set(feature_names) - set(input_df.columns)
        if missing_features:
            raise ValueError(f"Missing features: {missing_features}")
        
        # Select and order features
        input_df = input_df[feature_names]
        
        # Handle missing values (simple strategy)
        input_df = input_df.fillna(input_df.mean())
        
        # Scale if needed
        if needs_scaling and scaler is not None:
            input_scaled = scaler.transform(input_df)
        else:
            input_scaled = input_df.values
        
        # Make prediction
        predictions = model.predict(input_scaled)
        
        # Get prediction probabilities if available
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(input_scaled)
            return {
                'predictions': predictions,
                'probabilities': probabilities
            }
        else:
            return {'predictions': predictions}
    
    return predict

# Usage
predict_fn = create_prediction_pipeline(best_model, scaler, X.columns, needs_scaling=True)

# Example prediction
# new_data = {'feature1': 1.0, 'feature2': 2.0, ...}
# result = predict_fn(new_data)
```

## Data Scientist Tricks

### Data Type Decision Matrix
```python
def analyze_data_handling_strategy(df):
    """Comprehensive analysis to determine optimal data handling strategies"""
    
    strategies = {}
    
    for col in df.columns:
        col_info = {
            'dtype': str(df[col].dtype),
            'unique_count': df[col].nunique(),
            'null_count': df[col].isnull().sum(),
            'null_percentage': df[col].isnull().sum() / len(df) * 100
        }
        
        # Determine column type and strategy
        if df[col].dtype in ['int64', 'float64']:
            # Numerical column
            col_info['type'] = 'numerical'
            
            # Check distribution
            skewness = df[col].skew()
            col_info['skewness'] = skewness
            
            # Outlier detection
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
            col_info['outlier_percentage'] = len(outliers) / len(df) * 100
            
            # Recommendations
            recommendations = []
            
            if col_info['null_percentage'] > 0:
                if abs(skewness) > 1:
                    recommendations.append("Use median for missing values (skewed distribution)")
                else:
                    recommendations.append("Use mean for missing values (normal distribution)")
            
            if col_info['outlier_percentage'] > 5:
                recommendations.append("Consider outlier treatment (capping or transformation)")
            
            if abs(skewness) > 2:
                recommendations.append("Apply log transformation to reduce skewness")
            
            col_info['recommendations'] = recommendations
            
        elif df[col].dtype == 'object':
            # Categorical/Text column
            col_info['type'] = 'categorical'
            
            # Check if it's actually numerical
            try:
                pd.to_numeric(df[col], errors='raise')
                col_info['type'] = 'numerical_as_string'
                col_info['recommendations'] = ["Convert to numerical type"]
            except:
                # True categorical
                unique_ratio = col_info['unique_count'] / len(df)
                col_info['unique_ratio'] = unique_ratio
                
                recommendations = []
                
                if col_info['null_percentage'] > 0:
                    recommendations.append("Use mode or 'Unknown' for missing values")
                
                if unique_ratio > 0.5:
                    recommendations.append("High cardinality - consider target encoding or feature hashing")
                elif unique_ratio < 0.05:
                    recommendations.append("Low cardinality - use one-hot encoding")
                else:
                    recommendations.append("Medium cardinality - use label encoding or target encoding")
                
                # Check for potential date strings
                sample_values = df[col].dropna().head(10).astype(str)
                if any(len(val) > 8 and ('-' in val or '/' in val) for val in sample_values):
                    recommendations.append("Might be date - consider datetime conversion")
                
                col_info['recommendations'] = recommendations
        
        elif df[col].dtype == 'datetime64[ns]':
            col_info['type'] = 'datetime'
            col_info['recommendations'] = [
                "Extract date features (year, month, day, weekday)",
                "Consider cyclical encoding for seasonal patterns"
            ]
        
        else:
            col_info['type'] = 'other'
            col_info['recommendations'] = ["Review data type and consider appropriate conversion"]
        
        strategies[col] = col_info
    
    return strategies

def print_data_strategy_report(strategies):
    """Print a comprehensive data handling strategy report"""
    
    print("DATA HANDLING STRATEGY REPORT")
    print("=" * 80)
    
    for col, info in strategies.items():
        print(f"\nColumn: {col}")
        print(f"  Type: {info['type']}")
        print(f"  Data Type: {info['dtype']}")
        print(f"  Unique Values: {info['unique_count']:,}")
        print(f"  Missing Values: {info['null_count']:,} ({info['null_percentage']:.1f}%)")
        
        if 'skewness' in info:
            print(f"  Skewness: {info['skewness']:.2f}")
        if 'outlier_percentage' in info:
            print(f"  Outliers: {info['outlier_percentage']:.1f}%")
        if 'unique_ratio' in info:
            print(f"  Unique Ratio: {info['unique_ratio']:.3f}")
        
        print("  Recommendations:")
        for rec in info['recommendations']:
            print(f"    - {rec}")

# Usage
strategies = analyze_data_handling_strategy(df)
print_data_strategy_report(strategies)
```

### Quick Model Prototyping
```python
def quick_ml_prototype(df, target_col, problem_type='auto', test_size=0.2):
    """Rapid ML prototyping with automated preprocessing and model selection"""
    
    print("QUICK ML PROTOTYPE")
    print("=" * 50)
    
    # Separate features and target
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Determine problem type
    if problem_type == 'auto':
        if y.dtype == 'object' or len(y.unique()) < 20:
            problem_type = 'classification'
        else:
            problem_type = 'regression'
    
    print(f"Problem Type: {problem_type}")
    print(f"Features: {X.shape[1]}")
    print(f"Samples: {X.shape[0]}")
    
    # Quick preprocessing
    print("\nPreprocessing...")
    
    # Handle missing values
    X_processed = X.copy()
    for col in X.columns:
        if X[col].isnull().sum() > 0:
            if X[col].dtype in ['int64', 'float64']:
                X_processed[col].fillna(X[col].median(), inplace=True)
            else:
                X_processed[col].fillna(X[col].mode()[0], inplace=True)
    
    # Encode categorical variables
    categorical_cols = X_processed.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if X_processed[col].nunique() > 10:
            # High cardinality - use target encoding
            target_mean = y.groupby(X_processed[col]).mean()
            X_processed[col] = X_processed[col].map(target_mean)
        else:
            # Low cardinality - use label encoding
            le = LabelEncoder()
            X_processed[col] = le.fit_transform(X_processed[col].astype(str))
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_processed, y, test_size=test_size, random_state=42
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Quick model testing
    print("\nTesting models...")
    
    if problem_type == 'classification':
        models = {
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
            'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
            'SVM': SVC(random_state=42)
        }
        scoring = 'accuracy'
    else:
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.svm import SVR
        models = {
            'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
            'Linear Regression': LinearRegression(),
            'SVR': SVR()
        }
        scoring = 'r2'
    
    results = {}
    for name, model in models.items():
        # Use scaled data for SVM and Logistic Regression
        if name in ['SVM', 'SVR', 'Logistic Regression']:
            X_train_use, X_test_use = X_train_scaled, X_test_scaled
        else:
            X_train_use, X_test_use = X_train, X_test
        
        # Train and evaluate
        model.fit(X_train_use, y_train)
        train_score = model.score(X_train_use, y_train)
        test_score = model.score(X_test_use, y_test)
        
        results[name] = {
            'train_score': train_score,
            'test_score': test_score,
            'overfitting': train_score - test_score
        }
        
        print(f"{name:20} | Train: {train_score:.4f} | Test: {test_score:.4f} | Overfitting: {train_score - test_score:.4f}")
    
    # Best model
    best_model = max(results.items(), key=lambda x: x[1]['test_score'])
    print(f"\nBest Model: {best_model[0]} (Test Score: {best_model[1]['test_score']:.4f})")
    
    return results, X_processed, y

# Usage
# results, X_processed, y = quick_ml_prototype(df, 'target_column')
```

### Data Quality Scoring
```python
def calculate_data_quality_score(df):
    """Calculate overall data quality score and provide improvement suggestions"""
    
    scores = {}
    total_score = 0
    max_score = 0
    
    # Completeness Score (40% weight)
    completeness = (1 - df.isnull().sum().sum() / (len(df) * len(df.columns))) * 100
    scores['completeness'] = completeness
    total_score += completeness * 0.4
    max_score += 40
    
    # Consistency Score (20% weight)
    consistency_issues = 0
    total_checks = 0
    
    for col in df.select_dtypes(include=['object']).columns:
        total_checks += 1
        unique_vals = df[col].dropna().astype(str)
        # Check for case inconsistencies
        lower_unique = unique_vals.str.lower().nunique()
        if lower_unique < unique_vals.nunique():
            consistency_issues += 1
    
    consistency = (1 - consistency_issues / max(total_checks, 1)) * 100
    scores['consistency'] = consistency
    total_score += consistency * 0.2
    max_score += 20
    
    # Validity Score (20% weight)
    validity_issues = 0
    total_numeric_cols = len(df.select_dtypes(include=[np.number]).columns)
    
    for col in df.select_dtypes(include=[np.number]).columns:
        # Check for extreme outliers (beyond 3 standard deviations)
        z_scores = np.abs(stats.zscore(df[col].dropna()))
        if (z_scores > 3).sum() > len(df) * 0.05:  # More than 5% outliers
            validity_issues += 1
    
    validity = (1 - validity_issues / max(total_numeric_cols, 1)) * 100
    scores['validity'] = validity
    total_score += validity * 0.2
    max_score += 20
    
    # Uniqueness Score (20% weight)
    duplicate_ratio = df.duplicated().sum() / len(df)
    uniqueness = (1 - duplicate_ratio) * 100
    scores['uniqueness'] = uniqueness
    total_score += uniqueness * 0.2
    max_score += 20
    
    overall_score = (total_score / max_score) * 100
    
    print("DATA QUALITY ASSESSMENT")
    print("=" * 40)
    print(f"Overall Score: {overall_score:.1f}/100")
    print(f"  Completeness: {completeness:.1f}% (Weight: 40%)")
    print(f"  Consistency:  {consistency:.1f}% (Weight: 20%)")
    print(f"  Validity:     {validity:.1f}% (Weight: 20%)")
    print(f"  Uniqueness:   {uniqueness:.1f}% (Weight: 20%)")
    
    # Recommendations
    print("\nRECOMMENDations:")
    if completeness < 90:
        print("- Address missing values using appropriate imputation strategies")
    if consistency < 90:
        print("- Standardize categorical values (case, formatting)")
    if validity < 90:
        print("- Investigate and treat outliers in numerical columns")
    if uniqueness < 95:
        print("- Remove or investigate duplicate records")
    
    if overall_score >= 90:
        print("- Excellent data quality! Ready for modeling.")
    elif overall_score >= 70:
        print("- Good data quality with minor improvements needed.")
    else:
        print("- Significant data quality issues need attention before modeling.")
    
    return scores, overall_score

# Usage
scores, overall_score = calculate_data_quality_score(df)
```

This comprehensive ML cheatsheet provides data scientists with practical tools and decision-making frameworks for handling different types of data and choosing appropriate modeling strategies. Each section includes real-world tricks and automated functions that can significantly speed up the data science workflow.