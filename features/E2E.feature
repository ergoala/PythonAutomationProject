#Automation Challenge
Feature: Liverpool E2E
   Como usuario quiero validar el carrito de compras

@e2e
Scenario: Happy path E2E
    Given El usuario se enecuentra en la pagina liverpool
    When El usuario hace click en categorias
    Then El usuario hace hover en electronica
    And El usuario hace click en celulares
    Then El usuario hace click en 128 gb checkbox
    And El usuario selecciona el primer articulo
    When El usuario hace click en Agregar a mi bolsa
    When El usuario selecciona el carrito
    Then el usuario debe ingresar a la cartpage








