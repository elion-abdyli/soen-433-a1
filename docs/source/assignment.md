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

```{math}
E = mc^2

y = (2)x_1 + (-1)x_2 + 3



```

```{admonition} Solution
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

## Question 4

### a)

### b)


## Question 5


