CC = gcc
CFLAGS = 

all: button_2_led_mmap fast_led_mmap
	./configure_pins.sh

button_2_led_mmap: button_2_led_mmap.c beaglebone_gpio.h
	$(CC) $(CFLAGS) -o button_2_led_mmap button_2_led_mmap.c beaglebone_gpio.h

fast_led_mmap: fast_led_mmap.c beaglebone_gpio.h
	$(CC) $(CFLAGS) -o fast_led_mmap fast_led_mmap.c beaglebone_gpio.h

clean:
	rm button_2_led_mmap fast_led_mmap