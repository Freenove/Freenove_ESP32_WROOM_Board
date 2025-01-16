##############################################################################
Chapter LED
##############################################################################

This chapter is the Start Point in the journey to build and explore ESP32 electronic projects. We will start with simple "Blink" project.

Project 1.1 Blink
************************************

In this project, we will use ESP32 to control blinking a common LED.

Component List
===================================

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

Power
-----------------------------------

ESP32-WROOM needs 5v power supply. In this tutorial, we need connect ESP32-WROOM to computer via USB cable to power it and program it. We can also use other 5v power source to power it.

.. image:: ../_static/imgs/Preface/Preface09.png
    :align: center

In the following projects, we only use USB cable to power ESP32-WROOM by default.

Sketch
===================================

According to the circuit, when the GPIO2 of ESP32-WROOM output level is high, the LED turns ON. Conversely, when the GPIO2 ESP32-WROOM output level is low, the LED turns OFF. Therefore, we can let GPIO2 circularly output high and low level to make the LED blink.

Upload the following Sketch: s

**Freenove_ESP32_WROOM_Board\Sketches\Sketch_01.1_Blink.**

Before uploading the code, click " **Tools** ", " **Board** " and select " **ESP32 Dev Module** ".

Select the serial port.

.. image:: ../_static/imgs/1_LED/Chapter01_02.png
    :align: center

.. note:: 
    
    For macOS users, if the uploading fails, please set the baud rate to 115200 before clicking "Upload Using Programmer".

.. image:: ../_static/imgs/1_LED/Chapter01_03.png
    :align: center

Sketch_01.1_Blink
------------------------------------

.. image:: ../_static/imgs/1_LED/Chapter01_04.png
    :align: center

Click "Upload", Download the code to ESP32-WROOM and your LED in the circuit starts Blink.

.. image:: ../_static/imgs/1_LED/Chapter01_05.png
    :align: center

:red:`If you have any concerns, please contact us via:` support@freenove.com

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_02.1_ButtonAndLed/Sketch_02.1_ButtonAndLed.ino
    :linenos: 
    :language: c
    :dedent:

The Arduino IDE code usually contains two basic functions: void setup() and void loop(). 

After the board is reset, the setup() function will be executed firstly, and then the loop() function.

setup() function is generally used to write code to initialize the hardware. And loop() function is used to write code to achieve certain functions. loop() function is executed repeatedly. When the execution reaches the end of loop(), it will jump to the beginning of loop() to run again.

.. image:: ../_static/imgs/1_LED/Chapter01_06.png
    :align: center

.. py:function:: Reset

    Reset operation will lead the code to be executed from the beginning. Switching on the power, finishing uploading the code and pressing the reset button will trigger reset operation.

In the circuit, ESP32-WROOM's GPIO2 is connected to the LED, so the LED pin is defined as 2.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 7-7
    :dedent:

This means that after this line of code, all PIN_LED will be treated as 2.

In the setup () function, first, we set the PIN_LED as output mode, which can make the port output high level or low level.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 10-11
    :dedent:

Wait for 1000ms, that is 1s. Delay () function is used to make control board wait for a moment before executing the next statement. The parameter indicates the number of milliseconds to wait for.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 17-17
    :dedent:

Then set the PIN_LED to output low level, and LED light off. One second later, the execution of loop () function will be completed. 

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 18-19
    :dedent:

The loop() function is constantly being executed, so LED will keep blinking.

Reference
---------------------------------

.. py:function:: void pinMode(int pin, int mode);	

    Configures the specified pin to behave either as an input or an output. 

    **Parameters**

    pin: the pin number to set the mode of.

    mode: INPUT, OUTPUT, INPUT_PULLDOWM, or INPUT_PULLUP.

.. py:function:: void digitalWrite (int pin, int value);	

    Writes the value HIGH or LOW (1 or 0) to the given pin which must have been previously set as an output.

For more related functions, please refer to https://www.arduino.cc/reference/en/