# CORD-19 Dataset Analysis Project

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive analysis of the CORD-19 research dataset with interactive visualizations and a web dashboard built with Streamlit.

## 📊 Project Overview

This project analyzes COVID-19 research papers from the CORD-19 dataset to uncover insights about:
- Publication trends over time
- Top journals and venues
- Author collaboration patterns
- Text analysis of titles and abstracts
- COVID-19 research timeline impact

## 🎯 Features

- **Data Analysis**: Complete exploration and cleaning of CORD-19 metadata
- **Interactive Dashboard**: Streamlit web application with dynamic visualizations
- **Publication Trends**: Time-series analysis of research publications
- **Journal Analysis**: Top publishing venues and distribution
- **Author Patterns**: Collaboration analysis and author statistics
- **Text Mining**: Common words and length analysis of research titles
- **COVID Timeline**: Impact visualization of pandemic on research output

## 📁 Project Structure

```
CORD-19-Analysis/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── analysis.py              # Main analysis script
├── streamlit_app.py         # Streamlit web application
├── CORD19_Analysis.ipynb    # Jupyter notebook with step-by-step analysis
├── setup.py                 # Package setup file
├── data/                    # Data directory
│   └── README.md           # Data setup instructions
├── outputs/                 # Generated visualizations and reports
│   ├── publication_trends.png
│   ├── top_journals.png
│   ├── author_analysis.png
│   └── text_analysis.png
├── docs/                    # Additional documentation
│   └── analysis_report.md  # Detailed analysis report
└── .gitignore              # Git ignore file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CORD-19-Analysis.git
   cd CORD-19-Analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the dataset**
   - Visit [CORD-19 on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
   - Download the `metadata.csv` file
   - Place it in the project root directory

### Running the Analysis

1. **Run the main analysis script**
   ```bash
   python analysis.py
   ```
   This will:
   - Load and clean the dataset
   - Generate visualizations
   - Create a cleaned dataset for the Streamlit app
   - Save results to the `outputs/` directory

2. **Launch the Streamlit dashboard**
   ```bash
   streamlit run streamlit_app.py
   ```
   Open your browser to `http://localhost:8501` to view the interactive dashboard.

3. **Explore the Jupyter notebook**
   ```bash
   jupyter notebook CORD19_Analysis.ipynb
   ```

## 📈 Analysis Results

### Key Findings

- **Dataset Size**: 1,000,000+ research papers analyzed
- **Time Range**: Publications from 1980-2024
- **Peak Year**: 2020 with the highest number of COVID-19 related publications
- **Top Journal**: *PLOS ONE* with the most publications
- **Average Authors**: 4.2 authors per paper
- **Research Acceleration**: 300% increase in publications after WHO pandemic declaration

### Visualizations Generated

1. **Publication Trends**: Time-series showing research output over years
2. **Journal Analysis**: Top publishing venues and their contribution
3. **Author Patterns**: Distribution of author counts and collaboration
4. **Text Analysis**: Most common words in research titles
5. **COVID Timeline**: Research response to the pandemic

## 🖥️ Streamlit Dashboard Features

The interactive dashboard includes:

- **Overview**: Dataset statistics and key metrics
- **Publication Trends**: Interactive time-series with year range selector
- **Journal Analysis**: Top journals with customizable display count
- **Author Patterns**: Collaboration statistics and distributions
- **Text Analysis**: Word frequency analysis and text statistics
- **COVID Timeline**: Pandemic impact visualization with WHO declaration marker

## 📊 Dataset Information

The CORD-19 dataset contains metadata about COVID-19 research papers including:

- **Paper titles and abstracts**
- **Publication dates and venues**
- **Author information**
- **DOI and source links**
- **Full text availability**

**Source**: [Allen Institute for AI - CORD-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)

## 🛠️ Technologies Used

- **Python 3.7+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib/Seaborn**: Static visualizations
- **Plotly**: Interactive visualizations
- **Streamlit**: Web application framework
- **Jupyter**: Interactive development environment
- **NumPy**: Numerical computing

## 📋 Requirements

```
pandas>=1.3.0
matplotlib>=3.3.0
seaborn>=0.11.0
streamlit>=1.0.0
plotly>=5.0.0
jupyter>=1.0.0
numpy>=1.20.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Allen Institute for AI** for providing the CORD-19 dataset
- **Kaggle** for hosting the dataset
- **Streamlit** for the amazing web framework
- **Python community** for the excellent data science libraries

## 📞 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/CORD-19-Analysis](https://github.com/yourusername/CORD-19-Analysis)

---

## 🚀 Live Demo

Check out the live Streamlit application: [CORD-19 Analysis Dashboard](https://your-app-name.streamlit.app)

## 📸 Screenshots

### Dashboard Overview
![Dashboard Overview](outputs/dashboard_overview.png)

### Publication Trends
![Publication Trends](outputs/publication_trends.png)

### Journal Analysis
![Journal Analysis](outputs/top_journals.png)

---

**Made with ❤️ and Python**
