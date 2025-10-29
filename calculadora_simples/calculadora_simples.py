import tkinter as tk
from tkinter import ttk, font
import locale
import os
import sys
from PIL import Image, ImageTk

# --- Função para resolver o caminho dos recursos ---
def resource_path(relative_path):
    """ Obtém o caminho absoluto para o recurso, funciona para dev e para o PyInstaller """
    try:
        # PyInstaller cria uma pasta temp e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# --- Classe para Seções Recolhíveis ---
class CollapsibleFrame(ttk.Frame):
    """Um frame que pode ser recolhido/expandido."""
    def __init__(self, parent, text="", expanded_by_default=False, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.text = text
        self.is_expanded = tk.BooleanVar(value=expanded_by_default)

        self.title_frame = ttk.Frame(self)
        self.title_frame.pack(fill="x", expand=True)

        self.toggle_button = ttk.Label(self.title_frame, style="Header.TLabel")
        self.toggle_button.pack(side="left")

        self.title_label = ttk.Label(self.title_frame, text=self.text, style="Header.TLabel")
        self.title_label.pack(side="left", fill="x", expand=True)

        self.content_frame = ttk.Frame(self)

        self.toggle_button.bind("<Button-1>", self.toggle)
        self.title_label.bind("<Button-1>", self.toggle)
        
        if not self.is_expanded.get():
            self.content_frame.pack_forget()
            self.toggle_button.configure(text="► ")
        else:
            self.content_frame.pack(fill="x", expand=True)
            self.toggle_button.configure(text="▼ ")

    def toggle(self, event=None):
        if self.is_expanded.get():
            self.content_frame.pack_forget()
            self.toggle_button.configure(text="► ")
            self.is_expanded.set(False)
        else:
            self.content_frame.pack(fill="x", expand=True)
            self.toggle_button.configure(text="▼ ")
            self.is_expanded.set(True)

# --- Classe para criar Tooltips ---
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip_window, text=self.text, justify='left',
                         background="#FFFFE0", relief='solid', borderwidth=1,
                         font=("Segoe UI", 9, "normal"))
        label.pack(ipadx=5, ipady=3)

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
        self.tooltip_window = None

# --- Funções Auxiliares ---
def format_currency(value):
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(value, grouping=True, symbol=True)
    except (locale.Error, TypeError):
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def limpar_campos():
    """Limpa os campos de entrada e esconde a área de resultados."""
    entry_faturamento.delete(0, tk.END)
    combo_area.set("")
    for widget in result_frame.winfo_children():
        widget.destroy()
    result_frame.pack_forget()
    for anexo_id in anexos:
        if trees[anexo_id].selection():
            trees[anexo_id].selection_remove(trees[anexo_id].selection())
        if collapsible_frames[anexo_id].is_expanded.get():
            collapsible_frames[anexo_id].toggle()

