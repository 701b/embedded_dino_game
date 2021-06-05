#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/device.h>
#include <linux/fs.h>
#include <linux/uaccess.h>
#include <linux/slab.h>
#include <linux/smp.h>
#include <linux/semaphore.h>
#include <linux/i2c-dev.h>
#include <linux/delay.h>
#include <asm/io.h>

MODULE_LICENSE("GPL");

/**
 * GPIO
 */

#define PERIPHERAL_BASE 0x3F000000UL
#define GPIO_BASE (PERIPHERAL_BASE + 0x200000)

void* gpioCtr = NULL;

void initGpio(void) {
    gpioCtr = ioremap(GPIO_BASE, 0x1000);
}

void closeGpio(void) {
    iounmap(gpioCtr);
}

void setGpioInput(int gpioNumber) {
    int regId = gpioNumber / 10;
    int pos = gpioNumber % 10;

    uint32_t* fselReg = (uint32_t*) (gpioCtr + 0x4 * regId);
    uint32_t fselVal = *fselReg;
    uint32_t mask = 0x7 << (pos * 3);

    fselVal = fselVal & ~mask;

    *fselReg = fselVal;
}

void getGpioInputValue(int gpioNumber, int* value) {
    int regId = gpioNumber / 32;
    int pos = gpioNumber % 32;

    #define GPIO_LEV_OFFSET 0x34
    uint32_t* levelReg = (uint32_t*) (gpioCtr + GPIO_LEV_OFFSET + 0x4 * regId);
    uint32_t* level = *levelReg & (0x1 << pos);

    *value = level ? 1 : 0;
}

void setGpioPullup(int gpioNumber) {
    int reg_id = gpioNumber / 32;
    int pos = gpioNumber % 32;

    #define GPIO_PUD_OFFSET 0x94
    #define GPIO_PUDCLK_OFFSET 0x98
    uint32_t* pud_reg = (uint32_t*) (gpioCtr + GPIO_PUD_OFFSET);
    uint32_t* pudclk_reg = (uint32_t*) (gpioCtr + GPIO_PUDCLK_OFFSET + 0x4 * reg_id);

    #define GPIO_PUD_PULLUP 0x2
    *pud_reg = GPIO_PUD_PULLUP;
    
    udelay(1);

    *pudclk_reg = (0x1 << pos);

    udelay(1);

    *pud_reg = 0;
    *pudclk_reg = 0;
}

/**
 * Driver
 */

#define MAJOR_NUM 0
#define DEVICE_NAME "rpikey"
#define CLASS_NAME "rpikey_class"

static int majorNumber;
static struct class* cRpiKeyClass = NULL;
static struct device* cRpiKeyDevice = NULL;

static int deviceOpen(struct inode* inode, struct file* file);
static int deviceRelease(struct inode* inode, struct file* file);
long deviceIoctl(struct file* file, unsigned int ioctlNum, unsigned long ioctlParam);

struct file_operations Fops = {
    .unlocked_ioctl = deviceIoctl,
    .open = deviceOpen,
    .release = deviceRelease,
};

static int deviceOpen(struct inode* inode, struct file* file) {
    printk(KERN_INFO "rpikey deviceOpen(%p)\n", file);
    return 0;
}

static int deviceRelease(struct inode* inode, struct file* file) {
    printk(KERN_INFO "rpikey deviceRelease(%p)\n", file);
    return 0;
}

long deviceIoctl(struct file* file, unsigned int ioctlNum, unsigned long ioctlParam) {
    if (ioctlNum == 100 || ioctlNum == 101) {
        uint32_t paramValue[1];
        int gpioNum;

        switch (ioctlNum)
        {
            case 100:
                gpioNum = 20;
                break;

            case 101:
                gpioNum = 21;
                break;
        }

        getGpioInputValue(gpioNum, &paramValue[0]);

        printk(KERN_INFO "rpikey button input GPIO%d: %d\n", gpioNum, paramValue[0]);

        copy_to_user((void*) ioctlParam, (void*) paramValue, sizeof(uint32_t));
    }

    return 0;
}

static int __init rpiKeyInit(void) {
    majorNumber = register_chrdev(MAJOR_NUM, DEVICE_NAME, &Fops);
    cRpiKeyClass = class_create(THIS_MODULE, CLASS_NAME);
    cRpiKeyDevice = device_create(cRpiKeyClass, NULL, MKDEV(majorNumber, 0), NULL, DEVICE_NAME);

    initGpio();

    setGpioInput(20);
    setGpioInput(21);
    setGpioPullup(20);
    setGpioPullup(21);

    return 0;
}

static void __exit rpiKeyExit(void) {
    closeGpio();

    device_destroy(cRpiKeyClass, MKDEV(majorNumber, 0));
    class_unregister(cRpiKeyClass);
    class_destroy(cRpiKeyClass);
    unregister_chrdev(majorNumber, DEVICE_NAME);
}

module_init(rpiKeyInit);
module_exit(rpiKeyExit);