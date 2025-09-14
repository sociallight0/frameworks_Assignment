#!/usr/bin/env python3
"""
CORD-19 Project Setup Script
============================

This script helps set up the CORD-19 analysis project structure and 
checks for required dependencies.

Usage: python setup_project.py
"""

import os
import sys
import subprocess
import urllib.request
import json
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"   Current version: {sys.version}")
        return False
    else:
        print(f"✅ Python version: {sys.version.split()[0]}")
        return True

def create_directory_structure():
    """Create the project directory structure."""
    print("\n📁 Creating directory structure...")
    
    directories = [
        'data',
        'outputs',
        'docs',
        '.streamlit'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"   Created: {directory}/")
    
    # Create Streamlit config
    streamlit_config = """
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"

[server]
headless = true
port = 8501
"""
    
    with open('.streamlit/config.toml', 'w') as f:
        f.write(streamlit_config.strip())
    print("   Created: .streamlit/config.toml")

def check_dependencies():
    """Check if required packages are installed."""
    print("\n📦 Checking dependencies...")
    
    required_packages = [
        'pandas',
        'numpy', 
        'matplotlib',
        'seaborn',
        'plotly',
        'streamlit'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} (missing)")
            missing_packages.append(package)
    
    return missing_packages

def install_dependencies(missing_packages):
    """Install missing dependencies."""
    if not missing_packages:
        return True
    
    print(f"\n🔧 Installing missing packages: {', '.join(missing_packages)}")
    
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '--upgrade'
        ] + missing_packages)
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please install manually:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False

def create_sample_data():
    """Create a sample dataset if the main file doesn't exist."""
    if os.path.exists('metadata.csv'):
        print("\n✅ metadata.csv found")
        return True
    
    print("\n📊 metadata.csv not found. Creating sample data...")
    
    # Create a small sample dataset for testing
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
    
    # Generate sample data
    np.random.seed(42)
    n_samples = 1000
    
    # Sample titles and abstracts
    sample_titles = [
        "COVID-19 transmission dynamics in healthcare settings",
        "SARS-CoV-2 vaccine efficacy and safety analysis",
        "Impact of pandemic on mental health outcomes",
        "Respiratory symptoms in coronavirus patients",
        "Public health measures during COVID-19 outbreak",
        "Clinical characteristics of severe COVID-19 cases",
        "Epidemiological investigation of coronavirus spread",
        "Treatment protocols for COVID-19 patients",
        "Long-term effects of SARS-CoV-2 infection",
        "Prevention strategies for pandemic control"
    ]
    
    sample_abstracts = [
        "This study investigates the transmission patterns of COVID-19 in various healthcare settings and provides recommendations for infection control.",
        "We analyzed vaccine efficacy data from multiple clinical trials to assess the safety and effectiveness of COVID-19 vaccines.",
        "The pandemic has significantly impacted mental health worldwide. This research examines the psychological effects and coping strategies.",
        "Clinical analysis of respiratory symptoms in COVID-19 patients, including severity assessment and treatment outcomes.",
        "Evaluation of public health interventions implemented during the COVID-19 pandemic and their effectiveness in controlling spread."
    ]
    
    sample_journals = [
        "PLOS ONE", "Nature Communications", "The Lancet", "NEJM", "Science",
        "medRxiv", "bioRxiv", "Scientific Reports", "BMC Medicine", "Cell"
    ]
    
    # Generate sample data
    data = {
        'cord_uid': [f'cord_{i:06d}' for i in range(n_samples)],
        'title': np.random.choice(sample_titles, n_samples),
        'abstract': np.random.choice(sample_abstracts, n_samples),
        'authors': [f'Author{i%5+1}; Author{(i+1)%5+1}; Author{(i+2)%5+1}' for i in range(n_samples)],
        'journal': np.random.choice(sample_journals, n_samples),
        'publish_time': pd.date_range(start='2018-01-01', end='2023-12-31', periods=n_samples)
    }
    
    df = pd.DataFrame(data)
    df.to_csv('metadata_sample.csv', index=False)
    
    print("   Created metadata_sample.csv with 1,000 sample records")
    print("   💡 For full analysis, download the complete dataset from:")
    print("      https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge")
    print("   📝 See data/README.md for detailed instructions")
    
    return True