def analisar_faturamento():
    """Mostra a área de resultados e preenche com a análise."""
    for widget in result_frame.winfo_children():
        widget.destroy()
    result_frame.pack(pady=10)
    
    for anexo_id in anexos:
        if trees[anexo_id].selection():
            trees[anexo_id].selection_remove(trees[anexo_id].selection())

    try:
        faturamento_str = entry_faturamento.get().replace("R$", "").strip().replace(".", "").replace(",", ".")
        area_selecionada = combo_area.get()

        if not faturamento_str or not area_selecionada:
            ttk.Label(result_frame, text="Por favor, preencha todos os campos.", foreground="#E8A900", style="BoldResult.TLabel").pack()
            return
        
        faturamento_anual = float(faturamento_str)
        anexo_id_alvo = areas_de_atuacao[area_selecionada]

        enquadramento = None
        target_faixa_index = -1

        dados = anexos[anexo_id_alvo]
        for i, faixa in enumerate(dados["faixas"]):
            if faixa["min"] < faturamento_anual <= faixa["max"]:
                enquadramento = {
                    "Anexo": f'{anexo_id_alvo} - {dados["nome"]}',
                    "Faixa": faixa['faixa'],
                    "Alíquota": f'{faixa["aliquota"]}%',
                    "Dedução": format_currency(faixa['deducao'])
                }
                target_faixa_index = i
                break

        if not enquadramento and faturamento_anual <= 180000:
             enquadramento = {"info": f"Empresa na 1ª faixa do {anexo_id_alvo}."}

        if enquadramento:
            color = "#4CAF50"
            ttk.Label(result_frame, text="Enquadramento Encontrado:", style="BoldHeader.TLabel").pack(pady=(0,5))
            if "info" in enquadramento:
                ttk.Label(result_frame, text=enquadramento['info'], foreground=color, style="BoldResult.TLabel").pack()
            else:
                for key, value in enquadramento.items():
                    ttk.Label(result_frame, text=f"{key}: {value}", foreground=color, style="BoldResult.TLabel").pack()
                if target_faixa_index != -1:
                    collapsible = collapsible_frames[anexo_id_alvo]
                    if not collapsible.is_expanded.get():
                        collapsible.toggle()
                    
                    target_tree = trees[anexo_id_alvo]
                    item_id = target_tree.get_children()[target_faixa_index]
                    target_tree.selection_set(item_id)
                    target_tree.focus(item_id)
                    canvas.after(100, lambda: canvas.yview_moveto(collapsible.winfo_y() / scrollable_frame.winfo_height()))

        else:
            ttk.Label(result_frame, text="Faturamento acima do teto do Simples Nacional.", foreground="#D22B2B", style="BoldResult.TLabel").pack()

    except ValueError:
        ttk.Label(result_frame, text="Erro: Digite um número válido.", foreground="red", style="BoldResult.TLabel").pack()

# --- Dados do Simples Nacional ---
anexos = {
    "Anexo I": {"nome": "Comércio", "descricao": "Venda de mercadorias.", "faixas": [{"faixa": "1ª", "min": 0, "max": 180000, "aliquota": 4.0, "deducao": 0}, {"faixa": "2ª", "min": 180000.01, "max": 360000, "aliquota": 7.3, "deducao": 5940}, {"faixa": "3ª", "min": 360000.01, "max": 720000, "aliquota": 9.5, "deducao": 13860}, {"faixa": "4ª", "min": 720000.01, "max": 1800000, "aliquota": 10.7, "deducao": 22500}, {"faixa": "5ª", "min": 1800000.01, "max": 3600000, "aliquota": 14.3, "deducao": 87300}, {"faixa": "6ª", "min": 3600000.01, "max": 4800000, "aliquota": 19.0, "deducao": 378000}]},
    "Anexo II": {"nome": "Indústria", "descricao": "Produção e manufatura.", "faixas": [{"faixa": "1ª", "min": 0, "max": 180000, "aliquota": 4.5, "deducao": 0}, {"faixa": "2ª", "min": 180000.01, "max": 360000, "aliquota": 7.8, "deducao": 5940}, {"faixa": "3ª", "min": 360000.01, "max": 720000, "aliquota": 10.0, "deducao": 13860}, {"faixa": "4ª", "min": 720000.01, "max": 1800000, "aliquota": 11.2, "deducao": 22500}, {"faixa": "5ª", "min": 1800000.01, "max": 3600000, "aliquota": 14.7, "deducao": 85500}, {"faixa": "6ª", "min": 3600000.01, "max": 4800000, "aliquota": 30.0, "deducao": 720000}]},
    "Anexo III": {"nome": "Serviços (fator r < 28%)", "descricao": "Instalação, reparos, contabilidade, academias, etc.", "faixas": [{"faixa": "1ª", "min": 0, "max": 180000, "aliquota": 6.0, "deducao": 0}, {"faixa": "2ª", "min": 180000.01, "max": 360000, "aliquota": 11.2, "deducao": 9360}, {"faixa": "3ª", "min": 360000.01, "max": 720000, "aliquota": 13.5, "deducao": 17640}, {"faixa": "4ª", "min": 720000.01, "max": 1800000, "aliquota": 16.0, "deducao": 35640}, {"faixa": "5ª", "min": 1800000.01, "max": 3600000, "aliquota": 21.0, "deducao": 125640}, {"faixa": "6ª", "min": 3600000.01, "max": 4800000, "aliquota": 33.0, "deducao": 648000}]},
    "Anexo IV": {"nome": "Serviços (sem CPP no DAS)", "descricao": "Limpeza, vigilância, obras, advocacia.", "faixas": [{"faixa": "1ª", "min": 0, "max": 180000, "aliquota": 4.5, "deducao": 0}, {"faixa": "2ª", "min": 180000.01, "max": 360000, "aliquota": 9.0, "deducao": 8100}, {"faixa": "3ª", "min": 360000.01, "max": 720000, "aliquota": 10.2, "deducao": 12420}, {"faixa": "4ª", "min": 720000.01, "max": 1800000, "aliquota": 14.0, "deducao": 39780}, {"faixa": "5ª", "min": 1800000.01, "max": 3600000, "aliquota": 22.0, "deducao": 183780}, {"faixa": "6ª", "min": 3600000.01, "max": 4800000, "aliquota": 33.0, "deducao": 828000}]},
    "Anexo V": {"nome": "Serviços (fator r >= 28%)", "descricao": "Auditoria, jornalismo, tecnologia, engenharia, etc.", "faixas": [{"faixa": "1ª", "min": 0, "max": 180000, "aliquota": 15.5, "deducao": 0}, {"faixa": "2ª", "min": 180000.01, "max": 360000, "aliquota": 18.0, "deducao": 4500}, {"faixa": "3ª", "min": 360000.01, "max": 720000, "aliquota": 19.5, "deducao": 9900}, {"faixa": "4ª", "min": 720000.01, "max": 1800000, "aliquota": 20.5, "deducao": 17100}, {"faixa": "5ª", "min": 1800000.01, "max": 3600000, "aliquota": 23.0, "deducao": 62100}, {"faixa": "6ª", "min": 3600000.01, "max": 4800000, "aliquota": 30.5, "deducao": 540000}]}
}

