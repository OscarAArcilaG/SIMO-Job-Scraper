from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas
import time
import os

start_time = time.time()

driver = webdriver.Chrome()
driver.get('https://simo.cnsc.gov.co/#ofertaEmpleo')
wait = WebDriverWait(driver, 10)

# Archivo ODS en el directorio actual
archivo_salida = os.path.join(os.getcwd(), "Simo.ods")

my_xpath_next_page = '//*[@id="dgrid_0"]/div[4]/div/div[2]/span[3]/span[3]'
element = wait.until(
    ec.element_to_be_clickable((By.XPATH, my_xpath_next_page))
)

my_xpath_number_of_pages = '//*[@id="dgrid_0"]/div[4]/div/div[2]/span[3]/span[3]'
numberOfPages = driver.find_element(
    By.XPATH,
    my_xpath_number_of_pages
).text

nivel = ["nivel del empleo"]
denominacion = ["denominacion del empleo"]
grado = ["grado del empleo"]
codigo = ["codigo del empleo"]
numeroOpec = ["numero opec"]
asignacionSalarial = ["asigacion salarial"]
convocatoria = ["convocatoria"]
cierreDeInscripciones = ["cierre de inscripciones"]
totalDeVacantes = ["total de vacantes"]
estudios = ["estudios"]
experiencia = ["experiencia"]


for page in range(1, int(numberOfPages) + 1):

    for num in range(0, 10):

        print("item: " + str(10 * (page - 1) + num + 1))

        base_xpath = (
            '/html/body/div[4]/div/div/div[2]/div/div/div[2]/div[4]/'
            'div/div[1]/div[3]/div[2]/div/div[' + str(num + 1) + ']'
        )

        my_xpath_nivel = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/p[1]/span[1]'
        )

        my_xpath_denominacion = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/p[1]/span[2]'
        )

        my_xpath_grado = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/p[1]/span[3]'
        )

        my_xpath_codigo = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/p[1]/span[4]'
        )

        my_xpath_numeroOpec = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/p[1]/span[5]'
        )

        my_xpath_asignacionSalarial = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/p[1]/span[6]'
        )

        my_xpath_vigenciaSalarial = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/p[1]/span[7]'
        )

        my_xpath_convocatoria= (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/p[1]/span[8]'
        )

        my_xpath_cierreDeInscripciones = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/p[1]/span[9]'
        )

        my_xpath_totalDeVacantes = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/div[1]'
        )

        my_xpath_encabezado = (
            base_xpath +
            '/div[1]/table/tr/td[1]/span/div/div[2]/button'
        )

        my_xpath_estudios = (
            base_xpath +
            '/div[2]/div/ul[2]/li[1]/span[2]'
        )

        my_xpath_experiencia = (
            base_xpath +
            '/div[2]/div/ul[2]/li[2]/span[2]'
        )

        try:
            wait.until(
                ec.element_to_be_clickable(
                    (By.XPATH, my_xpath_nivel)
                )
            )
            nivel.append(
                driver.find_element(
                    By.XPATH, my_xpath_nivel
                ).text
            )
        except:
            nivel.append('0')

        try:
            denominacion.append(
                driver.find_element(
                    By.XPATH, my_xpath_denominacion
                ).text
            )
        except:
            denominacion.append('0')

        try:
            grado.append(
                driver.find_element(
                    By.XPATH, my_xpath_grado
                ).text
            )
        except:
            grado.append('0')

        try:
            codigo.append(
                driver.find_element(
                    By.XPATH, my_xpath_codigo
                ).text
            )
        except:
            codigo.append('0')

        try:
            numeroOpec.append(
                driver.find_element(
                    By.XPATH, my_xpath_numeroOpec
                ).text
            )
        except:
            numeroOpec.append('0')

        try:
            asignacionSalarial.append(
                driver.find_element(
                    By.XPATH,
                    my_xpath_asignacionSalarial
                ).text
            )
        except:
            asignacionSalarial.append('0')

        try:
            convocatoria.append(
                driver.find_element(
                    By.XPATH, my_xpath_convocatoria
                ).text
            )
        except:
            convocatoria.append('0')

        try:
            cierreDeInscripciones.append(
                driver.find_element(
                    By.XPATH,
                    my_xpath_cierreDeInscripciones
                ).text
            )
        except:
            cierreDeInscripciones.append('0')

        try:
            totalDeVacantes.append(
                driver.find_element(
                    By.XPATH,
                    my_xpath_totalDeVacantes
                ).text
            )
        except:
            totalDeVacantes.append('0')

        try:
            element_encabezado = wait.until(
                ec.element_to_be_clickable(
                    (By.XPATH, my_xpath_encabezado)
                )
            )
            element_encabezado.click()
        except:
            pass

        try:
            estudios.append(
                driver.find_element(
                    By.XPATH, my_xpath_estudios
                ).text
            )
        except:
            estudios.append('0')

        try:
            experiencia.append(
                driver.find_element(
                    By.XPATH, my_xpath_experiencia
                ).text
            )
        except:
            experiencia.append('0')

    try:

        my_xpath_next_button = (
            '//*[@id="dgrid_0"]/div[4]/div/div[2]/span[4]'
        )

        next_button = wait.until(
            ec.element_to_be_clickable(
                (By.XPATH, my_xpath_next_button)
            )
        )

        next_button.click()

        try:
            wait.until(ec.staleness_of(next_button))
        except:
            print('Fail span4')

    except:

        try:

            my_xpath_next_button = (
                '//*[@id="dgrid_0"]/div[4]/div/div[2]/'
                'span[3]/span[3]'
            )

            next_button = wait.until(
                ec.element_to_be_clickable(
                    (By.XPATH, my_xpath_next_button)
                )
            )

            next_button.click()

            try:
                wait.until(ec.staleness_of(next_button))
            except:
                print('Fail span3')

        except:

            Data = pandas.DataFrame(
                zip(
                    nivel,
                    denominacion,
                    grado,
                    codigo,
                    numeroOpec,
                    asignacionSalarial,
                    convocatoria,
                    cierreDeInscripciones,
                    totalDeVacantes,
                    estudios,
                    experiencia
                )
            )

            # Guardar como OpenDocument Spreadsheet
            Data.to_excel(
                excel_writer=archivo_salida,
                engine="odf",
                index=False
            )

            print("Datos guardados en:")
            print(archivo_salida)

            input("Fail")


# Guardado final
Data = pandas.DataFrame(
    zip(
        nivel,
        denominacion,
        grado,
        codigo,
        numeroOpec,
        asignacionSalarial,
        convocatoria,
        cierreDeInscripciones,
        totalDeVacantes,
        estudios,
        experiencia
    )
)

Data.to_excel(
    excel_writer=archivo_salida,
    engine="odf",
    index=False
)

driver.quit()

print("Archivo generado:")
print(archivo_salida)

print("--- %s seconds ---" % (time.time() - start_time))
