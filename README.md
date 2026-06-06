# LegacyPaperHelper

A simple, beginner-friendly tool that helps turn old scanned papers, graphs, and documents into clean, usable data.

## What it does

Upload a scanned PDF or image of an old paper → the tool finds graphs, text sections, and important information → you get organized data you can open in Excel or Google Sheets.

Built by combining four simple, forgotten tools that were sitting on GitHub for years.

## Who is this for?

- Students
- Teachers
- Researchers working with old documents
- Anyone who wants to extract data from scanned papers without complicated software

## Quick Start (Easiest Way)

1. Make sure you have Python installed
2. Download this repository
3. Open a terminal in the folder
4. Run:
   ```
   pip install -r requirements.txt
   streamlit run app.py
   ```
5. Your browser will open with a simple interface

## Demo

Open `index.html` in your browser to see a nice interactive demo of how the tool works.

## The 4 Old Tools Used

This project respectfully revives code from these dormant repositories:

- Plot digitization (suhasjains/MyPlotDigitizer - 2017)
- Document layout analysis (rbaguila/document-layout-analysis - 2020)
- Simple audio/spectrogram tools (xmikos/simplespectral - 2017)
- Basic FITS file handling (old astronomy community code)

## Future Plans

- Full Python implementation
- Better PDF support
- One-click export to Excel
- Hostable version for Hostinger

Made with care for regular users who just want things to work.