areas_de_atuacao = {
    "Comércio em Geral (Lojas, e-commerce)": "Anexo I",
    "Indústria e Fábricas em Geral": "Anexo II",
    "Serviços (Reparos, Academias, Agências de Viagem, Contabilidade)": "Anexo III",
    "Serviços (Limpeza, Vigilância, Obras, Advocacia)": "Anexo IV",
    "Serviços (Tecnologia, Auditoria, Engenharia, Publicidade)": "Anexo V"
}

# --- Configuração da Interface Gráfica ---
app = tk.Tk()
app.title("Calculadora Simples Nacional")
app.geometry("950x750")
app.configure(bg="#2c2c2c")

# --- Estilos ---
style = ttk.Style()
style.theme_use('clam')
style.configure("TFrame", background="#2c2c2c")
style.configure("TLabel", background="#2c2c2c", foreground="#FFFFFF", font=("Segoe UI", 10))
style.configure("Title.TLabel", font=("Segoe UI", 18, "bold"))
style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))
style.configure("BoldHeader.TLabel", font=("Segoe UI", 12, "bold"), foreground="#FFFFFF")
style.configure("Result.TLabel", font=("Segoe UI", 11))
style.configure("BoldResult.TLabel", font=("Segoe UI", 11, "bold"))
style.configure("TButton", background="#0078D7", foreground="#FFFFFF", font=("Segoe UI", 10, "bold"), borderwidth=0)
style.map("TButton", background=[('active', '#005A9E')])
style.configure("Secondary.TButton", background="#6c757d", foreground="#FFFFFF")
style.map("Secondary.TButton", background=[('active', '#5a6268')])
style.configure("Treeview", rowheight=28, fieldbackground="#3c3c3c", background="#3c3c3c", foreground="#FFFFFF", font=("Segoe UI", 10))
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#4a4a4a", foreground="#FFFFFF")
style.map("Treeview", background=[('selected', '#0078D7')])

# --- Layout Principal com Scroll e Centralização ---

# Coluna central se expande, as laterais não
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

canvas = tk.Canvas(app, bg="#2c2c2c", highlightthickness=0)
scrollbar = ttk.Scrollbar(app, orient="vertical", command=canvas.yview)

