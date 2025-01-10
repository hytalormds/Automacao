# Automação de Gestão de Backups

Este guia explica de forma simples como usar um script para fazer backups automáticos dos seus arquivos. O script organiza, lista, remove arquivos antigos e copia os mais novos para outro local.

---

## O que você precisa

1. **Python Instalado**:
   - O Python é necessário para rodar o script. Se você não o tiver, você pode baixar aqui: [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Diretórios Configurados**:
   - Certifique-se de que os seguintes lugares estão configurados no seu computador:
     - **/home/valcann/backupsFrom**: Onde estão os arquivos que você quer fazer backup.
     - **/home/valcann/backupsTo**: Para onde os arquivos mais recentes serão copiados.
     - **/home/valcann**: Onde o script vai guardar os registros.

---

## Como usar o script

1. **Baixe o arquivo**:
   - Faça o download do arquivo do script para o seu computador e salve-o com o nome `automacao_backups.py`.

2. **Abra o terminal**:
   - **No Windows**: Use o "Prompt de Comando".
   - **No Linux ou Mac**: Use o aplicativo "Terminal".

3. **Acesse a pasta do script**:
   - No terminal, digite o comando `cd` para ir até a pasta onde o script foi salvo. Exemplo:
     ```bash
     cd /caminho/para/o/arquivo
     ```

4. **Execute o script**:
   - No terminal, digite o seguinte e aperte Enter:
     ```bash
     python3 automacao_backups.py
     ```

---

## O que o script faz

1. Ele verifica os arquivos na pasta **/home/valcann/backupsFrom**.
2. Cria um arquivo chamado **backupsFrom.log** com informações sobre os arquivos, como nome, tamanho e datas.
3. Remove os arquivos que têm mais de 3 dias.
4. Copia os arquivos mais novos para a pasta **/home/valcann/backupsTo**.
5. Cria um arquivo chamado **backupsTo.log** com detalhes dos arquivos copiados.

---

## Dicas e Soluções Rápidas

- **Erro de permissão**: Se o script não conseguir acessar as pastas, verifique se você tem permissão para editar esses locais.
- **Diretório não encontrado**: Se as pastas não existirem, crie-as manualmente. Use o comando `mkdir` no terminal:
  ```bash
  mkdir -p /home/valcann/backupsFrom
  mkdir -p /home/valcann/backupsTo
  ```
- **Python não encontrado**: Verifique se o Python está instalado corretamente no seu computador.

---

Se tiver dúvidas ou dificuldades, peça ajuda para alguém que tenha experiência com computadores ou programação. Boa sorte!

---
