# assignment 1

## Question 1

### a)

The model could learn and use features that would be unethical for the purpuse of profiling individuals.
The encryption would essentially be a way to remove those those features from the predictive signals.

### b)

Expert systems could be used because we can use the domain of actuarial science or socio-economic expertise and research to draw conclusions from known research and dataset on hand without performing learning tasks.

### c)

A possible regresion task could be to estimate the present value of a customer viewed as a financial asset of the bank.

### d)

A possible classification task would be the probability of a customer defaulting on a loan.

### e)

A possible unsupervised learning task would would be performing anomaly detection via clustering models.

### f)
A typical split would be 70:15:15 for training, validation and testing respectively.
The training set serves for performing the core learning algorithm of fitting a model to data.
The validation set can be used for tuning, model selection, and indication of overfitting or underfitting.
The test set is used to simulate as close as possible deployment behavior and performance out of sample.

### g)
In a situation where there high ammounts of sequential data we intend to perform predictions on, deep learning would be better suited for the task. LSTM, RNN, and Transformers models typically perform best on sequential prediction tasks, and they have good scaling capabilities for massive datasets, and can handle massive and complex feature sets through embedding capabilities.




## Question 2

### a)
Activation functions supply the non-linearity required to obtain a universal approximator. Without this all neural network would reduce to a linear transformation.
In the task of fitting manifolds to data, activation functions serve to warp the manifold by way of its non linearities.

### b)
Relu is simple to evaluate, differente, and it computes efficiently. However, it has limited representationnal capacity not only because it is piecewise linear but also because both the activation and gradient can vanish for negative values. This increases the likelyhood of dead neurons, which lose all signal during backpropagation and cannot recover through training.

Leaky relu, however maintains a faint but present gradient signal in the negative domain. The activation in the negative domain is also negative, increasing the representationnal capacity. This enables the interpretation of negative signals, which makes the network more robust by capturing a broader domain of signals. More importantly the gradient, instead of collapsing to zero unrecoverably during training, can instead preserve a faint signal, which can later be further updated or recover during exposure to further data. 
## Question 3

### a)


**Model:**

ŷ = w1·x1 + w2·x2 + w0  

Parameters: w1 = 2, w2 = -1, w0 = 3

---

**Samples:**

| Sample | x1 | x2 | True y |
|--------|----|----|---------|
| 1      | 1  | 2  | 4       |
| 2      | 2  | 1  | 3       |
| 3      | 0  | 3  | 1       |

---

**Step 1: Predictions**

- ŷ1 = 2(1) + (-1)(2) + 3 = 3  
- ŷ2 = 2(2) + (-1)(1) + 3 = 6  
- ŷ3 = 2(0) + (-1)(3) + 3 = 0  

---

**Step 2: Squared Errors**

- (ŷ1 - y1)² = (3 - 4)² = 1  
- (ŷ2 - y2)² = (6 - 3)² = 9  
- (ŷ3 - y3)² = (0 - 1)² = 1  

---

**Step 3: Mean Squared Error**

MSE = (1 + 9 + 1) / 3 = 11/3 ≈ 3.67  

---

**Final Answer:**  
MSE = 11/3 ≈ 3.67


### b)

**Initial weights:**  
w1 = 2, w2 = -1, w0 = 3  
Learning rate: η = 0.1  

---

**Sample 1: (x1=1, x2=2, y=4)**  
ŷ = 3, error = -1  
∂w1 = -1, ∂w2 = -2, ∂w0 = -1  
Updated: w1 = 2.1, w2 = -0.8, w0 = 3.1  

---

**Sample 2: (x1=2, x2=1, y=3)**  
ŷ = 6.5, error = 3.5  
∂w1 = 7, ∂w2 = 3.5, ∂w0 = 3.5  
Updated: w1 = 1.4, w2 = -1.15, w0 = 2.75  

---

**Sample 3: (x1=0, x2=3, y=1)**  
ŷ = -0.7, error = -1.7  
∂w1 = 0, ∂w2 = -5.1, ∂w0 = -1.7  
Updated: w1 = 1.4, w2 = -0.64, w0 = 2.92  

---

**Final weights after one epoch:**  
w1 = 1.4, w2 = -0.64, w0 = 2.92  


## Question 4

**Question 4(a): Categorical Cross-Entropy Loss**

Formula:  
Loss = - (1/N) Σ log(p_correct_class)

where p_correct_class = predicted probability for the true label.

---

**Sample 1** (True = Positive, p = 0.70)  
Loss₁ = -log(0.70) ≈ 0.357  

**Sample 2** (True = Negative, p = 0.80)  
Loss₂ = -log(0.80) ≈ 0.223  

**Sample 3** (True = Neutral, p = 0.30)  
Loss₃ = -log(0.30) ≈ 1.204  

**Sample 4** (True = Positive, p = 0.60)  
Loss₄ = -log(0.60) ≈ 0.511  

**Sample 5** (True = Neutral, p = 0.50)  
Loss₅ = -log(0.50) ≈ 0.693  

---

**Total Loss** = (0.357 + 0.223 + 1.204 + 0.511 + 0.693) / 5  
= 2.988 / 5  
= 0.598  

**Final Answer (a):** Average Cross-Entropy Loss ≈ **0.598**

---

**Question 4(b): Classification Accuracy**

Rule: pick the class with the highest predicted probability.

- Sample 1: [0.70, 0.20, 0.10] → Predict Positive → Correct ✅  
- Sample 2: [0.10, 0.80, 0.10] → Predict Negative → Correct ✅  
- Sample 3: [0.30, 0.40, 0.30] → Predict Negative → True = Neutral → Incorrect ❌  
- Sample 4: [0.60, 0.25, 0.15] → Predict Positive → Correct ✅  
- Sample 5: [0.20, 0.30, 0.50] → Predict Neutral → Correct ✅  

Correct = 4 out of 5  

Accuracy = 4/5 = 0.8 = **80%**

---

**Final Answer (b):** Classification Accuracy = **80%**


### a)

### b)


## Question 5


