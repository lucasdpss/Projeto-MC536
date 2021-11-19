from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')

driver.get("http://www.ssp.sp.gov.br/transparenciassp/Consulta.aspx")

crime = driver.find_element_by_id("cphBody_btnFurtoCelular")

time.sleep(45)

id_mes = "cphBody_lkMes"


for j in range(9):
    id_aux = id_mes + str(j + 1)
    mes = driver.find_element_by_id(id_aux)
    mes.click()
    time.sleep(2)
    download = driver.find_element_by_id("cphBody_ExportarBOLink")
    download.click()
    time.sleep(3)

id_mes = "cphBody_lkMes"
id_ano = "cphBody_listAno"

for i in range(18, 15, -1):
    id_aux = id_ano + str(i)
    ano = driver.find_element_by_id(id_aux)
    ano.click()
    time.sleep(5)
    for j in range(12):
        id_aux = id_mes + str(j+1)
        mes = driver.find_element_by_id(id_aux)
        mes.click()
        download = driver.find_element_by_id("cphBody_ExportarBOLink")
        download.click()
        time.sleep(3)
