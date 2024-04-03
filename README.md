# Animeflix

Animeflix é uma aplicação web simples, baseada na Netflix, desenvolvida em Django. Permite aos usuários visualizar detalhes sobre diferentes obras, assistir a episódios e criar uma conta para personalizar a experiência de usuário.

## Índice

- [Instalação](#instalação)
- [Funcionalidades](#funcionalidades)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Instalação

Para executar o projeto localmente, siga os passos abaixo:

1. Clone o repositório:

```bash
git clone https://github.com/RatingTax78753/Animeflix.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute as migrações do banco de dados:

```bash
python manage.py migrate
```

4. Execute o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse `http://localhost:8000` no seu navegador para visualizar a aplicação.

## Funcionalidades

- **Página Inicial**: Existem duas "páginas iniciais":

  - **Página Inicial para os usuários que não estão logados**: Não possui conteúdo relevante, apenas um botão de redirecionamento para fazer login. É para esta página que os usuários são redirecionados ao sair de suas contas.

  - **Página Inicial para os usuários que estão logados**: A "verdadeira página inicial", onde todo o conteúdo é exibido.

- **Detalhes da Obra**: Exibe informações detalhadas sobre uma obra específica e sugere outras obras relacionadas com base nas categorias.
- **Editar Perfil**: Permite aos usuários autenticados editar seu perfil.
- **Criar Conta**: Formulário de registro para novos usuários com validação de email e senha.
- **Barra de Navegação**: Pode ser dividida em três partes:

  - **Logo**: Uma imagem com a logo/nome do site, que, ao ser clicada, redireciona o usuário para a página principal.

  - **Campo de pesquisa**: Permite aos usuários pesquisar as obras pelos seus títulos.

  - **Dropdown**: Um dropdown com o nome do usuário, localizado no canto direito da barra de navegação. Ao ser clicado, exibe duas opções: editar ou sair de sua respectiva conta. Para os usuários administradores, uma opção a mais aparece: 'Editar Site', que redireciona o administrador para uma página que dá acesso ao banco de dados do site, permitindo adicionar/editar obras ou episódios.

## Contribuição

Se você deseja contribuir com este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request; afinal, sou um programador iniciante, quaisquer sugestões são bem-vindas.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).

## Contato

- Email: ruanvr2006@gmail.com
- GitHub: [RatingTax78753](https://github.com/RatingTax78753)
