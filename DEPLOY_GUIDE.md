# 🚀 Guia de Deploy - Sistema de Biblioteca Django

## ⚠️ IMPORTANTE: GitHub Pages vs Deploy Completo

### GitHub Pages (Atual)
- ✅ Mostra página de demonstração estática
- ❌ **NÃO executa Django** (só serve arquivos HTML/CSS/JS)
- ❌ **NÃO tem banco de dados**
- ❌ **NÃO tem funcionalidades do admin**

### Deploy Completo (Necessário para sistema funcionar)
- ✅ Executa Django completo
- ✅ Banco de dados funcionando
- ✅ Painel admin funcional
- ✅ Todas as funcionalidades ativas

## 🎯 Solução: Deploy em Render (GRATUITO e FÁCIL)

### Passo 1: Preparar o Projeto

Os arquivos já foram criados:
- ✅ `render.yaml` - Configuração do Render
- ✅ `Procfile` - Comando de inicialização
- ✅ `requirements.txt` - Com dependências necessárias

### Passo 2: Criar Conta no Render

1. Acesse: https://render.com
2. Clique em **"Get Started for Free"**
3. Faça login com sua conta GitHub (Yonara-coder)

### Passo 3: Conectar Repositório

1. No dashboard do Render, clique em **"New +"** → **"Web Service"**
2. Conecte seu repositório GitHub: `Yonara-coder/sistbibioteca`
3. Render detectará automaticamente o `render.yaml`

### Passo 4: Configurar o Serviço

O Render usará as configurações do `render.yaml`, mas você pode ajustar:

**Configurações básicas:**
- **Name:** biblioteca-sistema (ou outro nome)
- **Region:** Escolha o mais próximo (ex: São Paulo)
- **Branch:** main
- **Root Directory:** (deixe vazio)
- **Runtime:** Python 3
- **Build Command:** `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
- **Start Command:** `gunicorn biblioteca_projeto.wsgi:application`

**Environment Variables (Variáveis de Ambiente):**
- `SECRET_KEY`: Gere uma chave secreta (Render pode gerar automaticamente)
- `DEBUG`: `False` (para produção)
- `ALLOWED_HOSTS`: `seu-app.onrender.com` (será fornecido pelo Render)

### Passo 5: Adicionar Banco de Dados (Opcional mas Recomendado)

1. No Render, clique em **"New +"** → **"PostgreSQL"**
2. Escolha o plano **Free**
3. Anote as credenciais do banco
4. Adicione as variáveis de ambiente no seu Web Service:
   - `DATABASE_URL`: (fornecido pelo Render)

### Passo 6: Criar Superusuário

Após o deploy, você precisará criar um superusuário:

1. No Render, vá em **"Shell"** do seu serviço
2. Execute:
```bash
python manage.py createsuperuser
```

### Passo 7: Acessar o Sistema

Após o deploy (5-10 minutos), seu sistema estará disponível em:
```
https://seu-app.onrender.com/admin/
```

## 🔄 Alternativas de Deploy

### Railway (Gratuito)
1. Acesse: https://railway.app
2. Conecte seu GitHub
3. Selecione o repositório
4. Railway detecta Django automaticamente
5. Adicione variáveis de ambiente se necessário

### PythonAnywhere (Gratuito para iniciantes)
1. Acesse: https://www.pythonanywhere.com
2. Crie conta gratuita
3. Faça upload do código via Git
4. Configure o servidor web

### Heroku (Pago, mas tem plano gratuito limitado)
1. Acesse: https://heroku.com
2. Instale Heroku CLI
3. Execute: `heroku create`
4. Execute: `git push heroku main`

## 📝 Checklist de Deploy

- [ ] Conta criada no Render/Railway
- [ ] Repositório conectado
- [ ] Variáveis de ambiente configuradas
- [ ] Deploy iniciado
- [ ] Superusuário criado
- [ ] Sistema acessível online
- [ ] Testado login no admin

## 🎉 Após o Deploy

Seu sistema estará **100% funcional** com:
- ✅ Painel admin completo
- ✅ Cadastro de livros, autores, membros
- ✅ Sistema de empréstimos e devoluções
- ✅ Tema visual de biblioteca aplicado
- ✅ Todas as funcionalidades ativas

## 🔗 Links Úteis

- **Render:** https://render.com
- **Railway:** https://railway.app
- **PythonAnywhere:** https://www.pythonanywhere.com
- **Documentação Django Deploy:** https://docs.djangoproject.com/en/4.2/howto/deployment/

