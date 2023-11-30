from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()

#driver = webdriver.Chrome()
#driver.get("http://www.python.org")
#assert "Python" in driver.title

class DoctorLoginTest(LiveServerTestCase):

    
    
    def testLoginForm(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000")
        username = driver.find_element('name', 'username')
        password = driver.find_element('name', 'password')
        id_ver_code = driver.find_element('name', 'verification_code')

        submit = driver.find_element('name', 'submit')

        username.send_keys("testDoc4")
        password.send_keys("Loki98012")
        id_ver_code.send_keys("640237")

        submit.send_keys(Keys.RETURN) 

        h = driver.find_element(By.TAG_NAME, 'h5')
        assert h.text == "Welcome, testDoc4"

        driver.get("http://127.0.0.1:8000/home")

        
        links = driver.find_elements(By.TAG_NAME, 'a')
        edit_appt_link = "blankatm"
        for link in links:
            print("\n\n")
            temp = link.get_attribute("href")
            if "editAppointment" in temp:
                edit_appt_link = temp
            print("\n\n")
        print('\n\n\n{}\n\n\n'.format(edit_appt_link))

        driver.get(temp)

        #now on edit appt page

        docNotes = driver.find_element('name', 'docNotes')
        apptdate = driver.find_element('name', 'apptDate')
        mypatient = driver.find_element('name', 'mypatient')

        submit = driver.find_element('name', 'submit')

        docNotes.send_keys("Some test notes from Doc.")
        apptdate.send_keys("12/5/2023")
        mypatient.send_keys(7)

        submit.send_keys(Keys.RETURN) 

        h = driver.find_element(By.TAG_NAME, 'h5')
        assert h.text == "Welcome, testDoc4"

        driver.get("http://127.0.0.1:8000/home")

        #now on to schedule appt doctor

        driver.get("http://127.0.0.1:8000/scheduleAppointmentDoctor")

        docNotes = driver.find_element('name', 'docNotes')
        apptdate = driver.find_element('name', 'apptDate')
        mypatient = driver.find_element('name', 'mypatient')

        submit = driver.find_element('name', 'submit')

        docNotes.send_keys("Some test notes from Doc.")
        apptdate.send_keys("12/5/2023")
        mypatient.send_keys(7)

        submit.send_keys(Keys.RETURN) 

        h = driver.find_element(By.TAG_NAME, 'h5')
        assert h.text == "Welcome, testDoc4"

        #now on to Add Patient

        #navigate to View Patients
        driver.get("http://127.0.0.1:8000/viewPatients")

        #assemble list of all patients
        links = driver.find_elements(By.TAG_NAME, 'a')
        addPatient_link = "home"
        for link in links:
            print("\n\n")
            temp = link.get_attribute("href")
            if "addPatient" in temp:
                addPatient_link = temp
            print("\n\n")
        print('\n\n\n{}\n\n\n'.format(addPatient_link))

        driver.get(temp)

        links = driver.find_elements(By.TAG_NAME, 'a')
        new_patient_link = "home"
        for link in links:
            print("\n\n")
            temp = link.get_attribute("href")
            if "helloMoon" in temp:
                new_patient_link = temp
            print("\n\n")
        print('\n\n\n{}\n\n\n'.format(new_patient_link)) #show the url we'd like to click

        driver.get(new_patient_link) #add patient

        h = driver.find_element(By.TAG_NAME, 'h5')
        assert h.text == "Welcome, testDoc4"


        #Now on to Add Diagnosis

        links = driver.find_elements(By.TAG_NAME, 'a')
        add_diagnosis_link = "home"
        for link in links:
            print("\n\n")
            temp = link.get_attribute("href")
            if "addDi" in temp:
                add_diagnosis_link = temp
            print("\n\n")
        print('\n\n\n{}\n\n\n'.format(add_diagnosis_link)) #show the url we'd like to click

        driver.get(add_diagnosis_link)

        diagnosis = driver.find_element('name', 'diagnosis')
        docNotes = driver.find_element('name', 'docNotes')
        mypatient = driver.find_element('name', 'mypatient')

        submit = driver.find_element('name', 'submit')

        docNotes.send_keys("Isolate and test while symptoms persist.")
        diagnosis.send_keys("COVID-19")
        mypatient.send_keys(7)

        submit.send_keys(Keys.RETURN) 

        h = driver.find_element(By.TAG_NAME, 'h5')
        assert h.text == "Welcome, testDoc4"

        #now on to SecureEditProfile

        driver.get("http://127.0.0.1:8000/viewPatients")

        links = driver.find_elements(By.TAG_NAME, 'a')
        edit_profile_link = "home"
        for link in links:
            print("\n\n")
            temp = link.get_attribute("href")
            print(temp)
            if "helloMoon" in temp:
                edit_profile_link = temp
            print("\n\n")
        print('\n\n\n{}\n\n\n'.format(edit_profile_link)) #show the url we'd like to click

        driver.get(edit_profile_link)

        links = driver.find_elements(By.TAG_NAME, 'a')
        edit_profile_link = "home"
        for link in links:
            print("\n\n")
            temp = link.get_attribute("href")
            print(temp)
            if "confirmPassword" in temp:
                edit_profile_link = temp
            print("\n\n")
        print('\n\n\n{}\n\n\n'.format(edit_profile_link)) #show the url we'd like to click

        driver.get(edit_profile_link)

        password = driver.find_element('name', 'password')
        submit = driver.find_element('name', 'submit')

        password.send_keys("Loki98012")
        submit.send_keys(Keys.RETURN) 

        symptoms = driver.find_element('name', 'symptoms')
        weight = driver.find_element('name', 'weight')
        allergies = driver.find_element('name', 'allergies')
        history = driver.find_element('name', 'history')
        submit = driver.find_element('name', 'submit')

        symptoms.send_keys("some symptoms")
        weight.send_keys(150)
        allergies.send_keys("some allergies")
        history.send_keys("some history")
        submit.send_keys(Keys.RETURN)

        h = driver.find_element(By.TAG_NAME, 'h5')
        assert h.text == "Welcome, testDoc4"

        #successfully passed all tests
        
        

        



    


        






# Create your tests here.
