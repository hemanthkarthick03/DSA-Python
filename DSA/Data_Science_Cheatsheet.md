# Data Science Cheatsheet - Complete Guide with Statistics & Probability

## Table of Contents
- [Data Science Fundamentals](#data-science-fundamentals)
- [Statistics Essentials](#statistics-essentials)
- [Probability Theory](#probability-theory)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Machine Learning Algorithms](#machine-learning-algorithms)
- [Model Evaluation](#model-evaluation)
- [Advanced Techniques](#advanced-techniques)
- [Data Visualization](#data-visualization)
- [Statistical Tests](#statistical-tests)
- [Time Series Analysis](#time-series-analysis)
- [Tricks & Best Practices](#tricks--best-practices)

## Data Science Fundamentals

### Essential Libraries Setup
```python
# Core libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Statistical libraries
import scipy.stats as stats
from scipy import optimize
import statsmodels.api as sm
from statsmodels.stats import diagnostic
from statsmodels.tsa.seasonal import seasonal_decompose

# Machine Learning
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso

# Advanced ML
import xgboost as xgb
import lightgbm as lgb
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
```

### Data Science Process Framework
```python
class DataScienceWorkflow:
    """Complete data science workflow framework"""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.raw_data = None
        self.processed_data = None
        self.model = None
        self.results = {}
    
    def load_data(self):
        """Load and initial data inspection"""
        self.raw_data = pd.read_csv(self.data_path)
        print(f"Data shape: {self.raw_data.shape}")
        print(f"Memory usage: {self.raw_data.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        return self.raw_data.head()
    
    def explore_data(self):
        """Comprehensive EDA"""
        print("=== DATA OVERVIEW ===")
        print(self.raw_data.info())
        print("\n=== MISSING VALUES ===")
        missing = self.raw_data.isnull().sum()
        print(missing[missing > 0])
        print("\n=== STATISTICAL SUMMARY ===")
        print(self.raw_data.describe())
        
        # Correlation analysis
        numeric_cols = self.raw_data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 1:
            plt.figure(figsize=(12, 8))
            sns.heatmap(self.raw_data[numeric_cols].corr(), annot=True, cmap='coolwarm')
            plt.title('Correlation Matrix')
            plt.show()
    
    def preprocess_data(self):
        """Data preprocessing pipeline"""
        self.processed_data = self.raw_data.copy()
        
        # Handle missing values
        numeric_cols = self.processed_data.select_dtypes(include=[np.number]).columns
        categorical_cols = self.processed_data.select_dtypes(include=['object']).columns
        
        # Fill numeric missing values with median
        for col in numeric_cols:
            if self.processed_data[col].isnull().sum() > 0:
                self.processed_data[col].fillna(self.processed_data[col].median(), inplace=True)
        
        # Fill categorical missing values with mode
        for col in categorical_cols:
            if self.processed_data[col].isnull().sum() > 0:
                self.processed_data[col].fillna(self.processed_data[col].mode()[0], inplace=True)
        
        return self.processed_data
    
    def feature_engineering(self, target_col):
        """Automated feature engineering"""
        # Create interaction features
        numeric_cols = self.processed_data.select_dtypes(include=[np.number]).columns
        numeric_cols = [col for col in numeric_cols if col != target_col]
        
        # Polynomial features for top correlated features
        correlations = self.processed_data[numeric_cols].corrwith(self.processed_data[target_col]).abs()
        top_features = correlations.nlargest(3).index.tolist()
        
        for i, col1 in enumerate(top_features):
            for col2 in top_features[i+1:]:
                self.processed_data[f'{col1}_x_{col2}'] = self.processed_data[col1] * self.processed_data[col2]
        
        return self.processed_data
    
    def train_model(self, target_col, model_type='classification'):
        """Train and evaluate model"""
        X = self.processed_data.drop(columns=[target_col])
        y = self.processed_data[target_col]
        
        # Encode categorical variables
        categorical_cols = X.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Train model
        if model_type == 'classification':
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
            self.model.fit(X_train_scaled, y_train)
            y_pred = self.model.predict(X_test_scaled)
            
            self.results = {
                'accuracy': accuracy_score(y_test, y_pred),
                'precision': precision_score(y_test, y_pred, average='weighted'),
                'recall': recall_score(y_test, y_pred, average='weighted'),
                'f1': f1_score(y_test, y_pred, average='weighted')
            }
        else:
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X_train_scaled, y_train)
            y_pred = self.model.predict(X_test_scaled)
            
            from sklearn.metrics import mean_squared_error, r2_score
            self.results = {
                'mse': mean_squared_error(y_test, y_pred),
                'rmse': np.sqrt(mean_squared_error(y_test, y_pred)),
                'r2': r2_score(y_test, y_pred)
            }
        
        return self.results

# Usage
# workflow = DataScienceWorkflow('data.csv')
# workflow.load_data()
# workflow.explore_data()
# workflow.preprocess_data()
# workflow.feature_engineering('target')
# results = workflow.train_model('target', 'classification')
```

## Statistics Essentials

### Descriptive Statistics
```python
def comprehensive_stats(data, column):
    """Calculate comprehensive descriptive statistics"""
    
    stats_dict = {
        'count': len(data[column]),
        'mean': np.mean(data[column]),
        'median': np.median(data[column]),
        'mode': stats.mode(data[column])[0][0],
        'std': np.std(data[column], ddof=1),  # Sample standard deviation
        'var': np.var(data[column], ddof=1),  # Sample variance
        'min': np.min(data[column]),
        'max': np.max(data[column]),
        'range': np.max(data[column]) - np.min(data[column]),
        'q1': np.percentile(data[column], 25),
        'q3': np.percentile(data[column], 75),
        'iqr': np.percentile(data[column], 75) - np.percentile(data[column], 25),
        'skewness': stats.skew(data[column]),
        'kurtosis': stats.kurtosis(data[column]),
        'cv': np.std(data[column], ddof=1) / np.mean(data[column])  # Coefficient of variation
    }
    
    return pd.Series(stats_dict)

# Advanced statistical measures
def advanced_statistics(data):
    """Calculate advanced statistical measures"""
    
    # Outlier detection using IQR method
    def detect_outliers_iqr(series):
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return series[(series < lower_bound) | (series > upper_bound)]
    
    # Z-score outlier detection
    def detect_outliers_zscore(series, threshold=3):
        z_scores = np.abs(stats.zscore(series))
        return series[z_scores > threshold]
    
    # Normality tests
    def test_normality(series):
        # Shapiro-Wilk test (best for small samples)
        shapiro_stat, shapiro_p = stats.shapiro(series)
        
        # Kolmogorov-Smirnov test
        ks_stat, ks_p = stats.kstest(series, 'norm', args=(series.mean(), series.std()))
        
        # Anderson-Darling test
        ad_stat, ad_critical, ad_significance = stats.anderson(series, dist='norm')
        
        return {
            'shapiro_stat': shapiro_stat,
            'shapiro_p': shapiro_p,
            'ks_stat': ks_stat,
            'ks_p': ks_p,
            'ad_stat': ad_stat,
            'is_normal_shapiro': shapiro_p > 0.05,
            'is_normal_ks': ks_p > 0.05
        }
    
    results = {}
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols:
        results[col] = {
            'basic_stats': comprehensive_stats(data, col),
            'outliers_iqr': detect_outliers_iqr(data[col]),
            'outliers_zscore': detect_outliers_zscore(data[col]),
            'normality_tests': test_normality(data[col])
        }
    
    return results

# Example usage
# stats_results = advanced_statistics(df)
# print(stats_results['column_name']['basic_stats'])
```

### Central Limit Theorem Demonstration
```python
def demonstrate_clt(population_dist='exponential', sample_sizes=[1, 5, 10, 30, 100], n_samples=1000):
    """Demonstrate Central Limit Theorem"""
    
    # Generate population
    np.random.seed(42)
    if population_dist == 'exponential':
        population = np.random.exponential(scale=2, size=10000)
    elif population_dist == 'uniform':
        population = np.random.uniform(0, 10, size=10000)
    elif population_dist == 'bimodal':
        pop1 = np.random.normal(2, 1, 5000)
        pop2 = np.random.normal(8, 1, 5000)
        population = np.concatenate([pop1, pop2])
    
    fig, axes = plt.subplots(2, len(sample_sizes), figsize=(20, 8))
    
    for i, sample_size in enumerate(sample_sizes):
        # Generate sample means
        sample_means = []
        for _ in range(n_samples):
            sample = np.random.choice(population, size=sample_size, replace=True)
            sample_means.append(np.mean(sample))
        
        # Plot population distribution (first row)
        if i == 0:
            axes[0, i].hist(population, bins=50, alpha=0.7, density=True)
            axes[0, i].set_title('Population Distribution')
        else:
            axes[0, i].axis('off')
        
        # Plot sampling distribution (second row)
        axes[1, i].hist(sample_means, bins=50, alpha=0.7, density=True)
        axes[1, i].set_title(f'Sample Size: {sample_size}')
        axes[1, i].axvline(np.mean(sample_means), color='red', linestyle='--', 
                          label=f'Mean: {np.mean(sample_means):.2f}')
        axes[1, i].legend()
        
        # Calculate and display statistics
        print(f"Sample Size {sample_size}:")
        print(f"  Mean of sample means: {np.mean(sample_means):.4f}")
        print(f"  Std of sample means: {np.std(sample_means):.4f}")
        print(f"  Theoretical std: {np.std(population)/np.sqrt(sample_size):.4f}")
        print(f"  Normality test p-value: {stats.shapiro(sample_means)[1]:.4f}")
        print()
    
    plt.tight_layout()
    plt.show()

# demonstrate_clt('exponential')
```

## Probability Theory

### Probability Distributions
```python
class ProbabilityDistributions:
    """Comprehensive probability distributions toolkit"""
    
    @staticmethod
    def plot_distributions():
        """Plot common probability distributions"""
        
        fig, axes = plt.subplots(3, 3, figsize=(15, 12))
        x = np.linspace(-4, 4, 1000)
        
        # Normal Distribution
        axes[0, 0].plot(x, stats.norm.pdf(x, 0, 1), label='μ=0, σ=1')
        axes[0, 0].plot(x, stats.norm.pdf(x, 0, 0.5), label='μ=0, σ=0.5')
        axes[0, 0].plot(x, stats.norm.pdf(x, 1, 1), label='μ=1, σ=1')
        axes[0, 0].set_title('Normal Distribution')
        axes[0, 0].legend()
        
        # Exponential Distribution
        x_exp = np.linspace(0, 5, 1000)
        axes[0, 1].plot(x_exp, stats.expon.pdf(x_exp, scale=1), label='λ=1')
        axes[0, 1].plot(x_exp, stats.expon.pdf(x_exp, scale=0.5), label='λ=2')
        axes[0, 1].plot(x_exp, stats.expon.pdf(x_exp, scale=2), label='λ=0.5')
        axes[0, 1].set_title('Exponential Distribution')
        axes[0, 1].legend()
        
        # Gamma Distribution
        axes[0, 2].plot(x_exp, stats.gamma.pdf(x_exp, a=1, scale=1), label='α=1, β=1')
        axes[0, 2].plot(x_exp, stats.gamma.pdf(x_exp, a=2, scale=1), label='α=2, β=1')
        axes[0, 2].plot(x_exp, stats.gamma.pdf(x_exp, a=1, scale=2), label='α=1, β=2')
        axes[0, 2].set_title('Gamma Distribution')
        axes[0, 2].legend()
        
        # Beta Distribution
        x_beta = np.linspace(0, 1, 1000)
        axes[1, 0].plot(x_beta, stats.beta.pdf(x_beta, 2, 2), label='α=2, β=2')
        axes[1, 0].plot(x_beta, stats.beta.pdf(x_beta, 1, 3), label='α=1, β=3')
        axes[1, 0].plot(x_beta, stats.beta.pdf(x_beta, 3, 1), label='α=3, β=1')
        axes[1, 0].set_title('Beta Distribution')
        axes[1, 0].legend()
        
        # Chi-square Distribution
        x_chi = np.linspace(0, 10, 1000)
        axes[1, 1].plot(x_chi, stats.chi2.pdf(x_chi, df=1), label='df=1')
        axes[1, 1].plot(x_chi, stats.chi2.pdf(x_chi, df=3), label='df=3')
        axes[1, 1].plot(x_chi, stats.chi2.pdf(x_chi, df=5), label='df=5')
        axes[1, 1].set_title('Chi-square Distribution')
        axes[1, 1].legend()
        
        # t-Distribution
        axes[1, 2].plot(x, stats.t.pdf(x, df=1), label='df=1')
        axes[1, 2].plot(x, stats.t.pdf(x, df=5), label='df=5')
        axes[1, 2].plot(x, stats.t.pdf(x, df=30), label='df=30')
        axes[1, 2].plot(x, stats.norm.pdf(x), label='Normal', linestyle='--')
        axes[1, 2].set_title('t-Distribution')
        axes[1, 2].legend()
        
        # F-Distribution
        x_f = np.linspace(0, 5, 1000)
        axes[2, 0].plot(x_f, stats.f.pdf(x_f, dfn=5, dfd=10), label='df1=5, df2=10')
        axes[2, 0].plot(x_f, stats.f.pdf(x_f, dfn=10, dfd=5), label='df1=10, df2=5')
        axes[2, 0].set_title('F-Distribution')
        axes[2, 0].legend()
        
        # Poisson Distribution
        x_pois = np.arange(0, 15)
        axes[2, 1].bar(x_pois, stats.poisson.pmf(x_pois, mu=2), alpha=0.7, label='λ=2')
        axes[2, 1].bar(x_pois, stats.poisson.pmf(x_pois, mu=5), alpha=0.7, label='λ=5')
        axes[2, 1].set_title('Poisson Distribution')
        axes[2, 1].legend()
        
        # Binomial Distribution
        x_binom = np.arange(0, 21)
        axes[2, 2].bar(x_binom, stats.binom.pmf(x_binom, n=20, p=0.3), alpha=0.7, label='n=20, p=0.3')
        axes[2, 2].bar(x_binom, stats.binom.pmf(x_binom, n=20, p=0.7), alpha=0.7, label='n=20, p=0.7')
        axes[2, 2].set_title('Binomial Distribution')
        axes[2, 2].legend()
        
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def bayes_theorem(prior, likelihood_given_event, likelihood_given_no_event):
        """Calculate posterior probability using Bayes' theorem"""
        # P(A|B) = P(B|A) * P(A) / P(B)
        # where P(B) = P(B|A) * P(A) + P(B|¬A) * P(¬A)
        
        marginal_likelihood = (likelihood_given_event * prior + 
                             likelihood_given_no_event * (1 - prior))
        
        posterior = (likelihood_given_event * prior) / marginal_likelihood
        
        return {
            'prior': prior,
            'likelihood_given_event': likelihood_given_event,
            'likelihood_given_no_event': likelihood_given_no_event,
            'marginal_likelihood': marginal_likelihood,
            'posterior': posterior
        }
    
    @staticmethod
    def monte_carlo_simulation(n_simulations=10000):
        """Monte Carlo simulation examples"""
        
        # Example 1: Estimate π
        def estimate_pi(n):
            inside_circle = 0
            for _ in range(n):
                x, y = np.random.uniform(-1, 1, 2)
                if x**2 + y**2 <= 1:
                    inside_circle += 1
            return 4 * inside_circle / n
        
        pi_estimate = estimate_pi(n_simulations)
        
        # Example 2: Portfolio risk simulation
        def portfolio_simulation(returns, weights, n_sims=10000):
            portfolio_returns = []
            for _ in range(n_sims):
                random_returns = np.random.multivariate_normal(
                    returns.mean(), returns.cov(), 252
                )
                portfolio_return = np.sum(random_returns * weights, axis=1)
                portfolio_returns.append(np.sum(portfolio_return))
            
            return np.array(portfolio_returns)
        
        # Example 3: Option pricing (Black-Scholes Monte Carlo)
        def option_price_mc(S0, K, T, r, sigma, n_sims=10000):
            dt = T / 252
            prices = []
            
            for _ in range(n_sims):
                S = S0
                for _ in range(252):
                    S *= np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.normal())
                prices.append(max(S - K, 0))  # Call option payoff
            
            return np.exp(-r * T) * np.mean(prices)
        
        return {
            'pi_estimate': pi_estimate,
            'pi_error': abs(pi_estimate - np.pi),
            'option_price_example': option_price_mc(100, 105, 1, 0.05, 0.2)
        }

# Usage
# prob_dist = ProbabilityDistributions()
# prob_dist.plot_distributions()
# bayes_result = prob_dist.bayes_theorem(0.01, 0.95, 0.05)  # Medical test example
# mc_results = prob_dist.monte_carlo_simulation()
```

### Hypothesis Testing Framework
```python
class HypothesisTestingToolkit:
    """Comprehensive hypothesis testing toolkit"""
    
    @staticmethod
    def power_analysis(effect_size, alpha=0.05, power=0.8):
        """Calculate required sample size for given power"""
        from statsmodels.stats.power import ttest_power
        
        # For t-test
        sample_size = ttest_power(effect_size, power, alpha, alternative='two-sided')
        
        return {
            'effect_size': effect_size,
            'alpha': alpha,
            'power': power,
            'required_sample_size': sample_size
        }
    
    @staticmethod
    def ab_test_analysis(control_group, treatment_group, alpha=0.05):
        """Comprehensive A/B test analysis"""
        
        # Basic statistics
        control_mean = np.mean(control_group)
        treatment_mean = np.mean(treatment_group)
        control_std = np.std(control_group, ddof=1)
        treatment_std = np.std(treatment_group, ddof=1)
        
        # Effect size (Cohen's d)
        pooled_std = np.sqrt(((len(control_group) - 1) * control_std**2 + 
                             (len(treatment_group) - 1) * treatment_std**2) / 
                            (len(control_group) + len(treatment_group) - 2))
        cohens_d = (treatment_mean - control_mean) / pooled_std
        
        # Statistical tests
        # 1. Two-sample t-test
        t_stat, t_pvalue = stats.ttest_ind(control_group, treatment_group)
        
        # 2. Welch's t-test (unequal variances)
        welch_stat, welch_pvalue = stats.ttest_ind(control_group, treatment_group, equal_var=False)
        
        # 3. Mann-Whitney U test (non-parametric)
        mw_stat, mw_pvalue = stats.mannwhitneyu(control_group, treatment_group, alternative='two-sided')
        
        # 4. Levene's test for equal variances
        levene_stat, levene_pvalue = stats.levene(control_group, treatment_group)
        
        # Confidence interval for difference in means
        se_diff = np.sqrt(control_std**2/len(control_group) + treatment_std**2/len(treatment_group))
        df = len(control_group) + len(treatment_group) - 2
        t_critical = stats.t.ppf(1 - alpha/2, df)
        diff_mean = treatment_mean - control_mean
        ci_lower = diff_mean - t_critical * se_diff
        ci_upper = diff_mean + t_critical * se_diff
        
        # Practical significance
        relative_change = (treatment_mean - control_mean) / control_mean * 100
        
        results = {
            'control_stats': {'mean': control_mean, 'std': control_std, 'n': len(control_group)},
            'treatment_stats': {'mean': treatment_mean, 'std': treatment_std, 'n': len(treatment_group)},
            'effect_size': cohens_d,
            'relative_change_percent': relative_change,
            'statistical_tests': {
                't_test': {'statistic': t_stat, 'p_value': t_pvalue, 'significant': t_pvalue < alpha},
                'welch_test': {'statistic': welch_stat, 'p_value': welch_pvalue, 'significant': welch_pvalue < alpha},
                'mann_whitney': {'statistic': mw_stat, 'p_value': mw_pvalue, 'significant': mw_pvalue < alpha},
                'levene_test': {'statistic': levene_stat, 'p_value': levene_pvalue, 'equal_variances': levene_pvalue > alpha}
            },
            'confidence_interval': {'lower': ci_lower, 'upper': ci_upper, 'level': 1-alpha},
            'recommendation': 'Use Welch test' if levene_pvalue < alpha else 'Use standard t-test'
        }
        
        return results
    
    @staticmethod
    def multiple_testing_correction(p_values, method='bonferroni'):
        """Apply multiple testing corrections"""
        from statsmodels.stats.multitest import multipletests
        
        rejected, p_corrected, alpha_sidak, alpha_bonf = multipletests(
            p_values, alpha=0.05, method=method
        )
        
        return {
            'original_p_values': p_values,
            'corrected_p_values': p_corrected,
            'rejected_hypotheses': rejected,
            'method': method,
            'bonferroni_alpha': alpha_bonf,
            'sidak_alpha': alpha_sidak
        }

# Example usage
# control = np.random.normal(100, 15, 1000)
# treatment = np.random.normal(105, 15, 1000)
# ab_results = HypothesisTestingToolkit.ab_test_analysis(control, treatment)
```

## Exploratory Data Analysis

### Advanced EDA Toolkit
```python
class AdvancedEDA:
    """Advanced Exploratory Data Analysis toolkit"""
    
    def __init__(self, data):
        self.data = data
        self.numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
    
    def univariate_analysis(self):
        """Comprehensive univariate analysis"""
        
        results = {}
        
        # Numeric variables
        for col in self.numeric_cols:
            fig, axes = plt.subplots(2, 2, figsize=(12, 8))
            
            # Histogram
            axes[0, 0].hist(self.data[col], bins=30, alpha=0.7, edgecolor='black')
            axes[0, 0].set_title(f'{col} - Histogram')
            axes[0, 0].axvline(self.data[col].mean(), color='red', linestyle='--', label='Mean')
            axes[0, 0].axvline(self.data[col].median(), color='green', linestyle='--', label='Median')
            axes[0, 0].legend()
            
            # Box plot
            axes[0, 1].boxplot(self.data[col])
            axes[0, 1].set_title(f'{col} - Box Plot')
            
            # Q-Q plot
            stats.probplot(self.data[col], dist="norm", plot=axes[1, 0])
            axes[1, 0].set_title(f'{col} - Q-Q Plot')
            
            # Density plot
            self.data[col].plot(kind='density', ax=axes[1, 1])
            axes[1, 1].set_title(f'{col} - Density Plot')
            
            plt.tight_layout()
            plt.show()
            
            # Statistical summary
            results[col] = comprehensive_stats(self.data, col)
        
        # Categorical variables
        for col in self.categorical_cols:
            fig, axes = plt.subplots(1, 2, figsize=(12, 4))
            
            # Value counts
            value_counts = self.data[col].value_counts()
            axes[0].bar(range(len(value_counts)), value_counts.values)
            axes[0].set_xticks(range(len(value_counts)))
            axes[0].set_xticklabels(value_counts.index, rotation=45)
            axes[0].set_title(f'{col} - Value Counts')
            
            # Pie chart
            axes[1].pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%')
            axes[1].set_title(f'{col} - Distribution')
            
            plt.tight_layout()
            plt.show()
            
            results[col] = {
                'unique_values': self.data[col].nunique(),
                'most_frequent': self.data[col].mode()[0],
                'value_counts': value_counts.to_dict()
            }
        
        return results
    
    def bivariate_analysis(self, target_col):
        """Comprehensive bivariate analysis"""
        
        if target_col in self.numeric_cols:
            # Numeric target
            for col in self.numeric_cols:
                if col != target_col:
                    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
                    
                    # Scatter plot
                    axes[0].scatter(self.data[col], self.data[target_col], alpha=0.6)
                    axes[0].set_xlabel(col)
                    axes[0].set_ylabel(target_col)
                    axes[0].set_title(f'{col} vs {target_col}')
                    
                    # Add correlation coefficient
                    corr = self.data[col].corr(self.data[target_col])
                    axes[0].text(0.05, 0.95, f'Correlation: {corr:.3f}', 
                               transform=axes[0].transAxes, bbox=dict(boxstyle="round", facecolor='wheat'))
                    
                    # Residual plot (if linear relationship)
                    from sklearn.linear_model import LinearRegression
                    X = self.data[col].values.reshape(-1, 1)
                    y = self.data[target_col].values
                    model = LinearRegression().fit(X, y)
                    y_pred = model.predict(X)
                    residuals = y - y_pred
                    
                    axes[1].scatter(y_pred, residuals, alpha=0.6)
                    axes[1].axhline(y=0, color='red', linestyle='--')
                    axes[1].set_xlabel('Predicted Values')
                    axes[1].set_ylabel('Residuals')
                    axes[1].set_title('Residual Plot')
                    
                    # Hexbin plot for large datasets
                    axes[2].hexbin(self.data[col], self.data[target_col], gridsize=20, cmap='Blues')
                    axes[2].set_xlabel(col)
                    axes[2].set_ylabel(target_col)
                    axes[2].set_title('Hexbin Plot')
                    
                    plt.tight_layout()
                    plt.show()
            
            # Categorical vs Numeric target
            for col in self.categorical_cols:
                fig, axes = plt.subplots(1, 2, figsize=(12, 4))
                
                # Box plot
                self.data.boxplot(column=target_col, by=col, ax=axes[0])
                axes[0].set_title(f'{target_col} by {col}')
                
                # Violin plot
                sns.violinplot(data=self.data, x=col, y=target_col, ax=axes[1])
                axes[1].set_title(f'{target_col} by {col} - Violin Plot')
                plt.xticks(rotation=45)
                
                plt.tight_layout()
                plt.show()
                
                # ANOVA test
                groups = [group[target_col].values for name, group in self.data.groupby(col)]
                f_stat, p_value = stats.f_oneway(*groups)
                print(f"ANOVA for {col} vs {target_col}: F={f_stat:.3f}, p={p_value:.3f}")
        
        else:
            # Categorical target
            for col in self.numeric_cols:
                # Distribution by target categories
                fig, axes = plt.subplots(1, 2, figsize=(12, 4))
                
                for category in self.data[target_col].unique():
                    subset = self.data[self.data[target_col] == category][col]
                    axes[0].hist(subset, alpha=0.7, label=category, bins=20)
                
                axes[0].set_xlabel(col)
                axes[0].set_ylabel('Frequency')
                axes[0].set_title(f'{col} Distribution by {target_col}')
                axes[0].legend()
                
                # Box plot
                self.data.boxplot(column=col, by=target_col, ax=axes[1])
                axes[1].set_title(f'{col} by {target_col}')
                
                plt.tight_layout()
                plt.show()
    
    def multivariate_analysis(self):
        """Multivariate analysis"""
        
        # Correlation heatmap
        if len(self.numeric_cols) > 1:
            plt.figure(figsize=(12, 8))
            correlation_matrix = self.data[self.numeric_cols].corr()
            
            # Create mask for upper triangle
            mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
            
            sns.heatmap(correlation_matrix, mask=mask, annot=True, cmap='coolwarm', 
                       center=0, square=True, linewidths=0.5)
            plt.title('Correlation Matrix')
            plt.show()
            
            # Find highly correlated pairs
            high_corr_pairs = []
            for i in range(len(correlation_matrix.columns)):
                for j in range(i+1, len(correlation_matrix.columns)):
                    if abs(correlation_matrix.iloc[i, j]) > 0.7:
                        high_corr_pairs.append((
                            correlation_matrix.columns[i],
                            correlation_matrix.columns[j],
                            correlation_matrix.iloc[i, j]
                        ))
            
            print("Highly correlated pairs (|r| > 0.7):")
            for pair in high_corr_pairs:
                print(f"{pair[0]} - {pair[1]}: {pair[2]:.3f}")
        
        # Principal Component Analysis
        if len(self.numeric_cols) > 2:
            from sklearn.decomposition import PCA
            from sklearn.preprocessing import StandardScaler
            
            # Standardize data
            scaler = StandardScaler()
            scaled_data = scaler.fit_transform(self.data[self.numeric_cols])
            
            # PCA
            pca = PCA()
            pca_result = pca.fit_transform(scaled_data)
            
            # Plot explained variance
            plt.figure(figsize=(10, 6))
            plt.subplot(1, 2, 1)
            plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), 
                    pca.explained_variance_ratio_, 'bo-')
            plt.xlabel('Principal Component')
            plt.ylabel('Explained Variance Ratio')
            plt.title('Scree Plot')
            
            plt.subplot(1, 2, 2)
            plt.plot(range(1, len(pca.explained_variance_ratio_) + 1), 
                    np.cumsum(pca.explained_variance_ratio_), 'ro-')
            plt.xlabel('Principal Component')
            plt.ylabel('Cumulative Explained Variance')
            plt.title('Cumulative Explained Variance')
            plt.axhline(y=0.8, color='k', linestyle='--', label='80% Variance')
            plt.legend()
            
            plt.tight_layout()
            plt.show()
            
            # Biplot for first two components
            if len(self.numeric_cols) >= 2:
                plt.figure(figsize=(10, 8))
                plt.scatter(pca_result[:, 0], pca_result[:, 1], alpha=0.6)
                
                # Add feature vectors
                feature_vectors = pca.components_.T * np.sqrt(pca.explained_variance_)
                for i, (feature, vector) in enumerate(zip(self.numeric_cols, feature_vectors)):
                    plt.arrow(0, 0, vector[0]*3, vector[1]*3, head_width=0.1, 
                             head_length=0.1, fc='red', ec='red')
                    plt.text(vector[0]*3.2, vector[1]*3.2, feature, fontsize=12)
                
                plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)')
                plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)')
                plt.title('PCA Biplot')
                plt.grid(True, alpha=0.3)
                plt.show()

# Usage
# eda = AdvancedEDA(df)
# univariate_results = eda.univariate_analysis()
# eda.bivariate_analysis('target_column')
# eda.multivariate_analysis()
```