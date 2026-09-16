# SIMO Job Scraper

A Python automation script that scrapes job listings from **SIMO** (Sistema de Información del Mercado Laboral), Colombia's public employment system. It extracts structured data across multiple pages, handles dynamic content, and exports the results to an ODS/Excel file.

## Features

- **Automated navigation**: Iterates through all result pages using Selenium WebDriver.
- **Data extraction**: Captures key fields for each job listing:
  - Nivel (Level)
  - Denominación (Job Title)
  - Grado (Grade)
  - Código (Code)
  - Número OPEC (OPEC Number)
  - Asignación Salarial (Salary)
  - Convocatoria (Announcement)
  - Cierre de Inscripciones (Application Deadline)
  - Total de Vacantes (Total Vacancies)
  - Estudios (Education Requirements)
  - Experiencia (Experience Requirements)
- **Robust error handling**: Uses `try/except` blocks to avoid crashes on missing elements.
- **Dynamic content handling**: Employs `WebDriverWait` to wait for elements to be clickable.
- **Export to ODS/Excel**: Saves the scraped data into an OpenDocument Spreadsheet (`Simo.ods`) using Pandas.

## Requirements

- Python 3.7+
- Google Chrome installed
- ChromeDriver compatible with your Chrome version
- Python packages:
  - `selenium`
  - `pandas`
  - `odfpy` (for ODS export)

You can install the Python dependencies with:

```bash
pip install selenium pandas odfpy
