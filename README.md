# Gauss (高斯数学算法实现)

本项目致力于使用 Python 语言复现高斯（Carl Friedrich Gauss）在数学、数论及统计学领域的经典算法。通过现代编程手段，探索古典数学之美，并为科学计算提供参考实现。

## 🚀 项目特点

- **纯 Python 实现**：仅依赖 Python 标准库或科学计算库（如 NumPy）。
- **算法覆盖**：涵盖高斯消元法、高斯-赛德尔迭代、正态分布计算等。
- **跨平台支持**：支持 macOS、Windows 11 及 Ubuntu 环境。

## 📚 已实现的算法

### 1. 线性代数
- **高斯消元法 (Gaussian Elimination)**：求解线性方程组的基础算法。
- **高斯-赛德尔迭代法 (Gauss-Seidel Method)**：用于数值求解大型线性方程组。

### 2. 数论
- **高斯圆问题 (Gauss Circle Problem)**：计算圆内格点数目。
- **二次剩余 (Quadratic Reciprocity)**：高斯引理的相关实现。

### 3. 统计与概率
- **高斯分布 (Gaussian Distribution)**：正态分布的概率密度函数及累积分布函数实现。

## 🛠️ 环境准备

建议使用 Python 3.8+ 环境。

```bash
# 克隆仓库
git clone [https://github.com/lzyq/Gauss.git](https://github.com/lzyq/Gauss.git)
cd Gauss

# 创建并激活虚拟环境 (可选)
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate  # Windows