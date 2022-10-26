from behave import *
from pages.home_testlink_page import HomeTestelink
from pages.github_page import *

homePage = HomeTestelink()
gitPage = GitHubPage()
gitLocator = GitHubPageLocator()

@given(u'que acesso a página do Testlink')
def step_impl(context):
    homePage.acessarTestelink("https://testlink.org/")


@given(u'que o usuário esteja no sistema Testlink')
def step_impl(context):
    titulo = homePage.driver.title
    assert titulo == 'TestLink'


@given(u'clique na opção "Acesse o repositório Git (GitHub)"')
def step_impl(context):
    homePage.clicarLinkGit()


@then(u'ele deve ser redirecionado para a página do repositório do GitHub do Testlink')
def step_impl(context):
    autor = gitPage.encontrarElemento(gitLocator.XPATH_AUTOR).text
    assert autor == "TestLinkOpenSourceTRMS"
