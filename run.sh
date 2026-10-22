#!/bin/bash
# Startup script for श्रीकृष्ण वाणी • Shree Krishna AI Life Counselor

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

echo "=========================================================="
echo "🦚 Starting श्रीकृष्ण वाणी • Shree Krishna AI Life Counselor"
echo "=========================================================="
echo "Open your browser at the local URL shown below (usually http://localhost:8501)"
echo "Press Ctrl+C to stop the server."
echo "=========================================================="

streamlit run app.py
