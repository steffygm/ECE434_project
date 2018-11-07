Griffin Steffy
hw04

NOTE: these two parts of the can not be run simutaneously, becuase there is a shared pin in setup

1. mmap

    1) run the configure_pins.sh script, it will configure the following pins to gpio
        P9_13: out
        P9_14: out
        P9_15: in
        P9_17: in
    2) type "make" into terminal and two executables will be outputed
        - button_2_led_mmap: this maps the state of a button to an led (13->15), (14->17)
        - fast_led_mmap: this blinks an led with a defined period inside of the c file

    3) run either of the two executables to examine the mmap implementation

    OSCILLISCOPE RESULTS:
        fastest period: 100us (input), read 125us (oscilliscope)
        CPU usage <5%, would jump around at initial run of 'htop'


2. SPI lcd display
    1) run the SPI_go.sh script
        - display tux on the lcd
        - rotate tux on the lcd
        - display text (My Name) on the lcd
        - run the movie file "RedsNighmare" on the lcd
        
========================
Professor Yoder's Comments

Looks good.  Did you try toggling without theusleep()?

Score:  10/10