#  British Airways AI Analytics Dashboard

An AI-powered customer review analysis system that leverages **Machine Learning**, **Amazon Bedrock**, and **AWS Serverless Services** to analyze airline reviews, predict customer sentiment, generate intelligent recommendations, and provide interactive analytics through a modern Streamlit dashboard.

---

##  Project Overview

The British Airways AI Analytics Dashboard helps analyze customer feedback by combining traditional Machine Learning with Generative AI.

Users can enter a customer review, and the system will:

- Predict the sentiment (Positive/Negative)
- Generate AI-powered recommendations
- Analyze review aspects
- Display service ratings
- Visualize trends
- Generate downloadable reports
- Store prediction history securely on AWS

---

##  Features

- 🤖 Sentiment Analysis using Logistic Regression
- 🧠 AI-Powered Recommendations using Amazon Bedrock (Amazon Nova)
- 📊 Interactive Analytics Dashboard
- ⭐ Service Rating Visualization
- 🔍 Aspect Analysis
- 📈 Trend Dashboard
- 📄 PDF Report Generation
- ☁️ AWS Cloud Integration
- 💾 DynamoDB Storage
- ⚡ Serverless Architecture
- 🎨 Modern Streamlit User Interface

---

##  System Architecture

```
                    User
                      │
                      ▼
          Streamlit Dashboard
                      │
                      ▼
      Logistic Regression Model
                      │
         ┌────────────┴────────────┐
         │                         │
         ▼                         ▼
 Sentiment Prediction     Amazon Bedrock
                                   │
                                   ▼
                      AI Recommendation
                                   │
                                   ▼
                           API Gateway
                                   │
                                   ▼
                             AWS Lambda
                                   │
                                   ▼
                           Amazon DynamoDB
                                   │
                                   ▼
                           CloudWatch Logs
```

---

##  Technology Stack

### Programming Language
- Python

### Frontend
- Streamlit

### Machine Learning
- Scikit-learn
- Logistic Regression

### AI Services
- Amazon Bedrock
- Amazon Nova

### AWS Services
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- Amazon CloudWatch

### Data Processing
- Pandas
- NumPy

### Visualization
- Plotly
- Matplotlib

---

##  Project Structure

```
BritishAirwaysAI/
│
├── dashboard/
│   └── app.py
│
├── recommendation/
│   └── recommendation_engine.py
│
├── utils/
│   ├── aspect_analyzer.py
│   ├── aws_handler.py
│   ├── download_section.py
│   ├── header.py
│   ├── input_section.py
│   ├── pdf_report.py
│   ├── quality_score.py
│   ├── result_cards.py
│   ├── service_cards.py
│   ├── sidebar.py
│   ├── trend_analysis.py
│   └── trend_dashboard.py
│
├── dataset/
│   └── british_airways_reviews.csv
│
├── models/
│
├── lambda/
│
├── requirements.txt
│
└── README.md
```

---

##  Workflow

1. User enters a customer review.
2. Text preprocessing is performed.
3. Logistic Regression predicts sentiment.
4. Amazon Bedrock generates AI-powered recommendations.
5. Results are sent through API Gateway.
6. AWS Lambda processes the request.
7. Prediction history is stored in DynamoDB.
8. Dashboard displays:
   - Sentiment
   - AI Recommendation
   - Aspect Analysis
   - Service Ratings
   - Trend Dashboard
   - Downloadable PDF Report

---

##  Dashboard Features

### Dashboard Overview
- AI-powered analytics dashboard
- Interactive KPI cards
- Modern UI

### Sentiment Prediction
- Positive
- Negative

### AI Recommendation
- Personalized suggestions generated using Amazon Nova

### Aspect Analysis
- Service Quality
- Food
- Cabin Crew
- Seat Comfort
- Entertainment
- Value for Money

### Trend Dashboard
- Sentiment trends
- Review insights
- Interactive charts

### Report Generation
- Export analysis as PDF

---

##  AWS Services Used

### Amazon Bedrock
Generates intelligent recommendations using the Amazon Nova foundation model.

### AWS Lambda
Processes backend requests without managing servers.

### Amazon API Gateway
Provides secure REST APIs for communication between the dashboard and backend.

### Amazon DynamoDB
Stores prediction history and customer review analytics.

### Amazon S3
Stores project assets and datasets.

### Amazon CloudWatch
Monitors application performance and logs backend activities.

---

##  Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/BritishAirwaysAI.git
cd BritishAirwaysAI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure AWS

```bash
aws configure
```

Provide:

- AWS Access Key
- AWS Secret Key
- Region
- Output Format

---

##  Run the Project

```bash
streamlit run dashboard/app.py
```

---

##  Future Enhancements

- Multi-airline review analysis
- Multilingual sentiment analysis
- Deep Learning models (BERT/RoBERTa)
- Real-time review streaming
- Advanced predictive analytics
- Interactive business intelligence dashboards

---

##  Learning Outcomes

This project demonstrates:

- Machine Learning for sentiment analysis
- Generative AI using Amazon Bedrock
- Serverless computing with AWS Lambda
- REST API integration using API Gateway
- Cloud database management with DynamoDB
- Interactive dashboard development using Streamlit
- Data visualization and reporting

---