def create_readme_files():
    """Create additional README files."""
    print("\n📝 Creating documentation files...")
    
    # Data README
    data_readme = """# Data Directory

This directory should contain the CORD-19 dataset files.

## Required Files

- `metadata.csv` - Main dataset file (download from Kaggle)

## Download Instructions

1. Visit [CORD-19 on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
2. Create a free Kaggle account if needed
3. Download the `metadata.csv` file
4. Place it in this directory

## Alternative: Sample Data

If you want to test the analysis with sample data:
- Run `python setup_project.py` to generate `metadata_sample.csv`
- Update file paths in analysis scripts to use the sample file

## File Sizes

- Full dataset: ~200-300 MB
- Sample dataset: ~100 KB
- Memory usage when loaded: ~1-2 GB for full dataset
"""
    
    with open('data/README.md', 'w') as f:
        f.write(data_readme.strip())
    
    # Outputs README
    outputs_readme = """# Outputs Directory

This directory contains generated visualizations and analysis results.

## Generated Files

After running the analysis, you'll find:

- `publication_trends.png` - Publication trends over time
- `top_journals.png` - Top publishing journals
- `author_analysis.png` - Author collaboration patterns
- `text_analysis.png` - Text analysis visualizations
- `cleaned_data.csv` - Processed dataset for Streamlit
- `analysis_summary.json` - Summary statistics

## File Management

- Files are automatically generated by `analysis.py`
- Safe to delete - will be regenerated on next run
- Add to `.gitignore` to avoid committing large files
"""
    
    with open('outputs/README.md', 'w') as f:
        f.write(outputs_readme.strip())
    
    print("   Created: data/README.md")
    print("   Created: outputs/README.md")

def run_basic_tests():
    """Run basic tests to ensure everything works."""
    print("\n🧪 Running basic tests...")
    
    try:
        # Test pandas
        import pandas as pd
        test_df = pd.DataFrame({'test': [1, 2, 3]})
        assert len(test_df) == 3
        print("   ✅ Pandas working")
        
        # Test matplotlib
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        plt.close(fig)
        print("   ✅ Matplotlib working")
        
        # Test streamlit
        import streamlit
        print("   ✅ Streamlit working")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Test failed: {e}")
        return False

def create_launch_script():
    """Create convenience scripts for launching the application."""
    print("\n🚀 Creating launch scripts...")
    
    # Windows batch file
    batch_script = """@echo off
echo Starting CORD-19 Analysis Dashboard...
echo.
echo Make sure you have the metadata.csv file in the project directory!
echo.
streamlit run streamlit_app.py
pause
"""
    
    with open('run_dashboard.bat', 'w') as f:
        f.write(batch_script)
    
    # Unix shell script
    shell_script = """#!/bin/bash
echo "Starting CORD-19 Analysis Dashboard..."
echo ""
echo "Make sure you have the metadata.csv file in the project directory!"
echo ""
streamlit run streamlit_app.py
"""
    
    with open('run_dashboard.sh', 'w') as f:
        f.write(shell_script)
    
    # Make shell script executable on Unix systems
    try:
        os.chmod('run_dashboard.sh', 0o755)
    except:
        pass
    
    print("   Created: run_dashboard.bat (Windows)")
    print("   Created: run_dashboard.sh (Unix/Linux/Mac)")

def create_license():
    """Create MIT license file."""
    license_text = """MIT License

Copyright (c) 2024 CORD-19 Analysis Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    
    with open('LICENSE', 'w') as f:
        f.write(license_text)
    
    print("   Created: LICENSE")

def main():
    """Main setup function."""
    print("🦠 CORD-19 Analysis Project Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Create directory structure
    create_directory_structure()
    
    # Check and install dependencies
    missing = check_dependencies()
    if missing:
        install = input(f"\nInstall missing packages? (y/n): ").lower().strip()
        if install == 'y':
            if not install_dependencies(missing):
                return False
        else:
            print("⚠️  Please install missing packages manually before proceeding.")
            return False
    
    # Create sample data if needed
    create_sample_data()
    
    # Create documentation
    create_readme_files()
    
    # Create launch scripts
    create_launch_script()
    
    # Create license
    create_license()
    
    # Run tests
    if not run_basic_tests():
        print("⚠️  Some tests failed. Check your installation.")
        return False
    
    print("\n🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("1. Download metadata.csv from Kaggle (see data/README.md)")
    print("2. Run analysis: python analysis.py")
    print("3. Launch dashboard: streamlit run streamlit_app.py")
    print("   Or use: python run_dashboard.sh / run_dashboard.bat")
    print("\n📚 Project structure:")
    print("├── analysis.py              # Main analysis script")
    print("├── streamlit_app.py         # Web dashboard")  
    print("├── CORD19_Analysis_Notebook.py  # Jupyter notebook")
    print("├── requirements.txt         # Dependencies")
    print("├── README.md               # Project documentation")
    print("├── data/                   # Dataset directory")
    print("├── outputs/                # Generated files")
    print("└── docs/                   # Additional documentation")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
