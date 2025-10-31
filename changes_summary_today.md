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