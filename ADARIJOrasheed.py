#ADARIJO RASHEED PYTHON CODE TO GENERATE A SUMMARY REPORT OF TOTAL PHONE NUMBERS FOR EACH SERVICE PROVIDERS 
my_MTN_count = 0
my_Airtel_count = 0
my_Glo_count = 0
my_9Mobile_count = 0
my_MTEL_count = 0
my_MTN = ["0703","0706","0803","0806","0810","0813","0814","0816","0903","0906","0913","0916","07025","07026","0704"]
my_Airtel = ["0701","0708","0802","0808","0812",'0901',"0902","0904","0907","0912"]
my_Glo = ["0705","0805","0807","0811","0815","0905","0915"]
my_9Mobile = ["0809","0817","0818","0909","0908"]
my_MTEL= ["0804"]

def returnNetwork(number):    
    global my_MTN_count
    global my_Airtel_count
    global my_Glo_count
    global my_9Mobile_count
    global my_MTEL_count
    
    if number[0:4] in my_MTN or number[0:5] in my_MTN:
        my_MTN_count += 1
    
    elif number[0:4] in my_Airtel:
        my_Airtel_count += 1
    
    elif number[0:4] in my_Glo:
        my_Glo_count += 1
    
    elif number[0:4] in my_9Mobile:
        my_9Mobile_count += 1
    
    elif number[0:4] in my_MTEL:
        my_MTEL_count += 1
    
#interacting with text file given        
numberlist = open("PhoneNumbers.txt", "r")
for i in numberlist:
    returnNetwork(number = i)

print(my_MTN_count,"MTN Numbers in text file ")
print(my_Airtel_count,"Airtel Numbers in text file")
print(my_Glo_count,"Globacom Numbers in text file")
print(my_9Mobile_count,"9mobile Numbers in text file")
print(my_MTEL_count,"MTEL Numbers in text file")
#sum of all service provider to check if it totals 1 million phone numbers
print(my_MTN_count + my_Airtel_count +  my_Glo_count + my_9Mobile_count + my_MTEL_count)
