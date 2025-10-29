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
