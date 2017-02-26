/******************************************************************************
* Project Name      : CE211305_Inductive_Proximity_Sensing
* Version           : 1.0
* Device Used       : CY8C4A45LQI-L483
* Software Used     : PSoC Creator 3.3 CP3
* Compiler Used     : ARM GCC 4.9.3 
* Related Hardware  : CY8CKIT-048 PSoC Analog Coprocessor Pioneer Kit
*******************************************************************************
* Copyright (2016), Cypress Semiconductor Corporation.
*******************************************************************************
* This software, including source code, documentation and related materials
* ("Software") is owned by Cypress Semiconductor Corporation (Cypress) and is
* protected by and subject to worldwide patent protection (United States and 
* foreign), United States copyright laws and international treaty provisions. 
* Cypress hereby grants to licensee a personal, non-exclusive, non-transferable
* license to copy, use, modify, create derivative works of, and compile the 
* Cypress source code and derivative works for the sole purpose of creating 
* custom software in support of licensee product, such licensee product to be
* used only in conjunction with Cypress's integrated circuit as specified in the
* applicable agreement. Any reproduction, modification, translation, compilation,
* or representation of this Software except as specified above is prohibited 
* without the express written permission of Cypress.
* 
* Disclaimer: THIS SOFTWARE IS PROVIDED AS-IS, WITH NO WARRANTY OF ANY KIND, 
* EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, NONINFRINGEMENT, IMPLIED 
* WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
* Cypress reserves the right to make changes to the Software without notice. 
* Cypress does not assume any liability arising out of the application or use
* of Software or any product or circuit described in the Software. Cypress does
* not authorize its products for use as critical components in any products 
* where a malfunction or failure may reasonably be expected to result in 
* significant injury or death ("ACTIVE Risk Product"). By including Cypress's 
* product in a ACTIVE Risk Product, the manufacturer of such system or application
* assumes all risk of such use and in doing so indemnifies Cypress against all
* liability. Use of this Software may be limited by and subject to the applicable
* Cypress software license agreement.
*******************************************************************************/
/*******************************************************************************
* Theory of Operation: This code example demonstrates how to interface the 
* PSoC Analog Coprocessor with an inductive proximity sensor. The code example
* measures the change in onboard inductance to detect the presence of metal in 
* close proximity to an onboard coil. The measured sensor data is observed over I2C.
* The brightness of the RGB LED varies based on the proximity distance between the 
* sensor and the metal. 
*******************************************************************************/

/* Header File Includes */
#include <project.h>
#include <stdbool.h>
#define ADC_CHANNEL_IPS         (0u)
#define PWMSCALE                (2u)
/* Threshold value used for detecting metal.  
   Threshold = Minimum raw count – (Peak-to-Peak Noise count)
   Note: Minimum raw count and Peak-to-Peak Noise count are taken from BCP in the absence of metal */
#define THRESHOLD               (2350u)
#define METAL_DETECTED          (1u)
#define METAL_NOT_DETECTED      (0u)
/* I2C Read/Write Boundary */
#define RWBOUNDARY              (0u)
/* IIR Filter coefficient */
/* Cut off frequency = fs/(2 * pi * iir_filter_constant).  In this project fs ~= 2 ksps.
This results in a cut-off frequency of 5.3 Hz.  We are using IIR filter as FIR requires 
more order of filter to get the same cut-off frequency*/
#define FILTER_COEFFICIENT_IPS  (60u)
/* Structure that holds the sensor values */
/* Use __attribute__((packed)) for GCC and MDK compilers to pack structures      */
/* For other compilers use the corresponding directive.                          */
/* For example, for IAR use the following directive                              */
/* typedef __packed struct {..}struct_name;                                      */
typedef struct __attribute__((packed))
{
	uint16 sensorRawData;				/* ADC result */
	uint8 metalDetected;			    /* Metal detection status */
}ips_sensor_data;

/* Function Prototypes */
void InitResources(void);

/* Declare the i2cBuffer to exchange sensor data between Bridge Control 
Panel (BCP) and PSoC Analog Coprocessor */
//ips_sensor_data i2cBuffer = {0,METAL_NOT_DETECTED};

