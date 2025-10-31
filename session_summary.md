## Resumo das Alterações da Sessão

### GitHub Pages Deployment Fix:
- Identificado que o GitHub Pages estava servindo a documentação em vez da landing page devido a um `index.html` específico do Flask na raiz.
- Gerado um `index.html` estático a partir de `templates/index.html`, substituindo as chamadas `url_for` do Flask por caminhos relativos (ex: `static/image.png`).
- Commit e push do `index.html` estático para a branch `gh-pages`.
- Revertido o `templates/index.html` na branch `main` para seu estado original (com `url_for`).

### Estilização da Seção "Blog":
- Aumentado o preenchimento superior e inferior da seção "Blog" (`#artigos`, `.news-section`) de `2rem` para `6rem`.

### Separadores do Menu de Navegação:
- Removida a regra CSS que adicionava separadores verticais entre os links de navegação (`nav ul li:not(:last-child)::after`).

### Layout da Seção "Quem Somos" (Alterações Iterativas):
- **Solicitação Inicial:** Usuário pediu para remover a imagem ao lado de "Nossa História" e expandir o parágrafo.
    - Removido o `div` `about-image`.
    - Alterado o CSS de `.about-content` de `grid-template-columns: 1fr 1fr;` para `grid-template-columns: 1fr;` para que o texto ocupasse a largura total.
- **Solicitação de Reversão 1:** Usuário pediu para reverter o posicionamento do parágrafo e manter os cartões "Nossa Equipe" como estavam.
    - Revertido o CSS de `.about-content` de volta para `grid-template-columns: 1fr 1fr;`.
- **Solicitação de Mover "Nossa História":** Usuário pediu para mover "Nossa História" e o parágrafo para a direita, deixando a esquerda vazia.
    - Adicionado um `div` vazio antes do `div` `about-text`.
- **Solicitação de Reversão 2:** Usuário pediu para reverter a alteração anterior.
    - Removido o `div` vazio que foi adicionado.
- **Solicitação de Adicionar Imagem:** Usuário pediu para adicionar `static/SisPeC-2.png` ao lado de "Nossa História", alinhada com o título, sem sobrepor "Nossa Equipe".
    - Re-adicionado o `div` `about-image` com a imagem `SisPeC-2.png` após o `div` `about-text`.
    - Ajustado o CSS de `.about-image` para `text-align: center; display: flex; justify-content: center; height: 100%;` para controlar seu tamanho e alinhamento.

### Opacidade da Imagem de Fundo:
- Ajustada a opacidade do `linear-gradient` na seção `.hero` de `0.92` para `0.95` para um contraste mais escuro.
- Ajustado `background-repeat` de `no-repeat, repeat` para `no-repeat` e `background-size` de `cover, 150px` para `cover` para a imagem de fundo da seção hero.

### Problema na Seção de Notícias:
- Identificado que a seção "Notícias" estava travada em "Carregando notícias..." devido a um problema de JavaScript. (Investigação em andamento, nenhuma correção aplicada ainda).