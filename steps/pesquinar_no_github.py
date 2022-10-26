from behave import *
from pages.github_page import *

gitPage = GitHubPage()
gitLocator = GitHubPageLocator()

@given(u'que o osuário esteja no GitHub')
def step_impl(context):
    creditos = gitPage.encontrarElemento(gitLocator.XPATH_CREDITO).text
    assert 'GitHub' in creditos


@given(u'escreva "LuizHenriqueVitorino" na aba de pesquisa do GitHub')
def step_impl(context):
    gitPage.pesquisar('LuizHenriqueVitorino')


@given(u'clique na opção "sear all of GitHub"')
def step_impl(context):
    gitPage.clicarSearAll()


@given(u'clique na opção "Users"')
def step_impl(context):
    gitPage.clicarUsers()


@then(u'deve aparecer a opção de clicar no Link que leva para a página do GitHub do Luiz Henrique')
def step_impl(context):
    user = gitPage.encontrarElemento(gitLocator.XPATH_URL_USER).text
    assert user == 'Luiz Henrique da Silva Vitorino'
