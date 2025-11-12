# 📄 Como Configurar o GitHub Pages

## ✅ Arquivos já enviados!

Os arquivos necessários já foram criados e enviados para o GitHub:
- ✅ `docs/index.html` - Página de demonstração
- ✅ `docs/static/admin/css/biblioteca_custom.css` - CSS customizado
- ✅ `.github/workflows/pages.yml` - Workflow de deploy automático

## 🔧 Passo a Passo para Ativar o GitHub Pages

### Opção 1: Usando GitHub Actions (Recomendado - Automático)

1. **Acesse as configurações do repositório:**
   - Vá em: https://github.com/Yonara-coder/sistbibioteca/settings/pages

2. **Configure a fonte:**
   - Em **"Source"**, selecione: **"GitHub Actions"**
   - Clique em **"Save"**

3. **Aguarde o deploy:**
   - O GitHub Actions irá automaticamente fazer o deploy
   - Pode levar alguns minutos na primeira vez
   - Você verá o progresso em: https://github.com/Yonara-coder/sistbibioteca/actions

4. **Acesse seu site:**
   - Após o deploy, seu site estará disponível em:
   - **https://yonara-coder.github.io/sistbibioteca/**

### Opção 2: Usando Branch main/docs (Alternativa)

Se a Opção 1 não funcionar:

1. **Acesse:** https://github.com/Yonara-coder/sistbibioteca/settings/pages

2. **Configure:**
   - **Source:** "Deploy from a branch"
   - **Branch:** `main`
   - **Folder:** `/docs`
   - Clique em **"Save"**

3. **Aguarde alguns minutos** e acesse:
   - **https://yonara-coder.github.io/sistbibioteca/**

## ⚠️ Importante

### O que o GitHub Pages mostra:
- ✅ Página de demonstração visual do projeto
- ✅ Informações sobre o sistema
- ✅ Tema visual customizado
- ✅ Documentação do projeto

### O que NÃO funciona no GitHub Pages:
- ❌ Aplicação Django completa (precisa de servidor Python)
- ❌ Banco de dados
- ❌ Funcionalidades interativas do admin

### Para ver o sistema funcionando completamente:
Você precisa executar localmente ou fazer deploy em:
- **Render** - https://render.com (gratuito)
- **Railway** - https://railway.app (gratuito)
- **Heroku** - https://heroku.com
- **PythonAnywhere** - https://pythonanywhere.com

## 🔍 Verificar Status do Deploy

1. Acesse: https://github.com/Yonara-coder/sistbibioteca/actions
2. Procure por "Deploy to GitHub Pages"
3. Clique para ver o progresso

## 📝 Notas

- O deploy pode levar **5-10 minutos** na primeira vez
- Após cada push na branch `main`, o site será atualizado automaticamente
- O site estará disponível em: **https://yonara-coder.github.io/sistbibioteca/**

## 🎉 Pronto!

Após configurar, seu site estará online e acessível publicamente!

