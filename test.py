import time
import serial
# from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import selenium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='COM3',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)

ser.isOpen()

print ('Enter your commands below.\r\nInsert "exit" to leave the application.')
profile = webdriver.FirefoxProfile()
profile.set_preference ('media.navigator.permission.disabled', True)
profile.update_preferences()
caps = DesiredCapabilities.FIREFOX
driver = webdriver.Firefox()
# driver = selenium.webdriver.remote.webdriver.WebDriver (command_executor="C:\Windows\geckodriver.exe", desired_capabilities=DesiredCapabilities.FIREFOX, browser_profile=profile)
driver.get('http://172.25.34.202/page.php');
input=1
while 1 :
    # get keyboard input
    # input = raw_input(">> ")
        # Python 3 users
        # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        # ser.write(input + '\r\n')
        out = ''
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(1)
        # while ser.inWaiting() > 0:
        out = ser.read(1)

        if out != '':
            print (out)
            # options = Options()
            # options.add_argument("--use-fake-ui-for-media-stream")
            # options.add_argument("--disable-user-media-security=true")
            # driver = webdriver.Firefox(executable_path="S:\shivam\chromedriver.exe", chrome_options=options)  # Optional argument, if not specified will search path.
           
            #time.sleep(20)
            driver.find_element_by_id('snap').click();
            time.sleep(5)
            driver.find_element_by_id('upload').click();
            time.sleep(2005)
