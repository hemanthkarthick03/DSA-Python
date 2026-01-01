# Probability & Statistics for Data Science - Complete Guide

## Table of Contents
- [Probability Fundamentals](#probability-fundamentals)
- [Probability Distributions](#probability-distributions)
- [Descriptive Statistics](#descriptive-statistics)
- [Inferential Statistics](#inferential-statistics)
- [Hypothesis Testing](#hypothesis-testing)
- [Bayesian Statistics](#bayesian-statistics)
- [Statistical Modeling](#statistical-modeling)
- [Experimental Design](#experimental-design)
- [Time Series Statistics](#time-series-statistics)
- [Multivariate Statistics](#multivariate-statistics)
- [Statistical Learning Theory](#statistical-learning-theory)
- [Practical Applications](#practical-applications)

## Probability Fundamentals

### Basic Probability Rules
```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.special import comb
import seaborn as sns

# Fundamental probability rules
def probability_rules_demo():
    """Demonstrate fundamental probability rules"""
    
    # Sample space and events
    sample_space = set(range(1, 7))  # Die outcomes
    event_A = {1, 2, 3}  # Low numbers
    event_B = {2, 4, 6}  # Even numbers
    
    # Basic probabilities
    P_A = len(event_A) / len(sample_space)
    P_B = len(event_B) / len(sample_space)
    P_A_and_B = len(event_A.intersection(event_B)) / len(sample_space)
    P_A_or_B = len(event_A.union(event_B)) / len(sample_space)
    
    print("Probability Rules Demonstration:")
    print(f"P(A) = {P_A:.3f}")
    print(f"P(B) = {P_B:.3f}")
    print(f"P(A ∩ B) = {P_A_and_B:.3f}")
    print(f"P(A ∪ B) = {P_A_or_B:.3f}")
    
    # Addition rule: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
    addition_rule = P_A + P_B - P_A_and_B
    print(f"Addition Rule Check: {addition_rule:.3f} = {P_A_or_B:.3f}")
    
    # Conditional probability: P(A|B) = P(A ∩ B) / P(B)
    P_A_given_B = P_A_and_B / P_B if P_B > 0 else 0
    print(f"P(A|B) = {P_A_given_B:.3f}")
    
    return {
        'P_A': P_A,
        'P_B': P_B,
        'P_A_and_B': P_A_and_B,
        'P_A_or_B': P_A_or_B,
        'P_A_given_B': P_A_given_B
    }

# Combinatorics for probability
def combinatorics_examples():
    """Examples of combinatorics in probability"""
    
    # Permutations: P(n,r) = n! / (n-r)!
    def permutations(n, r):
        return np.math.factorial(n) // np.math.factorial(n - r)
    
    # Combinations: C(n,r) = n! / (r!(n-r)!)
    def combinations(n, r):
        return comb(n, r, exact=True)
    
    print("Combinatorics Examples:")
    print(f"Permutations P(5,3) = {permutations(5, 3)}")
    print(f"Combinations C(5,3) = {combinations(5, 3)}")
    
    # Probability examples
    # Example 1: Probability of getting exactly 2 heads in 5 coin flips
    n_flips = 5
    n_heads = 2
    prob_head = 0.5
    
    prob_exact_heads = combinations(n_flips, n_heads) * (prob_head ** n_heads) * ((1 - prob_head) ** (n_flips - n_heads))
    print(f"P(exactly 2 heads in 5 flips) = {prob_exact_heads:.4f}")
    
    # Example 2: Birthday paradox
    def birthday_paradox(n_people):
        """Calculate probability that at least 2 people share a birthday"""
        if n_people > 365:
            return 1.0
        
        prob_all_different = 1.0
        for i in range(n_people):
            prob_all_different *= (365 - i) / 365
        
        return 1 - prob_all_different
    
    for n in [10, 20, 23, 30, 50]:
        prob = birthday_paradox(n)
        print(f"Birthday paradox with {n} people: {prob:.4f}")

# probability_rules_demo()
# combinatorics_examples()
```

### Conditional Probability and Independence
```python
def conditional_probability_examples():
    """Demonstrate conditional probability concepts"""
    
    # Medical test example
    # Disease prevalence: 1%
    # Test sensitivity (true positive rate): 95%
    # Test specificity (true negative rate): 90%
    
    P_disease = 0.01
    P_no_disease = 1 - P_disease
    P_positive_given_disease = 0.95  # Sensitivity
    P_negative_given_no_disease = 0.90  # Specificity
    P_positive_given_no_disease = 1 - P_negative_given_no_disease  # False positive rate
    
    # Total probability of positive test
    P_positive = (P_positive_given_disease * P_disease + 
                 P_positive_given_no_disease * P_no_disease)
    
    # Bayes' theorem: P(Disease|Positive) = P(Positive|Disease) * P(Disease) / P(Positive)
    P_disease_given_positive = (P_positive_given_disease * P_disease) / P_positive
    
    print("Medical Test Example:")
    print(f"Disease prevalence: {P_disease:.1%}")
    print(f"Test sensitivity: {P_positive_given_disease:.1%}")
    print(f"Test specificity: {P_negative_given_no_disease:.1%}")
    print(f"P(Positive test) = {P_positive:.4f}")
    print(f"P(Disease|Positive test) = {P_disease_given_positive:.4f} ({P_disease_given_positive:.1%})")
    
    # Independence test
    def test_independence(data, var1, var2):
        """Test if two variables are independent"""
        # Create contingency table
        contingency_table = pd.crosstab(data[var1], data[var2])
        
        # Chi-square test for independence
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        
        return {
            'chi2_statistic': chi2,
            'p_value': p_value,
            'degrees_of_freedom': dof,
            'is_independent': p_value > 0.05,
            'contingency_table': contingency_table,
            'expected_frequencies': expected
        }
    
    return P_disease_given_positive

# Example of Monty Hall problem
def monty_hall_simulation(n_simulations=10000):
    """Simulate the Monty Hall problem"""
    
    wins_stay = 0
    wins_switch = 0
    
    for _ in range(n_simulations):
        # Setup: car behind one of three doors
        car_door = np.random.randint(1, 4)
        
        # Contestant chooses a door
        chosen_door = np.random.randint(1, 4)
        
        # Host opens a door with a goat (not car, not chosen)
        available_doors = [d for d in [1, 2, 3] if d != car_door and d != chosen_door]
        if len(available_doors) == 2:
            # If contestant chose car door, host can open either remaining door
            host_opens = np.random.choice(available_doors)
        else:
            # If contestant didn't choose car door, host must open the other goat door
            host_opens = available_doors[0]
        
        # Remaining door for switching
        remaining_doors = [d for d in [1, 2, 3] if d != chosen_door and d != host_opens]
        switch_door = remaining_doors[0]
        
        # Check wins
        if chosen_door == car_door:
            wins_stay += 1
        if switch_door == car_door:
            wins_switch += 1
    
    prob_win_stay = wins_stay / n_simulations
    prob_win_switch = wins_switch / n_simulations
    
    print("Monty Hall Problem Simulation:")
    print(f"Probability of winning by staying: {prob_win_stay:.3f}")
    print(f"Probability of winning by switching: {prob_win_switch:.3f}")
    print(f"Theoretical probabilities: Stay = 1/3, Switch = 2/3")
    
    return prob_win_stay, prob_win_switch

# monty_hall_simulation()
```

## Probability Distributions

### Discrete Distributions
```python
def discrete_distributions_guide():
    """Comprehensive guide to discrete probability distributions"""
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # 1. Bernoulli Distribution
    # Single trial with probability p of success
    p = 0.3
    x_bernoulli = [0, 1]
    pmf_bernoulli = [1-p, p]
    
    axes[0, 0].bar(x_bernoulli, pmf_bernoulli, alpha=0.7, color='skyblue')
    axes[0, 0].set_title(f'Bernoulli Distribution (p={p})')
    axes[0, 0].set_xlabel('Outcome')
    axes[0, 0].set_ylabel('Probability')
    
    # 2. Binomial Distribution
    # n independent Bernoulli trials
    n, p = 20, 0.3
    x_binomial = np.arange(0, n+1)
    pmf_binomial = stats.binom.pmf(x_binomial, n, p)
    
    axes[0, 1].bar(x_binomial, pmf_binomial, alpha=0.7, color='lightgreen')
    axes[0, 1].set_title(f'Binomial Distribution (n={n}, p={p})')
    axes[0, 1].set_xlabel('Number of Successes')
    axes[0, 1].set_ylabel('Probability')
    
    # Add mean and variance
    mean_binom = n * p
    var_binom = n * p * (1 - p)
    axes[0, 1].axvline(mean_binom, color='red', linestyle='--', label=f'Mean={mean_binom:.1f}')
    axes[0, 1].legend()
    
    # 3. Poisson Distribution
    # Number of events in fixed interval
    lambda_vals = [1, 4, 10]
    x_poisson = np.arange(0, 20)
    
    for lam in lambda_vals:
        pmf_poisson = stats.poisson.pmf(x_poisson, lam)
        axes[0, 2].plot(x_poisson, pmf_poisson, 'o-', label=f'λ={lam}', alpha=0.7)
    
    axes[0, 2].set_title('Poisson Distribution')
    axes[0, 2].set_xlabel('Number of Events')
    axes[0, 2].set_ylabel('Probability')
    axes[0, 2].legend()
    
    # 4. Geometric Distribution
    # Number of trials until first success
    p_geom = 0.2
    x_geometric = np.arange(1, 21)
    pmf_geometric = stats.geom.pmf(x_geometric, p_geom)
    
    axes[1, 0].bar(x_geometric, pmf_geometric, alpha=0.7, color='orange')
    axes[1, 0].set_title(f'Geometric Distribution (p={p_geom})')
    axes[1, 0].set_xlabel('Trial of First Success')
    axes[1, 0].set_ylabel('Probability')
    
    # 5. Negative Binomial Distribution
    # Number of failures before r-th success
    r, p_nb = 5, 0.3
    x_negbinom = np.arange(0, 30)
    pmf_negbinom = stats.nbinom.pmf(x_negbinom, r, p_nb)
    
    axes[1, 1].bar(x_negbinom, pmf_negbinom, alpha=0.7, color='purple')
    axes[1, 1].set_title(f'Negative Binomial (r={r}, p={p_nb})')
    axes[1, 1].set_xlabel('Number of Failures')
    axes[1, 1].set_ylabel('Probability')
    
    # 6. Hypergeometric Distribution
    # Sampling without replacement
    N, K, n = 50, 20, 10  # Population size, success states, sample size
    x_hypergeom = np.arange(0, min(n, K) + 1)
    pmf_hypergeom = stats.hypergeom.pmf(x_hypergeom, N, K, n)
    
    axes[1, 2].bar(x_hypergeom, pmf_hypergeom, alpha=0.7, color='red')
    axes[1, 2].set_title(f'Hypergeometric (N={N}, K={K}, n={n})')
    axes[1, 2].set_xlabel('Number of Successes')
    axes[1, 2].set_ylabel('Probability')
    
    plt.tight_layout()
    plt.show()
    
    # Print key properties
    print("Discrete Distribution Properties:")
    print("1. Bernoulli: E[X] = p, Var(X) = p(1-p)")
    print("2. Binomial: E[X] = np, Var(X) = np(1-p)")
    print("3. Poisson: E[X] = λ, Var(X) = λ")
    print("4. Geometric: E[X] = 1/p, Var(X) = (1-p)/p²")
    print("5. Negative Binomial: E[X] = r(1-p)/p, Var(X) = r(1-p)/p²")
    print("6. Hypergeometric: E[X] = n(K/N), Var(X) = n(K/N)(1-K/N)(N-n)/(N-1)")

# discrete_distributions_guide()
```

### Continuous Distributions
```python
def continuous_distributions_guide():
    """Comprehensive guide to continuous probability distributions"""
    
    fig, axes = plt.subplots(3, 3, figsize=(18, 15))
    x = np.linspace(-4, 4, 1000)
    
    # 1. Normal Distribution
    mu_vals = [0, 0, 0]
    sigma_vals = [0.5, 1, 2]
    
    for mu, sigma in zip(mu_vals, sigma_vals):
        pdf_normal = stats.norm.pdf(x, mu, sigma)
        axes[0, 0].plot(x, pdf_normal, label=f'μ={mu}, σ={sigma}')
    
    axes[0, 0].set_title('Normal Distribution')
    axes[0, 0].set_xlabel('x')
    axes[0, 0].set_ylabel('Probability Density')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Exponential Distribution
    x_exp = np.linspace(0, 5, 1000)
    lambda_vals = [0.5, 1, 2]
    
    for lam in lambda_vals:
        pdf_exp = stats.expon.pdf(x_exp, scale=1/lam)
        axes[0, 1].plot(x_exp, pdf_exp, label=f'λ={lam}')
    
    axes[0, 1].set_title('Exponential Distribution')
    axes[0, 1].set_xlabel('x')
    axes[0, 1].set_ylabel('Probability Density')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Gamma Distribution
    x_gamma = np.linspace(0, 10, 1000)
    alpha_vals = [1, 2, 3]
    beta_vals = [1, 1, 1]
    
    for alpha, beta in zip(alpha_vals, beta_vals):
        pdf_gamma = stats.gamma.pdf(x_gamma, alpha, scale=1/beta)
        axes[0, 2].plot(x_gamma, pdf_gamma, label=f'α={alpha}, β={beta}')
    
    axes[0, 2].set_title('Gamma Distribution')
    axes[0, 2].set_xlabel('x')
    axes[0, 2].set_ylabel('Probability Density')
    axes[0, 2].legend()
    axes[0, 2].grid(True, alpha=0.3)
    
    # 4. Beta Distribution
    x_beta = np.linspace(0, 1, 1000)
    alpha_beta_pairs = [(0.5, 0.5), (2, 2), (2, 5)]
    
    for alpha, beta in alpha_beta_pairs:
        pdf_beta = stats.beta.pdf(x_beta, alpha, beta)
        axes[1, 0].plot(x_beta, pdf_beta, label=f'α={alpha}, β={beta}')
    
    axes[1, 0].set_title('Beta Distribution')
    axes[1, 0].set_xlabel('x')
    axes[1, 0].set_ylabel('Probability Density')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # 5. Chi-square Distribution
    x_chi2 = np.linspace(0, 15, 1000)
    df_vals = [1, 3, 5, 9]
    
    for df in df_vals:
        pdf_chi2 = stats.chi2.pdf(x_chi2, df)
        axes[1, 1].plot(x_chi2, pdf_chi2, label=f'df={df}')
    
    axes[1, 1].set_title('Chi-square Distribution')
    axes[1, 1].set_xlabel('x')
    axes[1, 1].set_ylabel('Probability Density')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    # 6. t-Distribution
    x_t = np.linspace(-4, 4, 1000)
    df_vals = [1, 3, 10, 30]
    
    for df in df_vals:
        pdf_t = stats.t.pdf(x_t, df)
        axes[1, 2].plot(x_t, pdf_t, label=f'df={df}')
    
    # Add normal for comparison
    pdf_normal = stats.norm.pdf(x_t, 0, 1)
    axes[1, 2].plot(x_t, pdf_normal, '--', label='Normal', alpha=0.7)
    
    axes[1, 2].set_title('t-Distribution')
    axes[1, 2].set_xlabel('x')
    axes[1, 2].set_ylabel('Probability Density')
    axes[1, 2].legend()
    axes[1, 2].grid(True, alpha=0.3)
    
    # 7. F-Distribution
    x_f = np.linspace(0, 5, 1000)
    df_pairs = [(1, 1), (5, 10), (10, 5)]
    
    for df1, df2 in df_pairs:
        pdf_f = stats.f.pdf(x_f, df1, df2)
        axes[2, 0].plot(x_f, pdf_f, label=f'df1={df1}, df2={df2}')
    
    axes[2, 0].set_title('F-Distribution')
    axes[2, 0].set_xlabel('x')
    axes[2, 0].set_ylabel('Probability Density')
    axes[2, 0].legend()
    axes[2, 0].grid(True, alpha=0.3)
    
    # 8. Uniform Distribution
    x_uniform = np.linspace(-1, 3, 1000)
    a, b = 0, 2
    pdf_uniform = stats.uniform.pdf(x_uniform, a, b-a)
    
    axes[2, 1].plot(x_uniform, pdf_uniform, linewidth=3, label=f'a={a}, b={b}')
    axes[2, 1].set_title('Uniform Distribution')
    axes[2, 1].set_xlabel('x')
    axes[2, 1].set_ylabel('Probability Density')
    axes[2, 1].legend()
    axes[2, 1].grid(True, alpha=0.3)
    
    # 9. Log-normal Distribution
    x_lognorm = np.linspace(0, 5, 1000)
    sigma_vals = [0.25, 0.5, 1]
    
    for sigma in sigma_vals:
        pdf_lognorm = stats.lognorm.pdf(x_lognorm, sigma)
        axes[2, 2].plot(x_lognorm, pdf_lognorm, label=f'σ={sigma}')
    
    axes[2, 2].set_title('Log-normal Distribution')
    axes[2, 2].set_xlabel('x')
    axes[2, 2].set_ylabel('Probability Density')
    axes[2, 2].legend()
    axes[2, 2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Distribution relationships and use cases
    print("Continuous Distribution Use Cases:")
    print("1. Normal: Natural phenomena, measurement errors, CLT")
    print("2. Exponential: Time between events, reliability analysis")
    print("3. Gamma: Waiting times, rainfall amounts")
    print("4. Beta: Probabilities, proportions, Bayesian priors")
    print("5. Chi-square: Goodness of fit tests, variance estimation")
    print("6. t-Distribution: Small sample inference, confidence intervals")
    print("7. F-Distribution: ANOVA, comparing variances")
    print("8. Uniform: Random number generation, lack of information")
    print("9. Log-normal: Stock prices, income distribution")

# continuous_distributions_guide()
```

### Central Limit Theorem
```python
def central_limit_theorem_demo():
    """Demonstrate Central Limit Theorem with different populations"""
    
    np.random.seed(42)
    
    # Different population distributions
    populations = {
        'Exponential': lambda size: np.random.exponential(2, size),
        'Uniform': lambda size: np.random.uniform(0, 10, size),
        'Bimodal': lambda size: np.concatenate([
            np.random.normal(2, 1, size//2),
            np.random.normal(8, 1, size//2)
        ]),
        'Skewed': lambda size: np.random.gamma(2, 2, size)
    }
    
    sample_sizes = [1, 5, 10, 30, 100]
    n_samples = 1000
    
    fig, axes = plt.subplots(len(populations), len(sample_sizes), figsize=(20, 16))
    
    for i, (pop_name, pop_func) in enumerate(populations.items()):
        # Generate population
        population = pop_func(10000)
        pop_mean = np.mean(population)
        pop_std = np.std(population)
        
        for j, sample_size in enumerate(sample_sizes):
            # Generate sampling distribution
            sample_means = []
            for _ in range(n_samples):
                sample = pop_func(sample_size)
                sample_means.append(np.mean(sample))
            
            sample_means = np.array(sample_means)
            
            # Plot histogram
            axes[i, j].hist(sample_means, bins=50, density=True, alpha=0.7, 
                          color='skyblue', edgecolor='black')
            
            # Overlay theoretical normal distribution
            if sample_size > 1:
                theoretical_mean = pop_mean
                theoretical_std = pop_std / np.sqrt(sample_size)
                x_theory = np.linspace(sample_means.min(), sample_means.max(), 100)
                y_theory = stats.norm.pdf(x_theory, theoretical_mean, theoretical_std)
                axes[i, j].plot(x_theory, y_theory, 'r-', linewidth=2, 
                              label='Theoretical Normal')
            
            # Add statistics
            actual_mean = np.mean(sample_means)
            actual_std = np.std(sample_means)
            
            axes[i, j].axvline(actual_mean, color='green', linestyle='--', 
                             label=f'Sample Mean: {actual_mean:.2f}')
            
            axes[i, j].set_title(f'{pop_name}\nSample Size: {sample_size}')
            axes[i, j].set_xlabel('Sample Mean')
            axes[i, j].set_ylabel('Density')
            
            if j == 0:
                axes[i, j].set_ylabel(f'{pop_name}\nDensity')
            
            # Add text with statistics
            textstr = f'Mean: {actual_mean:.2f}\nStd: {actual_std:.2f}'
            if sample_size > 1:
                textstr += f'\nTheory Std: {pop_std/np.sqrt(sample_size):.2f}'
            
            axes[i, j].text(0.05, 0.95, textstr, transform=axes[i, j].transAxes,
                          verticalalignment='top', bbox=dict(boxstyle='round', 
                          facecolor='wheat', alpha=0.8))
            
            # Normality test for larger samples
            if sample_size >= 30:
                _, p_value = stats.shapiro(sample_means[:5000])  # Shapiro-Wilk test
                is_normal = p_value > 0.05
                axes[i, j].text(0.05, 0.05, f'Normal: {"Yes" if is_normal else "No"}',
                              transform=axes[i, j].transAxes,
                              bbox=dict(boxstyle='round', 
                              facecolor='lightgreen' if is_normal else 'lightcoral'))
    
    plt.tight_layout()
    plt.show()
    
    # Summary of CLT
    print("Central Limit Theorem Key Points:")
    print("1. Sample means approach normal distribution as n increases")
    print("2. Mean of sampling distribution equals population mean")
    print("3. Standard error = population_std / sqrt(n)")
    print("4. Works regardless of population distribution shape")
    print("5. Rule of thumb: n ≥ 30 for CLT to apply")

# central_limit_theorem_demo()
```

## Descriptive Statistics

### Measures of Central Tendency and Spread
```python
def comprehensive_descriptive_stats(data):
    """Calculate comprehensive descriptive statistics"""
    
    import pandas as pd
    from scipy import stats
    
    # Convert to pandas Series if not already
    if not isinstance(data, pd.Series):
        data = pd.Series(data)
    
    # Remove missing values
    clean_data = data.dropna()
    n = len(clean_data)
    
    # Measures of central tendency
    mean = np.mean(clean_data)
    median = np.median(clean_data)
    mode_result = stats.mode(clean_data, keepdims=True)
    mode = mode_result.mode[0] if len(mode_result.mode) > 0 else np.nan
    
    # Measures of spread
    variance = np.var(clean_data, ddof=1)  # Sample variance
    std_dev = np.std(clean_data, ddof=1)   # Sample standard deviation
    range_val = np.max(clean_data) - np.min(clean_data)
    
    # Quartiles and IQR
    q1 = np.percentile(clean_data, 25)
    q2 = np.percentile(clean_data, 50)  # Same as median
    q3 = np.percentile(clean_data, 75)
    iqr = q3 - q1
    
    # Other percentiles
    p10 = np.percentile(clean_data, 10)
    p90 = np.percentile(clean_data, 90)
    
    # Measures of shape
    skewness = stats.skew(clean_data)
    kurtosis = stats.kurtosis(clean_data)  # Excess kurtosis
    
    # Robust statistics
    mad = stats.median_abs_deviation(clean_data)  # Median Absolute Deviation
    trimmed_mean = stats.trim_mean(clean_data, 0.1)  # 10% trimmed mean
    
    # Coefficient of variation
    cv = std_dev / mean if mean != 0 else np.inf
    
    # Outlier detection using IQR method
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    outliers = clean_data[(clean_data < lower_fence) | (clean_data > upper_fence)]
    
    # Z-score outliers
    z_scores = np.abs(stats.zscore(clean_data))
    z_outliers = clean_data[z_scores > 3]
    
    results = {
        'count': n,
        'missing': len(data) - n,
        'mean': mean,
        'median': median,
        'mode': mode,
        'std_dev': std_dev,
        'variance': variance,
        'range': range_val,
        'min': np.min(clean_data),
        'max': np.max(clean_data),
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'iqr': iqr,
        'p10': p10,
        'p90': p90,
        'skewness': skewness,
        'kurtosis': kurtosis,
        'mad': mad,
        'trimmed_mean': trimmed_mean,
        'cv': cv,
        'iqr_outliers': len(outliers),
        'z_outliers': len(z_outliers)
    }
    
    return results

def visualize_distribution(data, title="Distribution Analysis"):
    """Create comprehensive distribution visualization"""
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # 1. Histogram with density curve
    axes[0, 0].hist(data, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')
    
    # Fit normal distribution
    mu, sigma = stats.norm.fit(data)
    x = np.linspace(data.min(), data.max(), 100)
    axes[0, 0].plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2, label='Normal fit')
    
    # Add mean and median lines
    axes[0, 0].axvline(np.mean(data), color='red', linestyle='--', label=f'Mean: {np.mean(data):.2f}')
    axes[0, 0].axvline(np.median(data), color='green', linestyle='--', label=f'Median: {np.median(data):.2f}')
    
    axes[0, 0].set_title('Histogram with Normal Fit')
    axes[0, 0].set_xlabel('Value')
    axes[0, 0].set_ylabel('Density')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Box plot
    box_plot = axes[0, 1].boxplot(data, patch_artist=True)
    box_plot['boxes'][0].set_facecolor('lightblue')
    axes[0, 1].set_title('Box Plot')
    axes[0, 1].set_ylabel('Value')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Q-Q plot
    stats.probplot(data, dist="norm", plot=axes[0, 2])
    axes[0, 2].set_title('Q-Q Plot (Normal)')
    axes[0, 2].grid(True, alpha=0.3)
    
    # 4. Violin plot
    parts = axes[1, 0].violinplot([data], positions=[1], showmeans=True, showmedians=True)
    axes[1, 0].set_title('Violin Plot')
    axes[1, 0].set_ylabel('Value')
    axes[1, 0].set_xticks([1])
    axes[1, 0].set_xticklabels(['Data'])
    axes[1, 0].grid(True, alpha=0.3)
    
    # 5. Empirical CDF
    sorted_data = np.sort(data)
    y = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
    axes[1, 1].plot(sorted_data, y, 'b-', linewidth=2, label='Empirical CDF')
    
    # Theoretical normal CDF
    axes[1, 1].plot(x, stats.norm.cdf(x, mu, sigma), 'r--', linewidth=2, label='Normal CDF')
    
    axes[1, 1].set_title('Cumulative Distribution Function')
    axes[1, 1].set_xlabel('Value')
    axes[1, 1].set_ylabel('Cumulative Probability')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    # 6. Summary statistics text
    stats_dict = comprehensive_descriptive_stats(data)
    stats_text = f"""
    Count: {stats_dict['count']}
    Mean: {stats_dict['mean']:.3f}
    Median: {stats_dict['median']:.3f}
    Std Dev: {stats_dict['std_dev']:.3f}
    Skewness: {stats_dict['skewness']:.3f}
    Kurtosis: {stats_dict['kurtosis']:.3f}
    IQR: {stats_dict['iqr']:.3f}
    CV: {stats_dict['cv']:.3f}
    """
    
    axes[1, 2].text(0.1, 0.9, stats_text, transform=axes[1, 2].transAxes,
                    verticalalignment='top', fontsize=12,
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    axes[1, 2].set_title('Summary Statistics')
    axes[1, 2].axis('off')
    
    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()
    
    return stats_dict

# Example usage
# np.random.seed(42)
# sample_data = np.random.gamma(2, 2, 1000)  # Skewed data
# stats_results = visualize_distribution(sample_data, "Gamma Distribution Analysis")
```

## Inferential Statistics

### Confidence Intervals
```python
def confidence_intervals_guide():
    """Comprehensive guide to confidence intervals"""
    
    # Generate sample data
    np.random.seed(42)
    population_mean = 100
    population_std = 15
    sample_sizes = [10, 30, 100, 500]
    confidence_levels = [0.90, 0.95, 0.99]
    
    def calculate_ci_mean(data, confidence=0.95):
        """Calculate confidence interval for mean"""
        n = len(data)
        mean = np.mean(data)
        std_err = stats.sem(data)  # Standard error of mean
        
        # For small samples (n < 30), use t-distribution
        if n < 30:
            df = n - 1
            t_critical = stats.t.ppf((1 + confidence) / 2, df)
            margin_error = t_critical * std_err
        else:
            # For large samples, use normal distribution
            z_critical = stats.norm.ppf((1 + confidence) / 2)
            margin_error = z_critical * std_err
        
        ci_lower = mean - margin_error
        ci_upper = mean + margin_error
        
        return mean, ci_lower, ci_upper, margin_error
    
    def calculate_ci_proportion(successes, n, confidence=0.95):
        """Calculate confidence interval for proportion"""
        p_hat = successes / n
        z_critical = stats.norm.ppf((1 + confidence) / 2)
        
        # Standard error for proportion
        std_err = np.sqrt(p_hat * (1 - p_hat) / n)
        margin_error = z_critical * std_err
        
        ci_lower = max(0, p_hat - margin_error)
        ci_upper = min(1, p_hat + margin_error)
        
        return p_hat, ci_lower, ci_upper, margin_error
    
    # Demonstrate CI for means
    print("Confidence Intervals for Population Mean")
    print("=" * 50)
    print(f"True population mean: {population_mean}")
    print(f"True population std: {population_std}")
    print()
    
    results = []
    
    for sample_size in sample_sizes:
        sample = np.random.normal(population_mean, population_std, sample_size)
        
        print(f"Sample size: {sample_size}")
        for conf_level in confidence_levels:
            mean, ci_lower, ci_upper, margin_error = calculate_ci_mean(sample, conf_level)
            contains_true_mean = ci_lower <= population_mean <= ci_upper
            
            print(f"  {conf_level*100:.0f}% CI: [{ci_lower:.2f}, {ci_upper:.2f}] "
                  f"(width: {ci_upper - ci_lower:.2f}) "
                  f"{'✓' if contains_true_mean else '✗'}")
            
            results.append({
                'sample_size': sample_size,
                'confidence': conf_level,
                'ci_lower': ci_lower,
                'ci_upper': ci_upper,
                'width': ci_upper - ci_lower,
                'contains_true': contains_true_mean
            })
        print()
    
    # Visualize CI widths
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # CI width vs sample size
    for conf_level in confidence_levels:
        widths = [r['width'] for r in results if r['confidence'] == conf_level]
        axes[0].plot(sample_sizes, widths, 'o-', label=f'{conf_level*100:.0f}% CI')
    
    axes[0].set_xlabel('Sample Size')
    axes[0].set_ylabel('CI Width')
    axes[0].set_title('Confidence Interval Width vs Sample Size')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xscale('log')
    
    # CI coverage simulation
    n_simulations = 1000
    coverage_results = {}
    
    for conf_level in confidence_levels:
        coverage_count = 0
        for _ in range(n_simulations):
            sample = np.random.normal(population_mean, population_std, 50)
            _, ci_lower, ci_upper, _ = calculate_ci_mean(sample, conf_level)
            if ci_lower <= population_mean <= ci_upper:
                coverage_count += 1
        
        coverage_results[conf_level] = coverage_count / n_simulations
    
    conf_levels_pct = [cl * 100 for cl in confidence_levels]
    coverage_pct = [coverage_results[cl] * 100 for cl in confidence_levels]
    
    axes[1].bar(conf_levels_pct, coverage_pct, alpha=0.7, color='skyblue')
    axes[1].plot(conf_levels_pct, conf_levels_pct, 'r--', label='Expected Coverage')
    axes[1].set_xlabel('Confidence Level (%)')
    axes[1].set_ylabel('Actual Coverage (%)')
    axes[1].set_title('CI Coverage Simulation (n=1000)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Bootstrap confidence intervals
    def bootstrap_ci(data, statistic=np.mean, n_bootstrap=1000, confidence=0.95):
        """Calculate bootstrap confidence interval"""
        bootstrap_stats = []
        n = len(data)
        
        for _ in range(n_bootstrap):
            bootstrap_sample = np.random.choice(data, size=n, replace=True)
            bootstrap_stats.append(statistic(bootstrap_sample))
        
        bootstrap_stats = np.array(bootstrap_stats)
        alpha = 1 - confidence
        ci_lower = np.percentile(bootstrap_stats, 100 * alpha / 2)
        ci_upper = np.percentile(bootstrap_stats, 100 * (1 - alpha / 2))
        
        return ci_lower, ci_upper, bootstrap_stats
    
    # Example with bootstrap
    sample_data = np.random.exponential(2, 100)  # Non-normal data
    
    print("Bootstrap Confidence Intervals (Non-normal data)")
    print("=" * 50)
    
    statistics = {
        'Mean': np.mean,
        'Median': np.median,
        'Standard Deviation': lambda x: np.std(x, ddof=1)
    }
    
    for stat_name, stat_func in statistics.items():
        ci_lower, ci_upper, bootstrap_dist = bootstrap_ci(sample_data, stat_func)
        observed_stat = stat_func(sample_data)
        
        print(f"{stat_name}: {observed_stat:.3f}")
        print(f"  95% Bootstrap CI: [{ci_lower:.3f}, {ci_upper:.3f}]")
        print()

# confidence_intervals_guide()
```

## Hypothesis Testing

### Complete Hypothesis Testing Framework
```python
class HypothesisTestingFramework:
    """Comprehensive hypothesis testing framework"""
    
    def __init__(self, alpha=0.05):
        self.alpha = alpha
        self.test_results = {}
    
    def one_sample_t_test(self, data, mu0, alternative='two-sided'):
        """One-sample t-test"""
        n = len(data)
        sample_mean = np.mean(data)
        sample_std = np.std(data, ddof=1)
        se = sample_std / np.sqrt(n)
        
        # Calculate t-statistic
        t_stat = (sample_mean - mu0) / se
        df = n - 1
        
        # Calculate p-value based on alternative hypothesis
        if alternative == 'two-sided':
            p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        elif alternative == 'greater':
            p_value = 1 - stats.t.cdf(t_stat, df)
        elif alternative == 'less':
            p_value = stats.t.cdf(t_stat, df)
        
        # Critical value
        if alternative == 'two-sided':
            t_critical = stats.t.ppf(1 - self.alpha/2, df)
        else:
            t_critical = stats.t.ppf(1 - self.alpha, df)
        
        # Decision
        reject_null = p_value < self.alpha
        
        result = {
            'test_type': 'One-sample t-test',
            'null_hypothesis': f'μ = {mu0}',
            'alternative_hypothesis': f'μ {self._get_alt_symbol(alternative)} {mu0}',
            'sample_mean': sample_mean,
            'sample_std': sample_std,
            'sample_size': n,
            't_statistic': t_stat,
            'degrees_of_freedom': df,
            'p_value': p_value,
            't_critical': t_critical,
            'alpha': self.alpha,
            'reject_null': reject_null,
            'conclusion': self._get_conclusion(reject_null, alternative, mu0)
        }
        
        return result
    
    def two_sample_t_test(self, data1, data2, equal_var=True, alternative='two-sided'):
        """Two-sample t-test"""
        n1, n2 = len(data1), len(data2)
        mean1, mean2 = np.mean(data1), np.mean(data2)
        std1, std2 = np.std(data1, ddof=1), np.std(data2, ddof=1)
        
        if equal_var:
            # Pooled variance
            pooled_var = ((n1-1)*std1**2 + (n2-1)*std2**2) / (n1+n2-2)
            se = np.sqrt(pooled_var * (1/n1 + 1/n2))
            df = n1 + n2 - 2
        else:
            # Welch's t-test (unequal variances)
            se = np.sqrt(std1**2/n1 + std2**2/n2)
            df = (std1**2/n1 + std2**2/n2)**2 / ((std1**2/n1)**2/(n1-1) + (std2**2/n2)**2/(n2-1))
        
        t_stat = (mean1 - mean2) / se
        
        # Calculate p-value
        if alternative == 'two-sided':
            p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        elif alternative == 'greater':
            p_value = 1 - stats.t.cdf(t_stat, df)
        elif alternative == 'less':
            p_value = stats.t.cdf(t_stat, df)
        
        reject_null = p_value < self.alpha
        
        result = {
            'test_type': f'Two-sample t-test ({"equal" if equal_var else "unequal"} variances)',
            'null_hypothesis': 'μ₁ = μ₂',
            'alternative_hypothesis': f'μ₁ {self._get_alt_symbol(alternative)} μ₂',
            'sample1_mean': mean1,
            'sample2_mean': mean2,
            'sample1_std': std1,
            'sample2_std': std2,
            'sample1_size': n1,
            'sample2_size': n2,
            't_statistic': t_stat,
            'degrees_of_freedom': df,
            'p_value': p_value,
            'alpha': self.alpha,
            'reject_null': reject_null,
            'effect_size': self._cohens_d(data1, data2)
        }
        
        return result
    
    def paired_t_test(self, before, after, alternative='two-sided'):
        """Paired t-test"""
        differences = np.array(after) - np.array(before)
        return self.one_sample_t_test(differences, 0, alternative)
    
    def chi_square_test(self, observed, expected=None):
        """Chi-square goodness of fit test"""
        observed = np.array(observed)
        
        if expected is None:
            # Equal expected frequencies
            expected = np.full_like(observed, np.sum(observed) / len(observed))
        else:
            expected = np.array(expected)
        
        chi2_stat = np.sum((observed - expected)**2 / expected)
        df = len(observed) - 1
        p_value = 1 - stats.chi2.cdf(chi2_stat, df)
        
        reject_null = p_value < self.alpha
        
        result = {
            'test_type': 'Chi-square goodness of fit',
            'null_hypothesis': 'Observed frequencies match expected',
            'chi2_statistic': chi2_stat,
            'degrees_of_freedom': df,
            'p_value': p_value,
            'alpha': self.alpha,
            'reject_null': reject_null,
            'observed': observed,
            'expected': expected
        }
        
        return result
    
    def chi_square_independence(self, contingency_table):
        """Chi-square test of independence"""
        chi2_stat, p_value, df, expected = stats.chi2_contingency(contingency_table)
        
        reject_null = p_value < self.alpha
        
        # Cramér's V (effect size)
        n = np.sum(contingency_table)
        cramers_v = np.sqrt(chi2_stat / (n * (min(contingency_table.shape) - 1)))
        
        result = {
            'test_type': 'Chi-square test of independence',
            'null_hypothesis': 'Variables are independent',
            'chi2_statistic': chi2_stat,
            'degrees_of_freedom': df,
            'p_value': p_value,
            'alpha': self.alpha,
            'reject_null': reject_null,
            'cramers_v': cramers_v,
            'contingency_table': contingency_table,
            'expected_frequencies': expected
        }
        
        return result
    
    def anova_one_way(self, *groups):
        """One-way ANOVA"""
        f_stat, p_value = stats.f_oneway(*groups)
        
        # Calculate degrees of freedom
        k = len(groups)  # number of groups
        n = sum(len(group) for group in groups)  # total sample size
        df_between = k - 1
        df_within = n - k
        
        reject_null = p_value < self.alpha
        
        # Effect size (eta-squared)
        all_data = np.concatenate(groups)
        grand_mean = np.mean(all_data)
        
        ss_between = sum(len(group) * (np.mean(group) - grand_mean)**2 for group in groups)
        ss_total = sum((x - grand_mean)**2 for x in all_data)
        eta_squared = ss_between / ss_total
        
        result = {
            'test_type': 'One-way ANOVA',
            'null_hypothesis': 'All group means are equal',
            'f_statistic': f_stat,
            'df_between': df_between,
            'df_within': df_within,
            'p_value': p_value,
            'alpha': self.alpha,
            'reject_null': reject_null,
            'eta_squared': eta_squared,
            'group_means': [np.mean(group) for group in groups],
            'group_sizes': [len(group) for group in groups]
        }
        
        return result
    
    def mann_whitney_u(self, data1, data2, alternative='two-sided'):
        """Mann-Whitney U test (non-parametric)"""
        u_stat, p_value = stats.mannwhitneyu(data1, data2, alternative=alternative)
        
        reject_null = p_value < self.alpha
        
        result = {
            'test_type': 'Mann-Whitney U test',
            'null_hypothesis': 'Distributions are identical',
            'u_statistic': u_stat,
            'p_value': p_value,
            'alpha': self.alpha,
            'reject_null': reject_null,
            'sample1_median': np.median(data1),
            'sample2_median': np.median(data2)
        }
        
        return result
    
    def wilcoxon_signed_rank(self, data1, data2):
        """Wilcoxon signed-rank test (paired non-parametric)"""
        stat, p_value = stats.wilcoxon(data1, data2)
        
        reject_null = p_value < self.alpha
        
        result = {
            'test_type': 'Wilcoxon signed-rank test',
            'null_hypothesis': 'Median difference is zero',
            'statistic': stat,
            'p_value': p_value,
            'alpha': self.alpha,
            'reject_null': reject_null
        }
        
        return result
    
    def _get_alt_symbol(self, alternative):
        """Get symbol for alternative hypothesis"""
        symbols = {'two-sided': '≠', 'greater': '>', 'less': '<'}
        return symbols.get(alternative, '≠')
    
    def _get_conclusion(self, reject_null, alternative, mu0):
        """Generate conclusion text"""
        if reject_null:
            return f"Reject H₀: Evidence suggests μ {self._get_alt_symbol(alternative)} {mu0}"
        else:
            return f"Fail to reject H₀: Insufficient evidence that μ {self._get_alt_symbol(alternative)} {mu0}"
    
    def _cohens_d(self, data1, data2):
        """Calculate Cohen's d effect size"""
        n1, n2 = len(data1), len(data2)
        pooled_std = np.sqrt(((n1-1)*np.var(data1, ddof=1) + (n2-1)*np.var(data2, ddof=1)) / (n1+n2-2))
        return (np.mean(data1) - np.mean(data2)) / pooled_std
    
    def print_result(self, result):
        """Print formatted test result"""
        print(f"\n{result['test_type']}")
        print("=" * len(result['test_type']))
        print(f"H₀: {result['null_hypothesis']}")
        if 'alternative_hypothesis' in result:
            print(f"H₁: {result['alternative_hypothesis']}")
        
        # Print test statistic and p-value
        stat_name = [k for k in result.keys() if 'statistic' in k][0]
        print(f"\n{stat_name.replace('_', ' ').title()}: {result[stat_name]:.4f}")
        print(f"p-value: {result['p_value']:.4f}")
        print(f"α: {result['alpha']}")
        
        # Decision
        decision = "Reject H₀" if result['reject_null'] else "Fail to reject H₀"
        print(f"\nDecision: {decision}")
        
        if 'conclusion' in result:
            print(f"Conclusion: {result['conclusion']}")

# Example usage and demonstration
def hypothesis_testing_examples():
    """Demonstrate various hypothesis tests"""
    
    np.random.seed(42)
    tester = HypothesisTestingFramework(alpha=0.05)
    
    # Example 1: One-sample t-test
    print("Example 1: One-sample t-test")
    print("Testing if average height is 170 cm")
    heights = np.random.normal(172, 8, 50)  # True mean = 172
    result1 = tester.one_sample_t_test(heights, 170, 'two-sided')
    tester.print_result(result1)
    
    # Example 2: Two-sample t-test
    print("\n\nExample 2: Two-sample t-test")
    print("Comparing test scores between two groups")
    group_a = np.random.normal(75, 10, 30)
    group_b = np.random.normal(80, 12, 35)
    result2 = tester.two_sample_t_test(group_a, group_b, equal_var=False)
    tester.print_result(result2)
    print(f"Cohen's d (effect size): {result2['effect_size']:.3f}")
    
    # Example 3: Chi-square test
    print("\n\nExample 3: Chi-square goodness of fit")
    print("Testing if die is fair")
    observed_rolls = [18, 22, 16, 25, 12, 19]  # Rolls for faces 1-6
    expected_rolls = [20, 20, 20, 20, 20, 20]  # Expected for fair die
    result3 = tester.chi_square_test(observed_rolls, expected_rolls)
    tester.print_result(result3)
    
    # Example 4: ANOVA
    print("\n\nExample 4: One-way ANOVA")
    print("Comparing means across three groups")
    group1 = np.random.normal(20, 5, 25)
    group2 = np.random.normal(22, 5, 30)
    group3 = np.random.normal(25, 5, 28)
    result4 = tester.anova_one_way(group1, group2, group3)
    tester.print_result(result4)
    print(f"Eta-squared (effect size): {result4['eta_squared']:.3f}")

# hypothesis_testing_examples()
```