# Frame rolável que conterá todo o conteúdo
scrollable_frame = ttk.Frame(canvas, style="TFrame")
scrollable_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="n")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_configure(event):
    canvas.itemconfig(scrollable_window, width=event.width)

scrollable_frame.bind("<Configure>", on_frame_configure)
canvas.bind("<Configure>", on_canvas_configure)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# --- Seção do Cabeçalho (Logo) ---
header_frame = ttk.Frame(scrollable_frame)
header_frame.pack(pady=(20, 10))

try:
    logo_path = resource_path("SisPeC-negativo.png")
    img = Image.open(logo_path)
    img.thumbnail((250, 250))
    logo = ImageTk.PhotoImage(img)
    logo_label = ttk.Label(header_frame, image=logo, background="#2c2c2c")
    logo_label.pack()
except FileNotFoundError:
    print(f"Arquivo de imagem não encontrado em: {logo_path}")
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

# --- Seção da Calculadora ---
calc_frame = ttk.Frame(scrollable_frame)
calc_frame.pack(pady=10)

ttk.Label(calc_frame, text="Calculadora de Enquadramento do Simples Nacional", style="Title.TLabel").pack(pady=(0, 20))
ttk.Label(calc_frame, text="Digite o faturamento anual da empresa:", style="TLabel").pack()
entry_faturamento = ttk.Entry(calc_frame, font=("Segoe UI", 12), width=30, justify='center')
entry_faturamento.pack(pady=5)

ttk.Label(calc_frame, text="Selecione a área de atuação:", style="TLabel").pack(pady=(10, 0))
combo_area = ttk.Combobox(calc_frame, values=list(areas_de_atuacao.keys()), font=("Segoe UI", 10), width=50, justify='center')
combo_area.pack(pady=5)

buttons_frame = ttk.Frame(calc_frame)
buttons_frame.pack(pady=10)

analisar_button = ttk.Button(buttons_frame, text="Analisar Faturamento", command=analisar_faturamento, style="TButton", padding=10)
analisar_button.pack(side="left", padx=5)

limpar_button = ttk.Button(buttons_frame, text="Limpar", command=limpar_campos, style="Secondary.TButton", padding=10)
limpar_button.pack(side="left", padx=5)

result_frame = ttk.Frame(calc_frame)
result_frame.pack(pady=10)
result_frame.pack_forget() # Começa escondido

# --- Dicionários para guardar widgets ---
trees = {}
collapsible_frames = {}

# --- Tabelas dos Anexos ---
for anexo_id, dados in anexos.items():
    collapsible = CollapsibleFrame(scrollable_frame, text=f'{anexo_id} - {dados["nome"]}', expanded_by_default=False)
    collapsible.pack(pady=5, padx=20, fill="x")
    collapsible_frames[anexo_id] = collapsible
    Tooltip(collapsible.title_label, dados["descricao"])

    content = collapsible.content_frame
    columns = ("faixa", "faturamento", "aliquota", "deducao")
    tree = ttk.Treeview(content, columns=columns, show="headings", height=len(dados["faixas"]))
    trees[anexo_id] = tree
    
    tree.heading("faixa", text="Faixa")
    tree.heading("faturamento", text="Receita Bruta em 12 Meses")
    tree.heading("aliquota", text="Alíquota")
    tree.heading("deducao", text="Valor a Deduzir")

    tree.column("faixa", width=60, anchor="center")
    tree.column("faturamento", width=300)
    tree.column("aliquota", width=120, anchor="center")
    tree.column("deducao", width=180, anchor="e")

    for faixa in dados["faixas"]:
        faturamento_txt = f'De {format_currency(faixa["min"])} a {format_currency(faixa["max"])}'
        if faixa["min"] == 0:
            faturamento_txt = f'Até {format_currency(faixa["max"])}'
        tree.insert("", "end", values=(faixa["faixa"], faturamento_txt, f'{faixa["aliquota"]}%', format_currency(faixa['deducao'])))
    
    tree.pack(fill="x", expand=True, padx=10, pady=5)

# --- Iniciar a Aplicação ---
app.mainloop()