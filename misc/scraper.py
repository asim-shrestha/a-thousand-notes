from selenium import webdriver
import os
import time

# path to chromedriver.exe 
path = 'D:\Downloads\chromedriver_win32/chromedriver.exe'
# create nstance of webdriver
driver = webdriver.Chrome(path)


# Sign in to system
URL = 'https://melobytes.com/en/signin'
driver.get(URL)

# Find form, add values, and login
input_forms = driver.find_elements_by_class_name("ninput")
print(len(input_forms))
input_forms[0].send_keys("test@test.com")
input_forms[1].send_keys("test")
driver.find_element_by_id("do_signin").click()
time.sleep(5) # Wait for login


# Travel to page to send in image
melobytes = 'https://melobytes.com/en/app/image2music'
driver.get(melobytes)
# Code to open a specific url
IMAGE=os.getcwd()+"/img.png" # Path to my image within my drive
drop_target = driver.find_element_by_id("appfrmrow_in_file")

# Code to use JS to drag and drop an image
JS_DROP_FILE = """
    var target = arguments[0],
        offsetX = arguments[1],
        offsetY = arguments[2],
        document = target.ownerDocument || document,
        window = document.defaultView || window;

    var input = document.createElement('INPUT');
    input.type = 'file';
    input.onchange = function () {
      var rect = target.getBoundingClientRect(),
          x = rect.left + (offsetX || (rect.width >> 1)),
          y = rect.top + (offsetY || (rect.height >> 1)),
          dataTransfer = { files: this.files };

      ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        var evt = document.createEvent('MouseEvent');
        evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        evt.dataTransfer = dataTransfer;
        target.dispatchEvent(evt);
      });

      setTimeout(function () { document.body.removeChild(input); }, 25);
    };
    document.body.appendChild(input);
    return input;
"""

# Drop the image within the drop zone
drag_driver = drop_target.parent
file_input = drag_driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
file_input.send_keys(IMAGE)
time.sleep(5)

# Click the create song button
create_target = driver.find_element_by_id("do_run_app")
create_target.click()

# Poll until we have a result
result_links = None
while(not result_links):
    try:
        result_links = driver.find_elements_by_class_name("res_link")
    except:
        print('sleeping')
        time.sleep(5)

# Print the song link of the result
print([result_link.get_attribute("href") for result_link in result_links])
