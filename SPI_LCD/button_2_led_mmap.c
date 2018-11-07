// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <unistd.h>
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
        printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
        keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_addr_0;
    volatile unsigned int *gpio_oe_addr_0;
    volatile unsigned int *gpio_datain_0;
    volatile unsigned int *gpio_setdataout_addr_0;
    volatile unsigned int *gpio_cleardataout_addr_0;
    unsigned int reg_0;
    volatile void *gpio_addr_1;
    volatile unsigned int *gpio_oe_addr_1;
    volatile unsigned int *gpio_datain_1;
    volatile unsigned int *gpio_setdataout_addr_1;
    volatile unsigned int *gpio_cleardataout_addr_1;
    unsigned int reg_1;

    
    // Set the signal callback for Ctrl-C
        signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);
    
    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);

    gpio_addr_1 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

    printf("Mapping %X - %X (size: %X)\n", GPIO0_START_ADDR, GPIO0_END_ADDR, GPIO0_SIZE);

    gpio_addr_0 = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);

    gpio_oe_addr_1           = gpio_addr_1 + GPIO_OE;
    gpio_datain_1            = gpio_addr_1 + GPIO_DATAIN;
    gpio_setdataout_addr_1   = gpio_addr_1 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr_1 = gpio_addr_1 + GPIO_CLEARDATAOUT;
    gpio_oe_addr_0           = gpio_addr_0 + GPIO_OE;
    gpio_datain_0            = gpio_addr_0 + GPIO_DATAIN;
    gpio_setdataout_addr_0   = gpio_addr_0 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr_0 = gpio_addr_0 + GPIO_CLEARDATAOUT;


    if(gpio_addr_0 == MAP_FAILED) {
        printf("Unable to map GPIO_0\n");
        exit(1);
    }
    if(gpio_addr_1 == MAP_FAILED) {
        printf("Unable to map GPIO_1\n");
        exit(1);
    }

    printf("GPIO1 mapped to %p\n", gpio_addr_1);
    printf("GPIO1 OE mapped to %p\n", gpio_oe_addr_1);
    printf("GPIO1 SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr_1);
    printf("GPIO1 CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr_1);
    printf("GPIO0 mapped to %p\n", gpio_addr_0);
    printf("GPIO0 OE mapped to %p\n", gpio_oe_addr_0);
    printf("GPIO0 SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr_0);
    printf("GPIO0 CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr_0);


    // Set P9_14 to be an output pin
    reg_1 = *gpio_oe_addr_1;
    printf("GPIO1 configuration: %X\n", reg_1);
    reg_1 &= ~P9_14;       // Set P9_14 bit to 0
    *gpio_oe_addr_1 = reg_1;
    printf("GPIO1 configuration: %X\n", reg_1);

    reg_0 = *gpio_oe_addr_0;
    printf("GPIO0 configuration: %X\n", reg_0);
    reg_0 &= ~P9_13;       // Set P9_13 bit to 0
    *gpio_oe_addr_0 = reg_0;
    printf("GPIO0 configuration: %X\n", reg_0);


    printf("Start blinking LED P9_14\n");
    while(keepgoing) {
        if(*gpio_datain_0 & P9_17)
        {
            *gpio_setdataout_addr_0 = P9_13;
        }
        else
        {
            *gpio_cleardataout_addr_0 = P9_13;
        }
        if(*gpio_datain_1 & P9_15)
        {
            *gpio_setdataout_addr_1 = P9_14;
        }
        else
        {
            *gpio_cleardataout_addr_1 = P9_14;
        }
        //usleep(250000);
    }

    munmap((void *)gpio_addr_1, GPIO1_SIZE);
    munmap((void *)gpio_addr_0, GPIO0_SIZE);

    close(fd);
    return 0;
}

