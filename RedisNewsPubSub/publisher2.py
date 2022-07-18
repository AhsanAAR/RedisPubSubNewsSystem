


#import necessary modules
import csv
import redis

className = -1
article = []
message = ""

redisClient = redis.StrictRedis(host='localhost',  port=6379,db=0)

while True:

    className = -1
    topic = input("Enter Topic Name: ")
    message = " " #reset message value
    article = [] #reset article value
    # if(redisClient.hget("Channel1", topic) or redisClient.hget("Channel2", topic) or redisClient.hget("Channel3", topic) or redisClient.hget("Channel4", topic)):
    #     print("Cache Hit")
    #     print("Topic: ",topic)
    #     value = redisClient.hget("CacheTopics", topic).decode('UTF-8')  #convert bytes to string
        
    #     desc = value.split(",") #split the string using , 
    #     message = topic + "," + desc[1]  
    #     print("Class: ",desc[0]) 
    #     print("Description: ",desc[1]) 
    #     bmessage = bytes(message, 'utf-8') #converting string to bytesstring  
    #     print(type(desc[0]),"here")
    #     redisClient.publish(desc[0],bmessage)
    if(redisClient.hget("1", topic)):
        print("Cache Hit")
        print("Topic: ",topic)
        value = redisClient.hget("1", topic).decode('UTF-8')  #convert bytes to string
        
        desc = value.split(",") #split the string using , 
        message = topic + "," + desc[1]  
        print("Class: ",desc[0]) 
        print("Description: ",desc[1]) 
        bmessage = bytes(message, 'utf-8') #converting string to bytesstring  
        print(type(desc[0]),"here")
        redisClient.publish(desc[0],bmessage)
    elif(redisClient.hget("2", topic)):
        print("Cache Hit")
        print("Topic: ",topic)
        value = redisClient.hget("2", topic).decode('UTF-8')  #convert bytes to string
        
        desc = value.split(",") #split the string using , 
        message = topic + "," + desc[1]  
        print("Class: ",desc[0]) 
        print("Description: ",desc[1]) 
        bmessage = bytes(message, 'utf-8') #converting string to bytesstring  
        print(type(desc[0]),"here")
        redisClient.publish(desc[0],bmessage)
    elif(redisClient.hget("3", topic)):
        print("Cache Hit")
        print("Topic: ",topic)
        value = redisClient.hget("3", topic).decode('UTF-8')  #convert bytes to string
        
        desc = value.split(",") #split the string using , 
        message = topic + "," + desc[1]  
        print("Class: ",desc[0]) 
        print("Description: ",desc[1]) 
        bmessage = bytes(message, 'utf-8') #converting string to bytesstring  
        print(type(desc[0]),"here")
        redisClient.publish(desc[0],bmessage)
    elif(redisClient.hget("4", topic)):
        print("Cache Hit")
        print("Topic: ",topic)
        value = redisClient.hget("4", topic).decode('UTF-8')  #convert bytes to string
        
        desc = value.split(",") #split the string using , 
        message = topic + "," + desc[1]  
        print("Class: ",desc[0]) 
        print("Description: ",desc[1]) 
        bmessage = bytes(message, 'utf-8') #converting string to bytesstring  
        print(type(desc[0]),"here")
        redisClient.publish(desc[0],bmessage)


    else:
        print("Cache miss")

        with open('test.csv','rt')as f: #search the topic in file
            data = csv.reader(f)
            for row in data:
                    if(topic == (row[1])):
                        article = row
                        # print(type(article))
                        print("Topic: ",article[1]) #topic
                        print("Desc: ",article[2]) #description
                        className = article[0]
                        message = topic + "," + article[2]
                        bmessage = bytes(message, 'utf-8') #converting string to bytesstring                        
                        redisClient.publish(article[0],bmessage)

        if(className != -1):
            print("class of the article: ",className)

            with open('test.csv','rt')as g:       #cache all topics of that class
                data = csv.reader(g)
                channelName = className
                
                for row in data:
                    if(row[0] == className):
                        redisClient.hset(channelName, row[1],row[0]+","+row[2])

            redisClient.expire(channelName,10)
            print(channelName," expiry time",redisClient.ttl(channelName))       
        else:
            print("Topic not found")


    
    