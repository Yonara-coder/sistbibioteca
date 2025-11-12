# Guia para Publicar no GitHub

## ✅ Passo 1: Commit já foi feito!
O repositório local já está pronto com todos os arquivos commitados.

## 📝 Passo 2: Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name:** `biblioteca` (ou outro nome de sua preferência)
   - **Description:** "Sistema de Gerenciamento de Biblioteca com Django e Jazzmin"
   - **Visibility:** Escolha Público ou Privado
   - **NÃO marque** "Add a README file" (já temos um)
   - **NÃO marque** "Add .gitignore" (já temos um)
   - **NÃO marque** "Choose a license" (opcional)
3. Clique em **"Create repository"**

## 🔗 Passo 3: Conectar e Fazer Push

Após criar o repositório, o GitHub mostrará comandos. Use estes comandos no terminal:

```bash
# Adicionar o repositório remoto (substitua SEU_USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU_USUARIO/biblioteca.git

# Renomear a branch para main (se necessário)
git branch -M main

# Fazer o push
git push -u origin main
```

## 🔐 Se pedir autenticação:

### Opção 1: Personal Access Token (Recomendado)
1. Vá em: https://github.com/settings/tokens
2. Clique em "Generate new token (classic)"
3. Dê um nome e selecione escopos: `repo`
4. Copie o token gerado
5. Use o token como senha quando o Git pedir

### Opção 2: GitHub CLI
```bash
# Instalar GitHub CLI (se não tiver)
# Windows: winget install GitHub.cli
# Depois: gh auth login
```

## ✅ Verificar

Após o push, acesse seu repositório no GitHub e verifique se todos os arquivos aparecem!

