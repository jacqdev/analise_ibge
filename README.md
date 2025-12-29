# 📊 Análise IBGE

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/jacqdev/analise_ibge)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-success)](https://analise-ibge.streamlit.app)

Projeto em Python para análise de dados simulados do IBGE, com:
- Dashboard interativo em **Streamlit**
- Testes automatizados com **Pytest**
- Cobertura total de código (**100%**)

---

## 🚀 Como rodar localmente

```bash
git clone https://github.com/jacqdev/analise_ibge.git
cd analise_ibge
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
streamlit run src/dashboard.py