/*******************************************************************************
* Function Name: main
********************************************************************************
*
* Summary:
*  This function initializes all the resources, and in an infinite loop, performs tasks to measure the sensor
*  parameters and to send the data over I2C.
*
* Parameters:
*  None
*
* Return:
*  int
*
* Side Effects:
*   None
*******************************************************************************/
void doit(){
    int p1 =4;
    uint32 x[p1];
    int i=0;
    for(;i<p1;i++){
    x[i] = UART_1_UartGetChar();
    if(x[i]=='h'){break;}
    }
    while(UART_1_UartGetChar()!='h'){}
    i=0;
    for(;i<p1;i++){
    UART_1_UartPutChar(x[i]);
    }
}
int main()
{
    /* Variable to hold the duty cycle of PWM that drives the RGB LED */
    uint16 duty = 0;
    
    /* Variable to hold the ADC result */
    uint16 adcResult = 0;
    
    /* Variable to hold the sensor data */
    uint16 sensorRawData = 0;
    
    /* Variable to hold the metal detection  status */
    uint8 metalDetected = METAL_NOT_DETECTED;
    
    /* Variable to store the status returned by CyEnterCriticalSection()*/
    uint8 interruptState = 0;
    
    /* Enable global interrupts */
    CyGlobalIntEnable;
    
    /* Initialize hardware resources */
    InitResources();
    UART_1_Start();
    
    /* Infinite Loop */
    for(;;)
    {
        /* Check if ADC data is ready */
        if(ADC_IsEndConversion(ADC_RETURN_STATUS))
        {
            /* Get ADC result */
            adcResult = ADC_GetResult16(ADC_CHANNEL_IPS);
            
            /* Pass the ADC result through the IIR filter */
            sensorRawData = (adcResult + (FILTER_COEFFICIENT_IPS - 1) * sensorRawData) / FILTER_COEFFICIENT_IPS;
           
            /* Check if sensor data is below threshold */
            if(sensorRawData < THRESHOLD)
            {
               /* Set metal detection status variable */
               metalDetected = METAL_DETECTED; 
               
               /* Calculate duty cycle */
               duty = (THRESHOLD - sensorRawData) * PWMSCALE;
            
               /* Check if PWM duty cycle gets saturated */
               duty = (duty > PWM_PWM_PERIOD_VALUE) ? PWM_PWM_PERIOD_VALUE : duty;
            
               /* Control the duty cycle of PWM to change the LED intensity */
               PWM_WriteCompare(PWM_PWM_PERIOD_VALUE - duty);
              UART_1_UartPutChar('k');
               
               //doit();
            }
            else
            {
                metalDetected = METAL_NOT_DETECTED;
                /* Turn OFF the LED if metal is absent */
                PWM_WriteCompare(PWM_PWM_PERIOD_VALUE);
            }
        }
        /* Enter critical section to check if I2C bus is busy or not */
        /*interruptState = CyEnterCriticalSection();

        if(!(EzI2C_EzI2CGetActivity() & EzI2C_EZI2C_STATUS_BUSY))
        {
            i2cBuffer.sensorRawData = sensorRawData;
            i2cBuffer.metalDetected = metalDetected;   
        }
        CyExitCriticalSection(interruptState);*/
    }
}

/*******************************************************************************
* Function Name: void InitResources(void)
********************************************************************************
*
* Summary:
*  This function initializes all the hardware resources
*
* Parameters:
*  None
*
* Return:
*  None
*
* Side Effects:
*   None
*******************************************************************************/
void InitResources(void)
{
    /* Start EZI2C Slave Component and initialize buffer */
    //EzI2C_Start();
    //EzI2C_EzI2CSetBuffer1(sizeof(i2cBuffer), RWBOUNDARY, (uint8*)&i2cBuffer);

    /* Start Excitation PWM */
    ExcitationPWM_Start();
    
    /* Start the Scanning SAR ADC Component and start conversion */
    ADC_Start();
    ADC_StartConvert();
    
    /* Start Programmable Voltage Reference */
    PVref_Start();
    
    /* Enable Programmable Voltage Reference */
    PVref_Enable();
    
    /* Start Reference Buffer */
    VrefBuffer_Start();
    
    /* Start LED control PWM */
    PWM_Start();
    
    /* Start Opamp Component */
    Opamp_Start();
    
    /*Start Opamp_1 Component */
    Opamp_1_Start();

    /* Start Down Mixer Component */
    DownMixer_Start();
    
    /* Start Rectifier Component */
    Rectifier_Start();
}

/* [] END OF FILE */

