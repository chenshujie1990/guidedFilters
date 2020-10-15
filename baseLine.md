# 导向滤波器求解推导

## 局部线性模型

### 问题描述

* 给定两组观察值$x_1,x_2,\dotsb,x_n$与$y_1,y_2,\dotsb,y_n$

* 两组值之间存在近似线性关系$\hat{y}_i=ax_i+b$

求系数$a$和$b$的解析表达式

此时可以构建损失函数为$L(a,b)=\dfrac{1}{n}\displaystyle\sum_{i=1}^n(ax_i+b-y_i)^2$