# Roteiro de Execução 

Componentes: Gabriel Araújo, Guilherme Ferreira e Victor Ramos

Desenvolvemos 1 site dividido em duas partes, a primeira conta com proteção contra ataques, e o outro sem proteções, de forma que possamos testar possíveis ataques, mais precisamente o SQL INJECTION e ATAQUES XXS. Os sites se encontram no link: https://site-seguraca.herokuapp.com/ . As informações de login são: 

Login: jubileu

Senha: 123456

### EXEMPLO DE ATAQUE SQL INJECTION

Para simular um ataque SQL INJECTION primeiramente vamos no site sem proteção e nos campos de login vamos usar o seguinte script  ` ' OR 1=1 -- `. Após o procedimento de preenchimento das informações de login, clique no botão login e você terá acesso ao site.

```python	
def login_site_inseguro(request):
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == 'POST':
        user = request.POST.get('user', '')
        password = request.POST.get('password', '')
        query = UserInseguro.objects.raw(
            f"SELECT * FROM login_userinseguro WHERE 
             login_userinseguro.user='{user}' AND 
             login_userinseguro.password='{password}'"
        )
        if query:
            user = query[0]
            messages.add_message(request, messages.INFO, user)
            return redirect(reverse('site-inseguro'))
    context = {
        'message': 'site inseguro'
    }
    return render(request, 'login.html', context)
   ```

Acima temos o código do login do site inseguro, onde as informações de login e senha são concatenados na Query a ser executada. Logo abaixo tem o código do login seguro. Importante lembrar que o FRAMEWORK DJANGO faz uma consulta automatizada e segura, sem o risco de SQL INJECTION. 
```python
def login_site_seguro(request):
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == 'POST':
        user = request.POST.get('user', '')
        password = request.POST.get('password', '')
        try:
            user = UserInseguro.objects.get(user=user, password=password)
        except:
            user = None
        if user:
            messages.add_message(request, messages.INFO, user)
            return redirect(reverse('site-seguro'))
    context = {
        'message': 'site seguro'
    }
    return render(request, 'login.html', context)
	
```

### EXEMPLO DE ATAQUE XSS

Para efetuarmos o teste de XSS é necessário logar no “Site inseguro”, utilizando o usuário: jubileu e senha: 123456 ou por meio de SQL injection.
Após o login você vai se deparar com alguns alerts na página, eles são as consequências dos ataques XSS que aplicamos nos comentários.

Em um cenário inseguro não conseguimos visualizar os comentários que tem como conteúdo esses scripts;
 
No login seguro os comentários que possuem scripts são aceitos e visíveis para todos os usuários logados;  porém, não são executados. 

⚠⚠ a fim de avitar uso indevido a parte de adicionar novos comentários foi desativada

Exemplo do trecho de código DJANGO HTML, que faz o escape de todas as strings por padrão. Utilizando a tag explicitamente “autoescape off” conseguimos desativar esse escape padrão. 

```html
<div>
{% if site_seguro %}
    {{comment.comment}}
{% else %}
   {% autoescape off %}
        {{comment.comment}} 
   {% endautoescape %}
{% endif %}
</div>
```

Para executar o site localmente entre na pasta do projeto  e com o Python instalado e de preferência com a ambiente virtual digite no terminal:

> pip install -r  requirements

> python manage.py run server

