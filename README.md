# 📰 Fake News Detection with AI

## 🎥 Demo Time
Experience the project in action:  
[🔗 Watch the Demo](https://youtu.be/CPYNyuilGCQ)

## 🚀 Overview
In a world where **70% of Americans encounter fake news every day** on social media (source: D. Georgiev, 2024), distinguishing between fake and real news is crucial. This project delivers a **trusted and accurate Machine Learning solution** to identify fake news with ease and reliability. 🎯

## 🎯 Business Problem
The **Head of Innovation** at leading social media platforms like Meta, Snapchat, TikTok, and X (formerly Twitter) is seeking solutions to combat the proliferation of fake news. This project aims to answer the critical question:

**"How can we know if an article is fake or real?"**

## 📊 Data Source
We leveraged publicly accessible data from Kaggle:  
[Fake News Classification Dataset](https://www.kaggle.com/datasets/aadyasingh55/fake-news-classification/data)

## 🧠 Solution Architecture
### 🏋️‍♂️ Trained Models
1. **Multinomial Naive Bayes with Count Vectorizer**  
   - Configurations:  
     - Alpha = 0.001  
     - Alpha = 0.01  
     - Alpha = 0.1  
2. **Multinomial Naive Bayes with TF-IDF Vectorizer**  
   - Configurations:  
     - Alpha = 0.001  
     - Alpha = 0.01  
     - Alpha = 0.1  

### 🏆 Final Model Selection
- **Chosen Model:** Multinomial Naive Bayes with Count Vectorizer (Alpha = 0.001)
- **Why?**
  - Superior performance across metrics: **Accuracy**, **Cohen’s Kappa**, and **Matthew’s Correlation Coefficient**  
  - Balanced **Precision** and **Recall** ensuring consistency  
  - Robust stability across alpha variations  

## 🔧 Deployment Workflow
1. **User Input**  
   - News article provided by the user.  
2. **Cleaning, Preprocessing, and Tokenization**  
   - Ensures text is structured for model processing.  
3. **ML Model**  
   - Model stored as a **Pickle file** for efficient use.  
4. **Frontend Interface**  
   - Built with **Streamlit** for seamless interaction.  

## 🛠️ Tech Stack
- **Python**: Core programming language.  
- **Streamlit**: Frontend for deployment.
- **NLP methods**: For understanding natural language.
- **Scikit-learn**: ML model training and evaluation.
- **AI reinforcement**: For powering to the moon our model. 
- **Pandas** and **NumPy**: Data manipulation and preprocessing.

## 🤝 Contributing
Feel free to fork this project, submit issues, or make pull requests. Let's fight fake news together! 💪

## 📞 Contact
For questions or collaboration opportunities:  
**Email:** [tobiaspariente6@gmail.com](mailto:tobiaspariente6@gmail.com)  
**LinkedIn:** [My Profile](https://www.linkedin.com/in/tobiaspariente/)

## 🙏 Acknowledgments
Thanks to **Kaggle** & **Flatiron School** for the dataset and the ever-growing community of Machine Learning enthusiasts for inspiration and support.

## ✨ Future Improvements
- Expand the dataset for better generalization.  
- Implement additional models (e.g., transformers like BERT).  
- Optimize frontend for enhanced usability.
