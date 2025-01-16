##############################################################################
Chapter Bluetooth
##############################################################################

This chapter mainly introduces how to make simple data transmission through Bluetooth of ESP32-WROOM and mobile phones.

Project 3.1 Bluetooth Low Energy Data Passthrough
*********************************************************

Component List
===============================

.. list-table:: 
   :width: 100%
   :header-rows: 1 
   :align: center
   
   * -  ESP32-WROOM x1
     -  USB cable

   * -  |Chapter01_00|
     -  |Chapter01_01|

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png

Circuit
============================

Connect your computer and ESP32 with a USB cable.

.. image:: ../_static/imgs/Preface/Preface09.png
    :align: center

Lightblue
============================

If you can't install Serial Bluetooth on your phone, try LightBlue.If you do not have this software installed on your phone, you can refer to this link: https://apps.apple.com/us/app/lightblue/id557428110#?platform=iphone

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_24.png
    :align: center

Code
==============================

Move the program folder “ **Freenove_ESP32_WROOM_Board/Python/Python_Codes** ” to disk(D) in advance with the path of “ **D:/Micropython_Codes** ”.

Open “Thonny”, click “This computer” -> “D:”  ->  “Micropython_Codes”  ->  “03.1_BLE”. Select “ble_advertising.py”, right click your mouse to select “Upload to /”, wait for “ble_advertising.py” to be uploaded to ESP32-WROOM and then double click “BLE.py”. 

03.1_BLE
-------------------------------

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_25.png
    :align: center

Click run for BLE.py.

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_26.png
    :align: center

Turn ON Bluetooth on your phone, and open the Lightblue APP. 

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_27.png
    :align: center

In the Scan page, swipe down to refresh the name of Bluetooth that the phone searches for. Click ESP32.

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_28.png
    :align: center

After Bluetooth is connect successfully, Shell will printer the information.

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_29.png
    :align: center

Click “Receive”. Select the appropriate Data format in the box to the right of Data Format. For example, HEX for hexadecimal, utf-string for character, Binary for Binary, etc. Then click SUBSCRIBE.

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_30.png
    :align: center

You can type “12345” in Shell and press “Enter” to send.

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_31.png
    :align: center

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_32.png
    :align: center

And then you can see the mobile Bluetooth has received the message.

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_33.png
    :align: center

Similarly, you can select “Send” on your phone. Set Data format, and then enter anything in the sending box and click Write to send.

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_34.png
    :align: center

You can check the message from Bluetooth in “Shell”.

.. image:: ../_static/imgs/3_Bluetooth/Chapter03_35.png
    :align: center

And now data can be transferred between your mobile phone and computer via ESP32-WROOM.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/03.1_BLE/BLE.py
    :linenos: 
    :language: python
    :dedent:

Define the specified UUID number for BLE vendor.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/03.1_BLE/BLE.py
    :linenos: 
    :language: python
    :lines: 20-28
    :dedent:

Write an _irq function to manage BLE interrupt events.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/03.1_BLE/BLE.py
    :linenos: 
    :language: python
    :lines: 46-63
    :dedent:

Initialize the BLE function and name it.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/03.1_BLE/BLE.py
    :linenos: 
    :language: python
    :lines: 36-36
    :dedent:

When the mobile phone send data to ESP32 via BLE Bluetooth, it will print them out with serial port; When the serial port of ESP32 receive data, it will send them to mobile via BLE Bluetooth.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/03.1_BLE/BLE.py
    :linenos: 
    :language: python
    :lines: 80-96
    :dedent: