Editor de Sequências de DNA

Um editor interativo em Python que permite modificar uma sequência de DNA via linha de comando, com operações básicas de substituição, inserção e remoção de bases.

Contexto

Criado durante estudos de bioinformática para praticar manipulação de strings aplicada a sequências biológicas — simulando, de forma simplificada, o tipo de edição que ferramentas de biologia molecular fazem em sequências de DNA.

Como funciona

O programa mantém uma sequência de DNA em memória e apresenta um menu de opções no terminal. Cada operação (substituir, inserir ou remover uma base) atua sobre uma posição específica da sequência, sempre validando se a posição informada é válida antes de aplicar a mudança. A sequência atualizada é exibida após cada ação.

Como rodar
bash
python editor_dna.py
Exemplo de uso
Sequência de DNA original: ATCGGATAC

Menu de Modificação de DNA
1 - Substituir base
2 - Inserir base
3 - Remover base
4 - Mostrar sequência atual
0 - Sair
Escolha uma opção: 1
Posição da base a substituir (começa do 0): 2
Nova base (A, T, C ou G): T
Nova sequência: ATTGGATAC
Funcionalidades
Substituir base: troca a base em uma posição específica
Inserir base: adiciona uma nova base em uma posição da sequência
Remover base: exclui a base de uma posição específica
Mostrar sequência atual: exibe o estado atual da sequência
Possíveis melhorias futuras
Validar se a base inserida é realmente A, T, C ou G
Permitir carregar a sequência inicial a partir de um arquivo
Adicionar contagem de bases (A, T, C, G) na sequência atual
Tecnologias

Python (biblioteca padrão, sem dependências externas)
