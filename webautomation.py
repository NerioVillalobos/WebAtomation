import sys
import re
from selenium import webdriver

regex = '^[a-z0-9]'

if len(sys.argv) >= 4:
    arg1 = str(sys.argv[1]).strip()
    arg2 = str(sys.argv[2]).strip()
    arg3 = str(sys.argv[3]).strip()
    if arg1 == '' or arg2 == '' or arg3 == '':
        print ('No posee Argunmento')
    else:
        if arg1 == 'login' or arg1 == 'test':
            print ('Ingresando a Org Tipo:',arg1)
            if(re.search(regex,arg2)):
                                 
                print("Usuario posee sintaxis correcta")
                driver = webdriver.Chrome()
                driver.get('https://'+arg1+'.salesforce.com')

                searchbox = driver.find_element_by_xpath('//*[@id="username"]')
                searchbox.send_keys(arg2)

                searchbox = driver.find_element_by_xpath('//*[@id="password"]')
                searchbox.send_keys(arg3)

                searchButton = driver.find_element_by_xpath('//*[@id="Login"]')
                searchButton.click()

                searchtitle = driver.title
                if searchtitle == 'Iniciar sesión | Salesforce':
                    driver.get_screenshot_as_file("result_fail_login.png")
                    print ('Error de Autenticacion, el usuario o la clave no son correctas')
                else:
                    print('Login Satisfactorio en la Org')
            else:
                print('El usuario ingresado no posee una sintaxis correcta') 
        else:
            print ('Usted coloco un parametro no aceptado, debe colocar login o test')
else:
    print ('Usted debe ingresar los tres (3) parametros requeridos para su ejecucion')
    print ('Ayuda: comando.py <Tipo de Org:[login|test] <Usuario:[usuario de la Org]> <Clave de la Org:[Clave]')
