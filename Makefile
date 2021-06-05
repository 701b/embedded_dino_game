BUILDROOT_OUTPUT=/home/vodiakana/buildroot/output

KERNEL_DIR=$(BUILDROOT_OUTPUT)/build/linux-custom/
CROSS_COMPILE=$(BUILDROOT_OUTPUT)/host/bin/arm-linux-

obj-m+=dinodriver.o

all: dinodriver

dinodriver:
	$(MAKE) ARCH=arm CROSS_COMPILE=$(CROSS_COMPILE) -C $(KERNEL_DIR) M=`pwd` modules
clean:
	$(MAKE) ARCH=arm CROSS_COMPILE=$(CROSS_COMPILE) -C $(KERNEL_DIR) M=`pwd` clean