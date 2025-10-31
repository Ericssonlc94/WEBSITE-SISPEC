# Resumo das Alterações no Website SisPeC

Este documento resume as modificações realizadas no layout e estilo do site.

## 1. Layout do Cabeçalho

O objetivo principal foi redesenhar o cabeçalho para aumentar seu tamanho e garantir que o menu de navegação ficasse perfeitamente centralizado na página, enquanto a logo da SisPeC permanecesse fixa no canto esquerdo, separada da centralização do menu.

- **Aumento de Tamanho:**
  - A altura do cabeçalho (`<header>`) foi aumentada para `120px`.
  - A altura da logo foi aumentada para `100px`, com a largura ajustando-se automaticamente para manter a proporção correta e evitar distorções.

- **Centralização do Menu e Posicionamento da Logo:**
  - Após algumas tentativas com Flexbox e posicionamento absoluto, a solução final e mais robusta foi implementada com **CSS Grid**.
  - O container do cabeçalho (`.header-content`) foi transformado em um grid de 3 colunas (`grid-template-columns: 1fr auto 1fr;`).
  - A **logo** foi posicionada na primeira coluna (à esquerda).
  - O **menu de navegação** foi posicionado na segunda coluna (central).
  - Um `div` vazio foi adicionado no HTML para atuar como um **espaçador explícito** na terceira coluna, garantindo que a primeira e a terceira colunas tenham sempre a mesma largura e que o menu no centro seja matematicamente alinhado com o centro da página.
  - Foi adicionado um `column-gap` de `2rem` para criar um espaçamento visual adequado entre a logo e o menu.

- **Responsividade (Layout Móvel):**
  - Para telas menores (abaixo de `768px`), o layout do grid é desfeito e substituído por um layout Flexbox (`display: flex; flex-direction: column;`), empilhando a logo e o menu verticalmente para uma melhor visualização em dispositivos móveis.

## 2. Fundo da Seção "Hero"

- A solicitação foi para alterar o fundo da primeira seção do site, que continha círculos coloridos, por um efeito de "papel timbrado" usando a imagem `Símbolo-positivo.png`.
- A imagem foi salva na pasta `static`.
- O CSS da seção `.hero` foi modificado para usar múltiplas camadas de fundo:
  1. Uma camada superior com um gradiente de cor semi-transparente.
  2. Uma camada inferior com a imagem `Símbolo-positivo.png`, configurada para se repetir (`background-repeat: repeat;`).
- **Diagnóstico de Problema:** O efeito de papel timbrado não funcionou porque a imagem fornecida era preta, o que a tornava invisível sob o gradiente de cor escuro.
- **Tentativa de Correção:** Tentei usar a propriedade `background-blend-mode: screen;` para "inverter" a cor da imagem e torná-la visível.
- **Rollback:** A tentativa com `background-blend-mode` foi revertida a seu pedido, retornando o CSS ao estado anterior (com a imagem de fundo configurada, mas não visível).

## 3. Ajustes de Estilo e Layout (Sessão Atual)

Nesta sessão, focamos em refinar a experiência do usuário, fontes, animações e alinhamento de conteúdo.

- **Fonte e Animações:**
  - A fonte principal do site foi alterada para 'Source Sans Pro', importada do Google Fonts, para uma aparência mais moderna.
  - Uma animação de `fade-in` foi adicionada ao título principal na seção "Hero".
  - Uma animação de `slide-in` da esquerda foi aplicada ao parágrafo de introdução para um carregamento mais dinâmico.

- **Layout da Seção "Hero":**
  - O botão "Nossos Serviços" teve seu estilo alterado para "outline", criando uma identidade visual consistente com o botão "Fale Conosco".
  - O título e o parágrafo da seção foram alinhados à esquerda para melhorar a legibilidade, mas os botões abaixo foram mantidos centralizados na página para um call-to-action claro.
  - O texto do parágrafo principal foi justificado.

- **Seção "Quem Somos":**
  - A imagem genérica ao lado de "Nossa História" foi substituída pela logo `Símbolo.png`.
  - O texto dos parágrafos da história foi justificado.
  - O alinhamento vertical da imagem e do texto foi ajustado para que ambos começassem no topo da seção.
  - Para que a imagem se alinhasse em altura apenas com o texto da história (sem invadir a seção da equipe), uma altura máxima (`max-height: 300px`) foi definida para a imagem, resolvendo o requisito de layout de forma visual.

- **Refatoração da Seção de Notícias (Revertida):**
  - Foi iniciada a implementação de uma nova seção "Artigos" e de um visualizador de notícias dinâmico que consumiria dados de um site externo.
  - A pedido, todas as alterações relacionadas a esta funcionalidade (no HTML, CSS, JavaScript e no back-end `app.py`) foram completamente revertidas, restaurando o site ao seu estado anterior.
# Resumo das Alterações - Dia 31/10/2025

## 1. Reorganização da Ordem dos Menus
- **Antes**: Home, Notícias, Artigos, Serviços, Simuladores, Quem Somos, Contato
- **Depois**: Home, Quem Somos, Serviços, Simuladores, Blog, Contato
- Atualizado o menu de navegação para seguir a ordem: Home, Quem Somos, Serviços, Simuladores, Blog (com "Nossos Artigos"), Contato

## 2. Reestruturação da Página
- Reorganização da ordem das seções para: Home, Quem Somos, Serviços, Simuladores, Artigos (Blog), Contato
- Criado layout em grade para a seção de blog com artigos principais e sidebar de notícias

## 3. Melhorias na Exibição de Notícias
- Implementado carrossel de notícias com setas de navegação e indicadores
- Implementado carrossel separado e mais compacto para a sidebar de notícias
- Adicionado tratamento específico para exibir notícias de forma diferente na sidebar vs. seção principal

## 4. Atualizações na Seção de Blog
- Criado layout de duas colunas para Blog: artigos principais (2/3) e notícias (1/3)
- Movido o título "Nossos Artigos" para aparecer acima dos cards de artigos
- Atualizado o título principal de "Blog - Nossos Artigos" para apenas "Blog"
- Adicionado subtítulo "Nossos Artigos" acima dos cards de artigos

## 5. Melhorias na Navegação
- Implementado animações mais suaves para os links da navegação
- Adicionado sublinhado animado que se expande da esquerda para a direita
- Ajustado espaçamento e tamanho da fonte para melhor acomodar todos os links
- Adicionado setas de navegação com efeito circular para o carrossel de notícias

## 6. Correções de Layout
- Adicionado scroll-margin-top para corrigir problema de seções escondidas atrás do header fixo
- Ajustado o espaçamento e posicionamento dos elementos para melhor responsividade
- Corrigido problema de quebra de linha em links longos no menu

## 7. Implementação de Separação
- Adicionado separadores visíveis entre as seções da página
- Criado separadores horizontais usando CSS após cada seção

## 8. Melhorias na Experiência de Notícias
- Implementado sistema de abertura de notícias em nova aba ao invés de popup
- Implementado popup para artigos enquanto notícias abrem em nova aba
- Criado função específica para lidar com redirecionamento de notícias

## 9. Atualizações de Títulos
- Alterado título da sidebar de notícias de "Notícias do Simples Nacional" para "Notícias"
- Removido subtítulo "Atualizações da Receita Federal"
- Mantido títulos alinhados verticalmente entre artigos e notícias

## 10. Organização de Código
- Consolidado funções duplicadas de carregamento de notícias
- Criado lógica condicional para tratar notícias diferentes em contextos diferentes (sidebar vs carrossel)
- Melhorada estrutura de código para maior legibilidade e manutenção
