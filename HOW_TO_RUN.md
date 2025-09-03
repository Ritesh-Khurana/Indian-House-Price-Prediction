# 🚀 How to Run Your Indian Property Price Predictor

## 📋 **Quick Start Guide (With Virtual Environment)**

### 🎯 **Method 1: Super Easy - Double Click Batch File! (EASIEST)**

**Just double-click one of these files:**
- `RUN_APP_SIMPLE.bat` ← **Recommended! Most reliable**
- `RUN_APP.bat` ← Alternative version

**That's it!** The app will start automatically! 🎉

### 🎯 **Method 2: Using Anaconda Environment (Manual)**

Open PowerShell or Command Prompt and run:

```bash
# Step 1: Navigate to your project
cd "c:\Users\ritesh\New folder\house-price-predictor\streamlit_app"

# Step 2: Activate Anaconda base environment
conda activate base

# Step 3: Run your app
streamlit run indian_app.py
```

### 🎯 **Method 3: Using Anaconda Python Directly**

```bash
# Step 1: Navigate to your project
cd "c:\Users\ritesh\New folder\house-price-predictor\streamlit_app"

# Step 2: Run with full Anaconda Python path
C:\Users\ritesh\anaconda3\python.exe -m streamlit run indian_app.py
```

**Your app will open in browser at `http://localhost:8501`** 🎉

---

## 🔧 **Detailed Virtual Environment Instructions**

### **🐍 Step 1: Check Your Python Environment**
```bash
# Check if Anaconda is installed
conda --version

# Check available environments
conda env list
```

### **🌍 Step 2: Activate Your Environment**

**Option A: Using Anaconda Base Environment**
```bash
conda activate base
```

**Option B: Create a New Environment for This Project**
```bash
# Create new environment
conda create -n property-predictor python=3.9

# Activate it
conda activate property-predictor
```

### **📦 Step 3: Install Required Packages**
```bash
# Install in current environment
pip install streamlit pandas numpy plotly

# OR install from requirements.txt
pip install -r requirements.txt
```

### **🚀 Step 4: Run Your App**
```bash
# Navigate to project folder
cd "c:\Users\ritesh\New folder\house-price-predictor\streamlit_app"

# Run the app
streamlit run indian_app.py
```

### **🛑 Step 5: Stop the App**
- Press `Ctrl + C` in the terminal

### **🔄 Step 6: Deactivate Environment (when done)**
```bash
conda deactivate
```

---

## 🛠️ **Alternative Methods**

### **Method 3: Using Virtual Environment (venv)**
```bash
# Create virtual environment
python -m venv property_env

# Activate virtual environment
property_env\Scripts\activate

# Install packages
pip install -r requirements.txt

# Run app
streamlit run indian_app.py

# Deactivate when done
deactivate
```

### **Method 4: Using Anaconda Python Directly (No Activation)**
```bash
cd "c:\Users\ritesh\New folder\house-price-predictor\streamlit_app"
C:\Users\ritesh\anaconda3\python.exe -m streamlit run indian_app.py
```

### **Method 5: Specify Port (if 8501 is busy)**
```bash
conda activate base
streamlit run indian_app.py --server.port 8502
```

---

## 📦 **Installing Requirements (One-time Setup)**

If you ever move this project or set it up on a new computer:

```bash
cd "c:\Users\ritesh\New folder\house-price-predictor\streamlit_app"
pip install -r requirements.txt
```

---

## 🔍 **Troubleshooting**

### **Problem: "streamlit is not recognized"**
**Solution:** Install Streamlit
```bash
pip install streamlit
```

### **Problem: "No module named 'plotly'"**
**Solution:** Install missing packages
```bash
pip install plotly pandas numpy
```

### **Problem: Port already in use**
**Solution:** Use different port
```bash
streamlit run indian_app.py --server.port 8502
```

### **Problem: App doesn't open in browser**
**Solution:** Manually open browser and go to:
- `http://localhost:8501` OR
- `http://127.0.0.1:8501`

---

## 🎯 **Files in Your Project**

```
house-price-predictor/
├── streamlit_app/
│   ├── indian_app.py          ← Main app (RUN THIS ONE!)
│   ├── app.py                 ← Old version (don't use)
│   └── requirements.txt       ← Dependencies list
├── tutorials/
│   └── Property_Price_Predictor_Tutorial.ipynb  ← Learning guide
└── HOW_TO_RUN.md             ← This file
```

---

## ⚡ **Quick Commands Cheat Sheet**

### **🐍 Virtual Environment Commands**
| Action | Command |
|--------|---------|
| **Check Anaconda** | `conda --version` |
| **List environments** | `conda env list` |
| **Activate base env** | `conda activate base` |
| **Create new env** | `conda create -n property-predictor python=3.9` |
| **Activate new env** | `conda activate property-predictor` |
| **Deactivate env** | `conda deactivate` |

### **📱 App Commands**
| Action | Command |
|--------|---------|
| **Navigate to project** | `cd "c:\Users\ritesh\New folder\house-price-predictor\streamlit_app"` |
| **Run the app** | `streamlit run indian_app.py` |
| **Stop the app** | Press `Ctrl + C` in terminal |
| **Install packages** | `pip install -r requirements.txt` |
| **Open in browser** | Go to `http://localhost:8501` |

### **🔄 Complete Workflow**
```bash
# 1. Open PowerShell
# 2. Activate environment
conda activate base

# 3. Navigate to project
cd "c:\Users\ritesh\New folder\house-price-predictor\streamlit_app"

# 4. Run app
streamlit run indian_app.py

# 5. When done, stop app (Ctrl + C) and deactivate
conda deactivate
```

---

## 🎉 **Success!**

When everything works, you'll see:
- ✅ Terminal shows "You can now view your Streamlit app in your browser"
- ✅ Browser opens with your beautiful property price predictor
- ✅ Blue-purple gradient background with working calculators

**Enjoy your amazing property price predictor app!** 🏠✨

---

## 💡 **Pro Tips**

1. **Bookmark the URL:** Save `http://localhost:8501` in browser bookmarks
2. **Keep terminal open:** Don't close the PowerShell window while using the app
3. **Refresh browser:** If app looks weird, try refreshing the page (F5)
4. **Multiple ports:** You can run multiple apps on different ports (8501, 8502, etc.)

**Happy coding!** 🚀
