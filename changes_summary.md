## Resumo das Alterações e Tarefas Concluídas

Este documento resume as principais alterações e funcionalidades implementadas e corrigidas no projeto até o momento.

### 1. Configuração e Dependências
- Ativação do ambiente virtual Python e verificação da instalação das dependências.

### 2. Seção Blog - Modais para Artigos
- **Funcionalidade:** Os links "Ler mais" na seção "Blog" foram modificados para abrir os artigos em um modal pop-up, eliminando a necessidade de navegar para uma nova página.
- **Implementação:**
    - Reutilização da estrutura de modal existente no `templates/index.html`.
    - Adição de JavaScript para popular dinamicamente o título e o conteúdo do modal com base em atributos `data-` nos cartões de notícias.

### 3. Seção Contato - Integração Web3Forms
- **Funcionalidade:** A lógica de envio de e-mail do formulário de contato foi substituída pela integração com o serviço Web3Forms. O envio agora ocorre via AJAX, exibindo mensagens de sucesso/erro diretamente na página, sem recarregamento.
- **Implementação:**
    - Atualização do `templates/index.html` para submeter os dados do formulário diretamente para a API do Web3Forms, incluindo a `access_key` fornecida e um redirecionamento para a própria página de contato após o envio.
    - Limpeza do `app.py`, removendo a rota de envio de e-mail, importações relacionadas (`smtplib`, `ssl`, `email.message`, `request`, `redirect`, `url_for`, `flash`) e a configuração da `SECRET_KEY`.

### 4. Seção Blog - Correção na Busca de Notícias
- **Problema:** A busca de notícias do portal do Simples Nacional estava falhando.
- **Diagnóstico:** Análise da estrutura HTML do site alvo confirmou que os seletores (`div#ctl00_contentPlaceH_divNoticias`, `div.row`, `a.azulClaro`) estavam corretos. A falha foi atribuída a possíveis bloqueios de requisição.
- **Correção:** Adição de um cabeçalho `User-Agent` à chamada `requests.get()` em `app.py` para simular uma requisição de navegador padrão, melhorando a confiabilidade do scraping.

### 5. Seção "Quem Somos" - Ajustes de Layout (Parcialmente Revertidos)
- **Objetivo Inicial:** Centralizar o título "Nossa Equipe" e organizar os cartões dos membros lado a lado e centralizados.
- **Tentativas e Reversões:**
    - Reestruturação inicial do HTML para separar "Nossa Equipe" em uma seção própria e atualização da navegação.
    - **Reversão dessas alterações estruturais e de navegação** a pedido do usuário, confirmando que "Nossa Equipe" deve permanecer como uma subseção de "Quem Somos".
    - Tentativa de ajustar cores e tamanhos dos títulos "Nossa História" e "Nossa Equipe", que também foi revertida.
- **Estado Atual:** A seção "Quem Somos" foi restaurada à sua estrutura original, com "Nossa Equipe" e os cartões de membros dentro do `div.about-text`. O CSS foi ajustado para tentar centralizar o conteúdo dentro do `.about-text`.

### 6. Ajustes de Layout e Conteúdo (20/11/2025)

- **Geral:**
    - Removidas as linhas azuis decorativas que ficavam abaixo de cada título de seção.
    - Reduzido o espaçamento vertical entre os títulos de seção e seus respectivos subtítulos para um visual mais compacto.

- **Seção "Quem Somos":**
    - O tamanho da fonte dos títulos "Nossa História" e "Nossa Equipe" foi ajustado para `1.5rem`.
    - A lógica de estilização dos títulos foi corrigida para garantir que "Quem Somos" e "Nossa Equipe" possam ser modificados de forma independente, resolvendo um problema de herança de estilos.

- **Seção "Nossos Serviços":**
    - Os ícones dos cartões de serviço foram substituídos por imagens (PNGs) localizadas na pasta `static/icones`.
    - O tamanho da fonte dos títulos dos cartões foi reduzido para `1.35rem`.
    - A cor dos títulos dos cartões foi alterada para `var(--text-color)` (#333), para corresponder à cor do título "Notícias" na seção do Blog.

- **Seção "Simuladores":**
    - O cartão "Calculadora de Imposto de Renda" foi removido.
    - Adicionada uma nota de rodapé ("Calculadora meramente ilustrativa...") abaixo de cada botão de simulador.
    - Adicionado um aviso "Em breve." em vermelho ao lado dos botões dos simuladores "Lucro Presumido" e "Simples Nacional" para indicar que ainda não estão funcionais.

---
**Próximos Passos Pendentes:**
- Ajustar a cor e o tamanho dos títulos "Nossa História" e "Nossa Equipe" para serem pretos e ligeiramente menores, padronizando-os com o título "Notícias" da seção "Blog".
- Garantir que o "Nossa Equipe" e os cartões estejam centralizados e alinhados verticalmente com o "Nossos Serviços" (considerando a estrutura atual onde "Nossa Equipe" está dentro de "Quem Somos").